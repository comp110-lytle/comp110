---
title: Team Lead Guide to Grading
date: 2022-01-10
author:
- Andrew Zheng
page: team
template: overview
site-branch: team
---

## Key Objectives

- Overview
- Generating Spreadsheets for Project Grading
- Building and Deploying Autograders to Gradescope

## Overview

The grading team lead is mainly responsible for organizing weekly meetings for assignment/quiz grading, handling regrade requests, and allocating projects to TAs for them to grade. During quiz weeks, there may be a need to schedule multiple meetings in order to quickly grade and return quizzes back to students. It is important to check Gradescope often to keep up with regrade requests, especially in the weeks following the release of quiz or project grades as this is when the majority of regrades are requested. Occasionally, depending on the exercise/project, the grading team lead will also need to update the autograder. 

## Generating Spreadsheets for Project Grading

Once a project deadline has passed, the submissions must be divvied up among all the TAs for them to grade. Generate the spreadsheet using the following steps:

1. If you have already cloned the team110 repo, skip to step 2. Otherwise, follow the instructions under the `Clone the team110 Repo` section in the [Course Site Setup guide](/team/documentation/guides/course_site_setup.html).
2. Once you have cloned the repo, create and switch to a new branch using the following command: `git checkout -b <name of branch>`
3. Open the project assignment for section 1 on Gradescope and go to `Review Grades` (located on the left side of the page). At the bottom right of the screen, use the `Export Submissions` option and then download the zip that it produces. Locate the downloaded zip and extract the contents. You should see a folder with the name `assignment_<number>_export`. Inside the folder, you should see all the project submissions. Move the `assignment_<number>_export` folder into the `team110/code` folder (you can do this by simply dragging the folder directly from the file explorer to the `code` folder in VSCode). 
4. Repeat step 3 for the section 2 project submissions.
5. Open the `team110/code/grading/grading_csv.py` file. The file has several named constants. Assign the `GS_ASSIGNMENT_EXPORT_1` named constant to a string containing the name of the section 1 submissions folder (`"assignment_<number>_export"`) and assign the `GS_ASSIGNMENT_EXPORT_2` named constant to a string containing the name of the section 2 submissions folder.
6. Open the project assignment for section 1 on Gradescope again, but this time go to `Manage Submissions`. Copy the url and assign the `GS_SUBMISSIONS_1` named constant to a string containing the copied url. Repeat this process with section 2 and the `GS_SUBMISSIONS_2` named constant.
7. The `utas` variable stores a list of all the names of the UTAs on the team. Check the list to make sure all the UTAs are included and appear only once in the list. If any UTAs are missing, add their names to the list.
    * TODO: Find a way to import the list of UTAs from Airtable
8. Run the `grading_csv` file as a module. Make sure your terminal is in the right directory. If you type pwd in the terminal it should print `/Some/Path/.../team110/code`. If you do not see this, trash the terminal and create a new one. When you create a new one it should prompt you for the desired working directory – select the `code` option. Once you are sure that your terminal is in the code directory, run the following command: `python -m grading.grading_csv`. This should generate a file named `submissions.csv` in the `team110/code` folder. Locate the `submissions.csv` file by right-clicking on it and selecting `Reveal in File Explorer`.
9. Create a google spreadsheet and go to File > Import > Upload and drag the `submissions.csv` file from the file explorer to the box to generate the spreadsheet. Modify the spreadsheet to look like [this](https://docs.google.com/spreadsheets/d/1-VCluD-GqdE-zfbX5IuTJlXDLYau0ugSMejDRu82ejs/edit?usp=sharing). Change the spreadsheet settings so that anyone with the link can edit.
10. Contact Kris to decide on expectations for when all project grading should be complete. Create an announcement in Slack to notify the TAs of project grading allocations. Include the deadline and spreadsheet link in the announcement.

Note: Some students will inevitably turn in their projects late (after the spreadsheet has been generated). In this case, the grading team should handle the late submissions at one of the meetings.

## Building and Deploying Autograders to Gradescope

Sometimes exercise or project autograders need to be updated. Follow these steps for building and configuring the updated autograder in Gradescope.

1. If you have already cloned the team110 repo, skip to step 2. Otherwise, follow the instructions under the `Clone the team110 Repo` section in the [Course Site Setup guide](/team/documentation/guides/course_site_setup.html).
2. Once you have cloned the repo, create and switch to a new branch using the following command: `git checkout -b <name of branch>`.
3. Locate the test file that needs to be updated. Test files for exercises should be found in `team110/code/graders/exercises` and test files for projects should be found in `team110/code/graders/projects`.
4. Once the test files have been updated, create the grader zip: `python -m grading.build <path to folder containing test files>`. For example, to build the autograder for ex01, run the command `python -m grading.build graders.exercises.ex01`. In the `team110/code` folder, you should now see a file named `yy.mm.dd-hh.mm-graders.exercises.ex01.zip`. Right-click on this zip file and select `Reveal in File Explorer`.
5. Go to the course Gradescope page and open the assignment. Select `Configure Autograder` on the left side of the screen. Replace and update the autograder with the zip that was just created. This kicks off the Docker Image build on Gradescope's end. It typically takes a few minutes to install the latest Python and packages we depend upon. The very last step, once it has completed, is "Successfully tagged gradescope/autograders:University_of_North_Carolina_..."
6. Once the autograder has finished updating, go to the `Manage Submissions` tab and select the `Regrade All Submissions` option to update the students' grades.
7. Stage (`git add <path to file>`), commit (`git commit -m "<commit message>"`), and push (`git push origin <branch name>`) the updated test files to the team110 repo.

> Contributors: Andrew Zheng
