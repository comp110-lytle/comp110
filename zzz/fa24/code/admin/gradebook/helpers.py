import functools
import re
import math
from typing import Optional
import pandas as pd


def read_gradebook_csvs(csvs: list[str]) -> pd.DataFrame:
    """
    Given a list of gradebook CSV file paths from Gradescope, in reverse chronological order
    of final exam (such that the first non-zero grade assigned in an assignment wins),
    read all CSVs into a single DataFrame indexed off of the student's SID (onyen) in
    Gradescope.
    """
    if len(csvs) == 0:
        raise ValueError("List of CSVs must contain at least one path.")

    grades = pd.read_csv(csvs[0], encoding="utf-8").fillna(0.0)
    grades["Email"] = grades["Email"].str.lower()
    grades = grades.set_index("Email")
    for csv_path in csvs[1:]:
        csv = pd.read_csv(csv_path, encoding="utf-8").fillna(0.0)
        csv["Email"] = csv["Email"].str.lower()
        csv = csv.set_index("Email")
        for sid in csv.index:
            try:
                existing_row = grades.loc[sid]
                next_row = csv.loc[sid]
                for col in grades.columns[4:]:
                    try:
                        existing = float(existing_row[col])
                        new = float(next_row[col])
                        if math.isnan(existing) or existing == 0.0:
                            if not math.isnan(new) and new > 0.0:
                                grades.loc[sid, [col]] = new
                    except:
                        ...
            except KeyError:
                new_row = pd.DataFrame({sid: csv.loc[sid]}).T
                grades = pd.concat([grades, new_row], join="outer")
    return grades


def assignment_titles(grades: pd.DataFrame) -> list[str]:
    """
    Given a Gradebook from gradescope, extract the column names of all assignments.
    """
    return [col.replace(" - Max Points", "").strip() for col in grades.columns if "Max Points" in col]


def assignment_versions(titles: list[str]) -> dict[str, list[str]]:
    """
    Given a list of titles of all assignments, look for same prefix (e.g. FN00) and build up a list of all assignments
    with the same prefix. This is useful because for assignments with multiple versions (e.g. FN00 - A, FN00 - B) we 
    will want all titles various versions grouped together.
    """
    versions: dict[str, list[str]] = {}
    for title in titles:
        prefix = title[0:4]
        if prefix in versions:
            versions[prefix].append(title)
        else:
            versions[prefix] = [title]
    return versions



def component_titles(assignments: list[str], prefix: str) -> list[str]:
    """
    Given the list of assignments and a prefix, return only the assignments with the prefix.
    """
    return [a for a in assignments if a[0:len(prefix)] == prefix]

from typing import Callable
def bestof(versions: list[str]) -> Callable[[pd.Series], float]:
    def handle_row(row: pd.Series) -> float:
        max = 0.0
        for version in versions:
            pct = row[version] / row[f"{version} - Max Points"]
            if pct > max:
                max = pct
        return max
    return handle_row


def to_percentages(grades: pd.DataFrame) -> pd.DataFrame:
    """
    Given a Gradebook from gradescope, calculate percentage of points for each assignment.

    Truncate names to a format of XX## where XX is abbreviation for component and ## is number.
    """
    assignments = assignment_titles(grades)
    versions = assignment_versions(assignments)

    percents: dict[str, pd.Series] = dict()
    percents["Name"] = grades["Name"]
    percents["PID"] = grades["PID"]
    percents["Section"] = grades["Section"]
    percents["ONYEN"] = grades["ONYEN"]

    for assignment in versions:
        if len(versions[assignment]) == 1:
            percents[assignment] = grades[versions[assignment][0]] / grades[f"{versions[assignment][0]} - Max Points"]
        else:
            percents[assignment] = grades.apply(bestof(versions[assignment]), axis=1)


    return pd.DataFrame(percents)


from typing import Optional
from typing_extensions import TypedDict
COMPONENT = TypedDict("Component", {
    "prefix": str,
    "drops": int,
    "weight": float
})

def component_grade(grades_pct: pd.DataFrame, component: COMPONENT) -> pd.DataFrame:
    component_by_student = grades_pct[component_titles(grades_pct.columns, component["prefix"])].transpose()
    keep_n = component_by_student.shape[0] - component["drops"]
    component_score: dict[str, dict[str, float]] = dict()
    for student in component_by_student.columns:
        best = component_by_student[student].astype(float, errors = 'raise').nlargest(keep_n)
        component_score[student] = {
            component["prefix"]: best.mean(),
            f"{component['prefix']} (Pts)": best.mean() * component["weight"],
            f"{component['prefix']} (N)": int(best[best > 0.0].count())
        }
    component_score_df = pd.DataFrame(component_score).transpose()
    return component_score_df


def component_grades(grades_pct: pd.DataFrame, components: dict[str, dict[str, any]]) -> pd.DataFrame:
    grades = pd.DataFrame()
    grades["Name"] = grades_pct["Name"]
    grades["PID"] = grades_pct["PID"]
    grades["Section"] = grades_pct["Section"]
    grades["ONYEN"] = grades_pct["ONYEN"]
    total: pd.Series[float] = pd.Series()
    for c in components:
        grades_of_component = component_grade(grades_pct, components[c])
        grades = pd.concat([grades, grades_of_component], axis=1)
        if total.shape[0] == 0:
            total = grades[f"{components[c]['prefix']} (Pts)"]
        else:
            total += grades[f"{components[c]['prefix']} (Pts)"]
    grades["Total"] = total
    return grades

