---
title: Team Lead Guide to Worksheets
date: 2021-04-15
author:
- Megan Zhang
- Jasper Christie 
page: logistics

template: overview
site-branch: team
---

## Key Objectives

- Preparation
- Writing the Questions
- Review
- Compiling
- Workspace Items

## Overview

An optional practice worksheet is made available to students before every quiz and is intended to reinforce the topics that will be covered on the quiz. Practice worksheets in Spring 2021 have been in the form of pages on the course website, which has the benefit of always being in the same place and not overwhelming students with more Gradescope assignments. This and some of the other decisions we made about practice worksheets this semester may need to change in the future, especially when COMP 110 is taught in-person again. This guide will explain the process we used to make practice worksheets.

## Preparation

Our goal is to write questions that will reinforce the main topics covered on quizzes. To do this, start by talking to Kris about upcoming content near the beginning of a unit. Write down the topics that will be covered in the next quiz and consider what types of questions could address those topics.

## Writing the Questions

Begin by making a list of the types and number of questions you want to write. Try to include both **conceptual** and **application-based** questions.

> **Conceptual-based** questions can include true/false and short-answer.

> **Application-based** questions can include code/function-writing, code-tracing, and environment diagramming.

For example, you may decide to write 5 true/false questions, 2 code-tracing questions, and 2 environment diagramming questions. If there is more than one person working on a worksheet, divide the questions evenly between team members.

Once you have decided the number and types of questions you need to write, feel free to reference examples from lecure, review sessions, and previous semesters’ practice for inspiration. Make sure to communicate with other team members about question formatting, if applicable. _You may choose to draft these questions in a Google or Word Doc._

> For example, the Spring 2021 environment diagramming questions included a short sentence of instructions followed by a screenshot of the code from VSCode and a few sub-questions. (i.e. “What is the printed output?”, “How many frames are on the stack?”)

### Example Problems

Here are some examples of worksheet problems we created:

> List Diagramming 1:
> Given the code listing below, draw an environment diagram then answer the questions that follow.

![](/static/team/worksheets/exampleq.png)

**Solution**:

![](/static/team/worksheets/exampleq-answer.png)

---

> Function Writing: Write a definition for a function called reverse, which has one parameter of type str named string and returns a str that has all the characters of string in reverse order. Use a while loop. For example, a call to reverse with “hello” would return “olleh”.

**Solution**:

![](/static/team/worksheets/exampleq2-answer.png)


### Problem Solutions

**Tip**: As you complete the questions, make sure to write down the answers as well. True/False, short-answer, and code-tracing solutions can simply be typed.

Code/function-writing solutions should be typed in VSCode and then screenshotted with the line numbers included. Environment diagramming solutions should be drawn using a digital tool (i.e. Google Drawings) and screenshotted.

Place the solutions on a separate page below the questions in your document.

## Review

After you finish writing the questions, make sure to review them for spelling mistakes or any other inconsistencies. Double-check your answers to avoid confusion from students who will be working through the worksheet later.

If you are working with other team members, make sure to set aside time to meet and look over each other’s questions and answers. Make sure that there are no overlaps or strong similarities between them. Provide each other feedback and see if anything needs to be added or updated. If so, either go ahead and make the changes while you are together or meet again after the changes have been made.

## Compiling

Once you have completely reviewed the questions and checked for mistakes, it is time to compile the worksheet. If you are working with other team-members, compile all of your questions in one place. This could be a single pdf, a page on the website, or another format. If you are unsure, ask Kris how he prefers the practice worksheets to be distributed to students. For Spring 2021, this meant putting the questions on the COMP 110 website. Make sure the questions are numbered correctly and organized by topic (i.e. place the true/false questions under one section, diagramming questions in another section, etc.)

Depending on the format of the practice worksheets during your semester, you may need to make the answer key separate from the questions. In Spring 2021, however, the questions and answers were placed on the same page on the COMP 110 website. The questions were placed at the top of the page with subheadings for different sections. The answers were placed at the very bottom.

Finally, double check with Kris before making the practice worksheet public. He may request changes or offer last-minute suggestions for the questions. Once the worksheet has been approved, push it out to students in whatever format you have chosen for the semester. In Spring 2021, this meant pushing the changes from the worksheet branch to the master branch of <https://github.com/comp110/team110>, which added the practice worksheet page that we created to the COMP 110 website for student access.

## Workspace Items

This section discusses how we create pages for the website on GitHub, which includes working in branches through VS Code.

All of this happens in the team110 repository at <https://github.com/comp110/team110> in the site directory. When we want to create a new worksheet page, we switch to the worksheet branch. To check what local branches you have and what branch you are on, type `git branch` into the terminal and press enter. This will print a list of the local branches you have and there will be a `*` next to the branch you have checked out.

![](/static/team/worksheets/branch.PNG)

To checkout the worksheet branch, type `git checkout worksheet` in terminal and press enter. If you don’t have the worksheet branch locally yet, enter `git checkout -b worksheet`.

![](/static/team/worksheets/checkout.PNG)

Whenever you begin making a worksheet make sure to pull the most recent changes from both the master branch AND the worksheet branch with `git pull origin master` and `git pull origin worksheet`. Our worksheet files are under `site > resources > practice` and named like so:

> quiz0-worksheet.md, quiz1-worksheet.md, etc.

Create a new markdown file for the practice worksheet associated with the upcoming quiz and name it accordingly. At the top of this file, give it a title, author(s) and page, which will be the last subdirectory of the URL.

![](/static/team/worksheets/header.PNG)

Once the worksheet is done, we want the new markdown file to be merged to master, so it will appear on the website. First, stash your changes by adding them to the staging area and making a commit. Do this with two commands: `git add .` and `git commit -m “Your commit message here”`. Then, push with `git push origin worksheet`. Check <https://github.com/comp110/team110/tree/worksheet> to make sure the last commit was pushed. Lastly, let Kris know that the worksheet is ready to be reviewed and merged with the master branch.

> Contributors: Megan Zhang, Jasper Christie 
