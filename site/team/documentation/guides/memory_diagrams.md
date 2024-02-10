---
title: Making Memory Diagrams 
date: 2021-02-25
author:
  - Vrinda Desai
  - Alyssa Lytle
page: logistics
template: overview
site-branch: team
---

# Making Memory Diagrams

Team 110, please refer to the following instructions for creating memory diagrams. Once a memory diagram or practice problem is fully reviewed, it will be posted on the 110 website for student-use. Refer to the #content-design Slack channel to see which topics to focus on every few weeks. 

# Creating A Diagram

If you are creating a memory diagram, you are free to do anything as long as it fulfills the [topic categories](/resources/practice/MemDiagrams.md) we are in need of and is within the scope of this course. Before you create a new memory diagram, check for notes on your previously submitted diagrams.



When submitting your diagram for peer-review, complete the following:

## Create a Page for Your Snippet

Every memory diagram page should have a code snippet, a solution image, and an [image description](/team/documentation/guides/image_descriptions.html). *(Save the raw copy of your solution in case you need to make edits!)*


Save the file with your solution image in the folder: `/site/static/team/diagrams/`

Create a new file in the folder "site/team/projects/diagrams/" and give it a name fitting for the example followed by `.md`. (For example, if my example was a class making baseball cards, I might name it `baseball.md`.)

Next, copy paste the text from "templates.md", which is already in the "diagrams" folder. You'll see where to add your code, solution image, and image description.

Back on the [Memory Diagram Table](https://docs.google.com/spreadsheets/d/1O5yaFVEdeX7CQDvhyLis0WJG6_i8piesP23BrgvNpC0/edit?usp=sharing), fill out the information for your diagram and mark the STATUS as “In Proposal.” Under MATERIALS you will put the url to your new page. (For example, the url for the baseball example would be <https://comp110-24s.github.io/team/projects/diagrams/baseball.html>. *NOTE THAT IT'LL RENDER AS .HTML, NOT .MD!*)


## Follow Through

After your proposed diagram has been reviewed, complete the following:
If the STATUS is “Ready to Post,” great job! No other work is required on your part.
If the STATUS is “Edits Needed,” go ahead and check out the NOTES section. Make prescribed changes and reupload all materials as if they are a new diagram following the steps above. This means you will upload two new files to the folder and you will be filling out a new row in the spreadsheet. Wait for your diagram to be reviewed again.

# Reviewing A Diagram

There are two types of reviews you can do for memory diagrams: adding a solution for an existing snippet or review an existing solution. 

# Adding A Solution

Follow these steps for any entry on the table marked "needs solution". 

View the page by clicking on the url, but also find the page in the site repo under "site/team/projects/diagrams". (There may be an existing image description commented out!)

Write a solution to code snippet and add an image description following [the image description guidelines](/team/documentation/guides/image_descriptions.html).

Save your solution as a .JPG or .PNG file in the site repo inside the folder site/static/team/diagrams/. Add the image to the page along with the image description using the following syntax:

~~~
# Solution

<img class="img-fluid" src="/static/team/diagrams/<solution-file-name>"/>

*Image Description:*

<Image description goes here.>
~~~

Finish up by [creating a pull request](#creating-a-pull-request) and changing the entry status to "Needs Review".

# Reviewing A Solution

Use this process to review any entry on the table marked "Needs Review".

If you are reviewing a memory diagram snippet with an existing solution, you should still write out your own solution. Compare your solution to the solution provided. Check for correctness as well as the proper format described in Creating a Diagram. *This includes checking the following Image Description and making sure that it matches a correct solution!* 

Provide any corrections in the NOTES section and mark the STATUS as “Edits Needed.” 
If everything looks good, mark the STATUS as “Ready to Post.”

*For speedy communication, please message the diagram-creator to let them know if you have corrections!*

# Creating A Pull Request

First, make sure you've set up the course repository by following the [course site setup](/team/documentation/guides/course_site_setup.html) guide.

You can then add your changes to the site via a *pull request*!

## Branch!

1. Make sure you're on the main branch (`git checkout main`) and run the command `git pull origin main` to get the latest updates.
2. Checkout a new `git` branch. In your terminal run the following command, replacing ONYEN with your onyen:
   `git checkout -b ONYEN-mem-diagram`


## Commit and Push!

1. To commit your changes, first add the files you've changed to the staging area:
   You can use `git add .` to add every single change file at once.
   Then commit your changes:
   `git commit -m "a description of what changes you made on the site"`
1. Push your work to your training branch on the staff repo (`git push origin [your-branch-name]`). Check your branch with `git branch`.

## Create a Pull Request! 

1. Open GitHub Pull Requests on the `comp110` repo: <https://github.com/comp110-lytle/comp110/pulls>
1. You might see a yellow notification box: "Your recently pushed branches...". If so select "Compare & Pull Request". If not, select "New Pull Request", and in the Compare branch drop-down select your branch.
1. Scroll through the differences and confirm your latest changes were successfully pushed. If you don't see them, check that you committed everything you expected and pushed to your branch. Select "Create Pull Request".
1. In the description box, briefly describe your branch.
1. On the right-hand sidebar, select Alyssa or [the web lead](/team/documentation/leads/website.md) as a reviewer.
1. Create pull request!