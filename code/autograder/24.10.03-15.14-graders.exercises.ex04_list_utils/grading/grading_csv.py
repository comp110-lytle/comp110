"""Create submission.csv for project grading."""

__author__ = "Kaki Ryan <kakiryan@cs.unc.edu>"
edited = "Chiara Sabato <csabato@unc.edu>" # added updates to work for single gradescope file of submissions

import os
import yaml
import pandas as pd
import re
from typing import List
import numpy as np

# set this to be whatever the big gradescope download folder is
GS_ASSIGNMENT_EXPORT: str = 'assignment_4333023_export'

# set this to be whatever the url is when you open the gradescope assignment and click on manage submissions
GS_SUBMISSIONS: str = "https://www.gradescope.com/courses/288698/assignments/1634500/submissions"

# put the list of UTAs here
utas: list[str] = ["Abigail Kessel", "Adin Zimmerman", "Andrew Zheng", "Aneka Happer", "Aryonna Rice",
"Austin Wade", "Ben Hites", "Catherine Roberts", "Chelsea Rowe", "Claire Helms", "CLayton Covington",
"David Karash", "David Nassif", "Emma Jia", "Erin Byrd", "Ezri White", "Fernando Garcia",
"Garrison Parrish", "Hannah Cruz", "Helen Charbonnet", "Janet Mbugua", "Jasper Christie",
"Jesse Wei", "Josh Lovett", "Kyle Sorensen", "Madeleine Genova", "Madyson Barber", "Manuela Danso-Fordjour",
"Marc Lewis", "Marlee Walls", "Matthew Kolsch", "Megan Zhang", "Meghan Sun", "Naomi Smith", "Olivia Wen",
"Quintin Gay", "Raine Thai", "Raven Taylor", "Rebekah Seawell", "Robert Suswell", "Sadie Amato", "Sophie Jiang",
"Tori Hoffman"]


def main() -> None:
    """Entry point of script. Expects to be run as CLI program."""
    submissions: list[str] = []
    urls: list[str] = []

    subs1: list[str] = os.listdir(GS_ASSIGNMENT_EXPORT)
    all_subs: list[str] = subs1

    for i in range(len(all_subs)):
        submission: str = all_subs[i]
        
        # this is just to skip the .DS_STORE file that sometimes shows up
        if submission[0] == '.':
            continue
        sub_num: str = re.compile("submission_(.*)$").search(submission).group(1)
        if 'yml' not in sub_num:
            submissions.append(sub_num)
            if i < len(subs1):
                urls.append(GS_SUBMISSIONS + "/" + sub_num)


    tuples = list(zip(submissions, urls))
    df = pd.DataFrame(tuples, columns=["Submission", "URL"])
    df.to_csv("submissions.csv")

    # split into equal groups depending on number of TAs (we had 40 fall 2020)
    groups = np.array_split(df, len(utas))
    for i in range(len(utas)):
        groups[i]['TA'] = utas[i]
        print(groups[i])

    pd.concat(groups).to_csv("submissions.csv")


if __name__ == "__main__":
    main()