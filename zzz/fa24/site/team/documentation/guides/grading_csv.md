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
- Quiz Grading
- Generating Spreadsheets for Project Grading
- Building and Deploying Autograders to Gradescope

## Overview

The grading team lead is mainly responsible for organizing weekly meetings for assignment/quiz grading, handling regrade requests, and allocating projects to TAs for them to grade. During quiz weeks, there may be a need to schedule multiple meetings in order to quickly grade and return quizzes back to students. It is important to check Gradescope often to keep up with regrade requests, especially in the weeks following the release of quiz or project grades as this is when the majority of regrades are requested. Occasionally, depending on the exercise/project, the grading team lead will also need to update the autograder - with the addition of the Curriculm Lead this is less likely, but still relevant.

## Quiz Grading

Gradescope has a lot of automation tools that make quiz grading much easier. There are grouping capabilities for multiple choice, text response, and math response. Instead of going through each question one at a time you are able to group them and then grade them all at once. The steps below describe how to group and grade questions that fall into those categories above. For diagraming question or code writing, grouping will not work and answers must be graded individually

### Multiple Choice, T/F, Short Response Questions

1. Click the desired quiz to grade
2. Select the number of the question to grade. It should have an underline appear when you hover over it. (If you click Submissions when it pops up it will take you to grade individually instead of grouping)
3. It will ask you whether you want to grade individually or grade in groups. Based on the type of question - MCQ, math written, text written - you can select the most fitting grouping category.
4. Gradescope will do a sizeable amount of the work sorting the responses but you need to scan over the sorted items to make sure they are correct. You will check each group one by one to make sure they're right before moving on to group the unsorted answers. (A lot of the time gradescope will misread parenthesis and brackets so it will create multiple groups with correct answers because it cannot tell the difference. Those groups can be merged together to make grading easier because there are less groups.)
5. Once the original groups have been checked and merged you can then select answers from whatever is left unsorted and place them in the correct group. You can also make new groups to put answers into - it is helpful here to look at the rubric to see if there are partial credit points and sort any answers into partial credit groups if they do not receive full credit, ex. using parenthesis instead of brackets for indexing may receive partial credit and sorting answers with parenthesis together may be easier to grade.
6. After answers have been sorted then clicking the Grade button on the bottom right will take you to grade each group. It will have you grade one answer from each group and then will apply your selection from the rubric to all other items in that group.

### Memory Diagrams and Code Writing

These questions are written and are not ones that can be sorted by gradescope - sometimes the output can be graded individually with grouping but the actual diagrams and code writing must be done one-by-one. These questions and their rubrics vary throughout the semester as the content gets more complex as the semester goes on.

In the past there have been grading teams formed of 5-ish TAs who would meet once the quizzes were scanned to start the grading and then most of the grading would be done by them and the Grading Lead. Recently TAs have been grading in All-Hands and individually and this has been successful where the Grading Lead helps answer questions about the rubric and make decisions for how to grade certain cases.

**Gradescope Shortcuts**

When grading these questions, it is easier to use the keyboard rather than the mouse. Each rubric item gets assigned to a number on the keyboard and any drop-down rubric items will have letters used to grade the individual rubric items in the drop-down. 

Z : takes you to the next ungraded submission
-> : takes you to the next submission in the sequence
<- : takes you back one submission in the sequence

### Regrade Requests

Regrade requests will technically be assigned to the person who graded the question. Typically regrade requests are questions that fall through the cracks with the grouping or memory diagrams questions. These should be done and responded to as soon as possible so students can know what their final grade is with the regrade. 

Sometimes regrade requests are written as trying to argue about receiving points back, generally it is clear whether the question was graded incorrectly and if the points should be returned back. If you have any concerns about a regrade request or do not know how to respond, ask for advice for how to handle it.

## Generating Spreadsheets for Project Grading

Once a project deadline has passed, the submissions must be divvied up among all the TAs for them to grade. Generate the spreadsheet using the following steps:

1. If you have already cloned the team110 repo, skip to step 2. Otherwise, follow the instructions under the `Clone the team110 Repo` section in the [Course Site Setup guide](/team/documentation/guides/course_site_setup.html).
2. Once you have cloned the repo, create and switch to a new branch using the following command: `git checkout -b <name of branch>`
3. Open the project assignment for section 1 on Gradescope and go to `Review Grades` (located on the left side of the page). At the bottom right of the screen, use the `Export Submissions` option and then download the zip that it produces. Locate the downloaded zip and extract the contents. You should see a folder with the name `assignment_<number>_export`. Inside the folder, you should see all the project submissions. Move the `assignment_<number>_export` folder into the `team110/code/autograder` folder (you can do this by simply dragging the folder directly from the file explorer to the `code` folder in VSCode). 
4. Open the `team110/code/grading/grading_csv.py` file. The file has several named constants. Assign the `GS_ASSIGNMENT_EXPORT` named constant to a string containing the name of the section 1 submissions folder (`"assignment_<number>_export"`).
5. Open the project assignment for section 1 on Gradescope again, but this time go to `Manage Submissions`. Copy the url and assign the `GS_SUBMISSIONS` named constant to a string containing the copied url. 
6. The `utas` variable stores a list of all the names of the UTAs on the team. Check the list to make sure all the UTAs are included and appear only once in the list. If any UTAs are missing, add their names to the list.
    * TODO: Find a way to import the list of UTAs from Airtable
7. Run the `grading_csv` file as a module  Make sure your terminal is in the right directory. If you type pwd in the terminal it should print `/Some/Path/.../comp110/code/autograder`. If you do not see this, trash the terminal and create a new one. When you create a new one it should prompt you for the desired working directory – select the `code` option. Once you are sure that your terminal is in the code directory, run the following command: `python -m grading.grading_csv`. This should generate a file named `submissions.csv` in the `team110/code` folder. Locate the `submissions.csv` file by right-clicking on it and selecting `Reveal in File Explorer`.
8. Create a google spreadsheet and go to File > Import > Upload and drag the `submissions.csv` file from the file explorer to the box to generate the spreadsheet. Modify the spreadsheet to include a checkbox beside each submission so TAs can mark off those they have graded. Change the spreadsheet settings so that anyone with the link can edit.
9. Create an announcement in Slack to notify the TAs of project grading allocations. Include the deadline and spreadsheet link in the announcement.

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

> Contributors: Andrew Zheng, Chiara Sabato
