"""A script to generate student gallery of turtle submissions.

Usage: python -m students.guggenheim.generate_index
"""

__author__ = ["Ezri White <ezri@live.unc.edu>"]

import csv


def intro() -> str:
    return ["---", "\ntitle: Guggenheim Museum", "\nauthor:", "\n- Ezri White", "\npage: guggenheim", "\ntemplate: layout.html", "\n---", "\n"]


def entry(data, row_num) -> str:
    if "drive" in data[5]:
        name = data[4].replace(" ", "")
        file_name = f"{row_num}{name}"
        art_path = f"\n<img src='../../static/photo_submissions/{file_name}.png' />"
    else:
        if "watch" in data[6]:
            link = data[6].replace("watch?v=", "embed/")
            if "feature" in link:
                link = link.split('&')[0]
        elif "youtu.be" in data[6]:
            link = data[6].replace("https://youtu.be/",
                                   "https://www.youtube.com/embed/")
        else:
            link = "https://www.youtube.com/embed/dQw4w9WgXcQ"

        art_path = f"<iframe src='{link}' frameborder='0' width='400px' height='225px' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>"
    return ["\n<div class='col-xl-4 col-lg-4 mb-4'>", f"\n<h5>{data[1]}</h5>", art_path, f"\n<h6>{data[4]}</h6>", f"\n<p>{data[2]}</p>", "\n</div>",  "\n"]


def main():

    path = "students/guggenheim/index.md"
    mode = "w"  # Write-only
    index = open(path, mode, encoding="utf8")

    index.writelines(intro())

    with open('students/guggenheim/entries.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        row_num = 0
        for row in csv_reader:
            index.writelines(entry(row, row_num))
            row_num += 1


if __name__ == "__main__":
    main()
