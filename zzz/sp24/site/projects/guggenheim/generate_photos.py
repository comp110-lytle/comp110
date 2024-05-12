"""A script to generate student gallery of turtle submissions.

Usage: python -m students.guggenheim.generate_photos
"""

__author__ = ["Ezri White <ezri@live.unc.edu>"]

import csv
import subprocess
import os
import time


def parse_row(data, row_num):
    if "drive" in data[5]:
        name = data[4].replace(" ", "")
        file_name = f"{row_num}{name}"
        if not os.path.exists(f"static/photo_submissions/{file_name}.png"):
            link = data[5].replace("open", "u/1/uc")
            print(f"\"{link}&export=download\"")
            subprocess.call(
                ["curl", "-L", "--output", f"static/photo_submissions/{file_name}.png", f"{link}&export=download"])
            subprocess.call(
                ["convert", f"static/photo_submissions/{file_name}.png", "-resize", "400", f"static/photo_submissions/{file_name}.png"])
            time.sleep(1)


def main():

    with open('students/guggenheim/entries.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        row_num = 0
        for row in csv_reader:
            parse_row(row, row_num)
            row_num += 1


if __name__ == "__main__":
    main()
