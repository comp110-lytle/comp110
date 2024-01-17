from datetime import date, timedelta
from tabulate import tabulate
from IPython.display import HTML
from enum import Enum
from typing import Optional, Dict, List, Set


# Months
JAN = 1
FEB = 2
MAR = 3
APR = 4
MAY = 5
JUN = 6
JUL = 7
AUG = 8
SEP = 9
OCT = 10
NOV = 11
DEC = 12


# Weekdays
MON = 1
TUES = 2
WED = 3
THUR = 4
FRI = 5


class Kind(Enum):
    CL = "Class"
    LS = "Lesson"
    QZ = "Quiz"
    EX = "Exercise"
    PJ = "Project"
    FN = "Final"
    NA = "No Class"
    MS = "Milestone"
    RD = "Reading"
    DK = "Duke Game"
    RV = "Reviews"
    WD = "Wellness Day"
    HW = "Homework"
    EV = "Event"
    CQ = "Challenge Question"
    VL = "Virtual Lesson"


CL = Kind.CL
LS = Kind.LS
QZ = Kind.QZ
EX = Kind.EX
FN = Kind.FN
PJ = Kind.PJ
NA = Kind.NA
MS = Kind.MS
RD = Kind.RD
DK = Kind.DK
RV = Kind.RV
WD = Kind.WD
EV = Kind.EV
CQ = Kind.CQ
VL = Kind.VL


class Plan:
    kind: Kind
    n: int
    title: str
    date: date
    deadline: Optional[date]
    links: Dict[str, str]
    extension: Optional[date]

    def __init__(self, title: str, kind: Kind, n: int, date: date, deadline: Optional[timedelta] = None, links: Dict[str, str] = {}):
        self.kind = kind
        self.n = n
        self.title = title
        self.date = date
        self.deadline = deadline
        self.links = links
        self.extension = deadline

    def add_extension(self, ext_days: timedelta):
        """Extend assignment x amount of days"""
        self.extension = self.deadline + ext_days

    def __repr__(self) -> str:
        return f"{self.kind.name}{self.n:02} - {self.title}"


class HorizonPlan:
    descriptor: str
    links: Dict[str, str]
    date: date
    kind: Kind

    def __init__(self, descriptor: str, links: dict[str, str], date: date, kind: Kind):
        self.descriptor = descriptor
        self.links = links
        self.date = date
        self.kind = kind


def new_syllabus(fdoc: date, ldoc: date) -> Dict[date, List[Plan]]:
    """Establish a dictionary with a key for every date in the semester and plans for FDOC and LDOC."""
    syllabus: Dict[date, List[Plan]] = {}
    current_date: date = fdoc
    while current_date <= ldoc:
        syllabus[current_date] = []
        current_date += timedelta(1)
    syllabus[fdoc].append(Plan("FDOC", MS, 0, fdoc))
    syllabus[ldoc].append(Plan("LDOC", MS, 1, ldoc))
    return syllabus


def cut(dates: Dict[date, List[Plan]], start: date, end: date) -> Dict[date, List[Plan]]:
    """Cut a slice of a schedule such that you can play around with it interactively."""
    """
    Retains references to the Plans but the dictionary and lists per date are unique.
    This way we can play around with a cut of a date and then paste the dates back in 
    to a main calendar once we're happy with how it shapes up.
    """
    copy = {}
    for day in dates:
        if day >= start and day <= end:
            copy[day] = []
            for plan in dates[day]:
                copy[day].append(plan)
    return copy


def merge(a: Dict[date, List[Plan]], b: Dict[date, List[Plan]]) -> Dict[date, List[Plan]]:
    """Merge two schedules back together and produce a new schedule."""
    merged = {}
    days = list(a.keys())

    for day in b:
        if day not in days:
            days.append(day)

    for day in days:
        merged[day] = []
        if day in a:
            for plan in a[day]:
                merged[day].append(plan)
        if day in b:
            for plan in b[day]:
                if plan not in merged[day]:
                    merged[day].append(plan)
    return merged

