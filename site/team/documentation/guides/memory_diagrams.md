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

If you are creating a memory diagram, you are free to do anything as long as it fulfills the topics/problem categories we are in need of and is within the scope of this course. Before you create a new memory diagram, check for notes on your previously submitted diagrams.

Check that your solution adheres to the following criteria:
When updating variables, cross out old values rather than erasing/removing them. 
Include counter variables for any for-loops.
Save the raw copy of your solution in case you need to make edits!

When submitting your diagram for peer-review, complete the following:
Place your code, solution, and your image description into one markdown file (.md file). Feel free to use this Markdown Template for your materials.
You can enter in-line code into a markdown file, by simply putting backticks (`) around your code snippet. The solution will be inserted as an in-line image. 
Just below the solution, include your sample image description as plaintext. Review Sample Image Description for an example of how to write a description of a memory diagram. 
Upload this file into the Memory Diagrams Folder. 
Name the file with your ONEYEN, then an underscore, then “materials,” another underscore, and finally some sort of counter. For example, vrinda_materials_1.py would be the name of my first code snippet. This arbitrary counter can represent the number of diagrams you’ve progressively added, but mainly differentiates your files.
Paste the respective link to your materials under the MATERIALS columns in the spreadsheet.
Include your full name under NAME and mark the STATUS as “In Proposal.”

## Follow Through

After your proposed diagram has been reviewed, complete the following:
If the STATUS is “Ready to Post,” great job! No other work is required on your part.
If the STATUS is “Edits Needed,” go ahead and check out the NOTES section. Make prescribed changes and reupload all materials as if they are a new diagram following the steps above. This means you will upload two new files to the folder and you will be filling out a new row in the spreadsheet. Wait for your diagram to be reviewed again.

# Reviewing A Diagram

There are two types of reviews you can do for memory diagrams: adding a solution for an existing diagram or review an existing solution. 

# Adding A Solution

Follow these steps for any entry on the table marked "needs solution". 

View the page by clicking on the url, but also find the page in the site repo under "site/team/projects/diagrams". (There may be an existing image description commented out!)

Write a solution to code snippet and add an image description following [the image description guidelines](/site/team/documentation/guides/image_descriptions.html).

Save your solution as a .JPG or .PNG file in the site repo inside the folder site/static/team/diagrams/. Add the image to the page along with the image description using the following syntax:

~~~
# Solution

<img class="img-fluid" src="/static/team/diagrams/<solution-file-name>"/>

*Image Description:*

<Image description goes here.>
~~~

Finish up by [creating a pull request](#creating-a-pull-request).

# Reviewing A Solution

Use this process to review any entry on the table marked "needs review".

If you are reviewing a memory diagram snippet with an existing solution, you should still write out your own solution. Compare your solution to the solution provided. Check for correctness as well as the proper format described in Creating a Diagram. *This includes checking the following Image Description and making sure that it matches a correct solution!* 

Provide any corrections in the NOTES section and mark the STATUS as “Edits Needed.” 
If everything looks good, mark the STATUS as “Ready to Post.”

*For speedy communication, please message the diagram-creator to let them know if you have corrections!*

# Creating A Pull Request

You can push your changes to the site.