def calendar_table(dates: Dict[date, List[Plan]], end_date: date = None) -> HTML:
    """Produce an HTML calendar representation of a Date->List[Plan] dictionary."""
    table = [["Date", "Weekday", "Plan"]]
    week: int = 0
    first_day = next(iter(dates))
    last_date = None
    outstanding: Dict[date, List[Plan]] = {}
    for current_date in dates:
        if end_date is not None and current_date > end_date:
            break
        if current_date == first_day or current_date.isoweekday() == 1:
            table.append([f"Week {week}"])
            week += 1
        if len(dates[current_date]) > 0:
            for plan in dates[current_date]:
                title = plan.title
                if plan.deadline is not None:
                    title = f"Out: {title}"
                    if plan.deadline in outstanding:
                        outstanding[plan.deadline].append(plan)
                    else:
                        outstanding[plan.deadline] = [plan]

                if current_date != last_date:
                    table.append([plan.date.strftime("%b-%d"),
                                 plan.date.strftime("%a"), title])
                else:
                    table.append(["", "", title])

                last_date = current_date
        # Handle things whose deadline is on this date
        if current_date in outstanding:
            for plan in outstanding[current_date]:
                if current_date != last_date:
                    table.append([current_date.strftime(
                        "%b-%d"), current_date.strftime("%a"), f"Due: {plan.title}"])
                else:
                    table.append(["", "", f"Due: {plan.title}"])
                last_date = current_date
            del outstanding[current_date]
    return table


def show_calendar(dates: Dict[date, List[Plan]], end_date: date = None) -> HTML:
    """Produce an HTML calendar representation of a Date->List[Plan] dictionary."""
    table = [["Date", "Weekday", "Plan"]]
    week: int = 0
    first_day = next(iter(dates))
    last_date = None
    outstanding: Dict[date, List[Plan]] = {}
    for current_date in dates:
        if end_date is not None and current_date > end_date:
            break
        if current_date == first_day or current_date.isoweekday() == 1:
            table.append([f"Week {week}"])
            week += 1
        if len(dates[current_date]) > 0:
            for plan in dates[current_date]:
                title = plan.title
                if plan.deadline is not None:
                    title = f"Out: {title}"
                    if plan.deadline in outstanding:
                        outstanding[plan.deadline].append(plan)
                    else:
                        outstanding[plan.deadline] = [plan]

                if current_date != last_date:
                    table.append([plan.date.strftime("%b-%d"),
                                 plan.date.strftime("%a"), title])
                else:
                    table.append(["", "", title])

                last_date = current_date
        # Handle things whose deadline is on this date
        if current_date in outstanding:
            for plan in outstanding[current_date]:
                if current_date != last_date:
                    table.append([current_date.strftime(
                        "%b-%d"), current_date.strftime("%a"), f"Due: {plan.title}"])
                else:
                    table.append(["", "", f"Due: {plan.title}"])
                last_date = current_date
            del outstanding[current_date]
    sched = tabulate(table, tablefmt="html", stralign="left",
                     colalign=("left", "left", "left"))
    return HTML(sched)


def horizonize(dates: Dict[date, List[Plan]], end_date: date = None) -> list[HorizonPlan]:
    """Creates a dict of dates and their relative formatted deliverables. A bit of hardcoding here, could prob be optimized."""
    horizon_dates: list[HorizonPlan] = []
    for entry in dates:
        for item in dates[entry]:
            d8: date
            time: str
            if item.extension is not None:
                d8 = item.extension
                time = " 11:59pm"
            else:
                continue
            descript: str = str(item.kind).strip(
                "Kind.") + "0" + str(item.n) + " - " + (d8.strftime("%a, %b %d")).upper() + time
            if item.extension != item.deadline:
                descript: str = str(item.kind).strip(
                    "Kind.") + "0" + str(item.n) + "*(EXTENDED)* - " + (d8.strftime("%a, %b %d")).upper() + time
            plan = HorizonPlan(descript, strip_links(
                item.links), d8, item.kind)
            horizon_dates.append(plan)

    horizon_dates.sort(key=lambda item: item.date)
    return horizon_dates


def strip_links(links: Dict[str, str]):
    for x in links:
        if links[x] != "":
            return {x: links[x]}
    return links


def meeting_days(start: date, end: date, weekdays: Set[int], exceptions: Set[date]) -> List[date]:
    """Generate a list of days the class meets on."""
    days = []
    day: date = start
    while day <= end:
        if day.isoweekday() in weekdays and day not in exceptions:
            days.append(day)
        day += timedelta(1)
    return days


def schedule(title: str, calendar: Dict[date, List[Plan]], kind: Kind, n: int, on_date: date, deadline: date = None) -> Plan:
    plan = Plan(title, kind, n, on_date, deadline)
    if plan.date in calendar:
        calendar[plan.date].append(plan)
    else:
        calendar[plan.date] = [plan]
    return plan


def serialize_links(link: Dict[str, str]):
    # convert links
    return {}


def serialize_plan(plan: Plan):

    return {"kind": plan.kind.name,
            "n": plan.n,
            "title": plan.title,
            "date": str(plan.date),
            "deadline": str(plan.deadline),
            "links": plan.links}


def serialize(syllabus: Dict[date, List[Plan]]):
    serializeable_syllabus = {}
    for key in syllabus:
        new_key = key.isoformat()
        serializeable_syllabus[new_key] = []
        for plan in syllabus[key]:
            new_plan = serialize_plan(plan)
            serializeable_syllabus[new_key].append(new_plan)

    return serializeable_syllabus


VL_FILE_PREFIX = '---\ntitle: Virtual Lessons\nauthor:\n    - Alyssa Byrnes\npage: lessons\n---'


def generate_VL_index_page(lesson_list: list):
    lpage = VL_FILE_PREFIX + "\n\n"
    # page += '<div class="row">\n<div class="col-lg-6 col-md-12">\n'
    # lpage += '<div class="box link-page m-2 p-4">\n\n'
    lesson_number = 0
    for lesson in lesson_list:
        if lesson_number < 10:
            num_str = "LS0" + str(lesson_number) + " "
        else:
            num_str = "LS" + str(lesson_number) + " "
        [title, link_dict] = lesson
        lpage += f'<div class="plan Class"><span class="kind">{num_str}</span>\n'
        lpage += f'<span class="title">{title}:</span>\n'
        link_str = ""
        for link in link_dict.keys():
            if (link != "Assignment"):
                link_str += f'[{link}]({link_dict[link]}) | '
        lpage += link_str[:-3] + '\n'
        lpage += '</div>\n\n'
        lesson_number += 1

    # write lpage to a lessons page
    f = open("../../../site/virtual-classes/index.md", "w")
    f.writelines(lpage)
    f.close()


def make_VL_page(lesson_list: list, CQ_list: list, VL_idx: int, lesson_idx: int, CQ_idx: int):
    if VL_idx < 10:
        VL_number = "0" + str(VL_idx)
    else:
        VL_number = str(VL_idx)
    VL_prefix = '---\ntitle: Virtual Lesson ' + VL_number + \
        '\nauthor:\n    - Alyssa Byrnes\npage: lessons\n---'
    lpage = VL_prefix + "\n\n"
    # page += '<div class="row">\n<div class="col-lg-6 col-md-12">\n'
    lpage += '# Lessons\n'
    lpage += '<div class="box link-page m-2 p-4">\n\n'
    lesson_file = "VL" + VL_number + ".md"
    lesson_number = lesson_idx
    for lesson in lesson_list:
        if lesson_number < 10:
            num_str = "LS0" + str(lesson_number) + " "
        else:
            num_str = "LS" + str(lesson_number) + " "
        [title, link_dict] = lesson
        lpage += f'<div class="plan Class"><span class="kind">{num_str}</span>\n'
        lpage += f'<span class="title">{title}:</span>\n'
        link_str = ""
        for link in link_dict.keys():
            link_str += f'[{link}]({link_dict[link]}) | '
        lpage += link_str[:-3] + '\n'
        lpage += '</div>\n\n'
        lesson_number += 1
    lpage += "</div>\n\n"
    if len(CQ_list) >= 1:
        cq_number = CQ_idx
        lpage += '# Challenge Questions\n'
        lpage += '<div class="box link-page m-2 p-4">\n\n'
        for cq in CQ_list:
            if cq_number < 10:
                num_str = "CQ0" + str(cq_number) + " "
            else:
                num_str = "CQ" + str(cq_number) + " "
            [title, link_dict] = cq
            lpage += f'<div class="plan Class"><span class="kind">{num_str}</span>\n'
            lpage += f'<span class="title">{title}:</span>\n'
            link_str = ""
            for link in link_dict.keys():
                link_str += f'[{link}]({link_dict[link]}) | '
            lpage += link_str[:-3] + '\n'
            lpage += '</div>\n\n'
            cq_number += 1
        lpage += "</div>\n\n"
    # write lpage to a lessons page
    f = open("../../../site/virtual-classes/" + lesson_file, "w")
    f.writelines(lpage)
    f.close()
