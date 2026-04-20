---
title: EX09 - Data Analysis for Continuous Improvement
author:
- Kris Jordan
- Kaki Ryan
- Izzy Ford
- Benjamin Eldridge
- Izzi Hinks
- Alyssa Lytle
page: projects
template: overview
---



Courses such as COMP110, just like organizations, services, and products, can be improved through intentional iteration on their design in order to _create more value_ for its stakeholders. This practice is generally known as _continuous improvement_. 

What is _creating value_? This idea can manifest in many ways, such as: serving unmet needs, reframing problems as opportunities, identifying authentic demand, testing novel ideas, leveraging underutilized resources, extending existing solutions, and so on. 

In a course, the stakeholders are typically:

1. Students Enrolled
2. Instructional Staff
3. Academic Institution
4. Societal Workforce

In this open-ended exercise, you will explore the data that we have collected via the anonymized course survey submitted by you and your peers earlier in the semester by creating data utility functions that can analyze . Then, you will reflect on your personal experiences and observations in COMP110 and brainstorm modifications to the course that _create value_ beyond its current design.

From your brainstormed ideas, you will consider them in the context of the anonymized course survey data submitted by you and your peers earlier in the semester. You will identify which one of your ideas _does not_ or is _least likely_ to have data to support or refute your idea and suggest how we might collect that data in the future. Then you will identify which one of your ideas _does have_ data to analyze and carry out an analysis of your most promising idea.

You will then perform an analysis of the data to explore the degree to which the data supports your idea. It is OK and expected that many ideas will not have conclusive support in the data and may even be rejected by the data. This is OK!

For this analysis, you will be using a Python package called `seaborn` to create graphs or visualizations that relate to your analysis. After you have written your analysis and drawn a conclusion based on whether your analysis supported your idea, you will present your analysis, visualizations, and conclusion via a live website!

Your project will need to satisfy many specifications, so before you begin programming be sure to read this project's write-up and the provided template notebook in full.

## Rubric

Part 0. Data Utilities (40pts)

* `head` -- 10 Points Autograded
* `select` -- 10 Points Autograded
* `concat` -- 10 Points Autograded
* `count` -- 10 Points Autograded

Part 1. Creative Ideation (15pts)

* Good - 5 pts - One brainstormed idea identifies value created for a specific stakeholder group.
* Better - 10 pts - Three brainstormed ideas which each identify value created for a specific stakeholder group.
* Best - 15 pts - Five brainstormed ideas which each identify value created for a specific stakeholder group.

Part 1.1. Identifying Missing Data (10pts)

* Good - 5 pts - Identifies an idea that does not have applicable data to support or is unlikely to have enough data to support.
* Better - 10 pts - Additionally is able to suggest a plausible and realistic way to collect data to support the idea in the future.

Part 1.2. Choosing Your Analysis (10pts)

* Good - 5 pts - Chooses an idea that has data from the survey which could be analyzed in support of it.
* Better - 10 pts - Articulates reason for choosing this idea to analyze over others based on its potential to create value.

Part 1.3. Analysis (60pts) - Each rubric item is independent of the others.

* 5pts - Each code cell in your analysis is preceded by a markdown cell explaining what you are attempting to do. Walk us through your thought process.
* 5pts - The code cells are executed and the notebook has saved outputs of code cells submitted.
* 5pts - Make use of `read_csv_rows` function
* 5pts - Make use of `head` function 
* 5pts - Make use of `columnar` function
* 5pts - Make use of `select` function
* 5pts - Make use of `count` function
* 5pts - Define, import, and use at least one helper function of your own design. One idea is a function that filters some data based on some criteria. For example, all values in a column that are greater than some threshold.
* 5pts - Carries out a logical analysis given the stated idea being analyzed.
* 15pts - Produce at least three charts or visualizations of the relevant data being analyzed using `seaborn`, at least one of which is not a `scatterplot` or `lineplot`.

Part 1.4. Conclusion (15pts)

* Good - 5 pts - Summarizes findings of analysis and the degree to which it supports, refutes, or is inconclusive regarding the idea put forth.
* Better - 10 pts - Puts forth potential costs, downsides, or trade-offs of adopting the idea.
* Best - 15 pts - Identifies extensions or refinements to this idea to consider as future work.

Part 2. Presenting Your Results (30pts)

* 10 pts - Your website's project page includes a summary of the analysis you performed in your notebook.
* 10 pts - At least three charts or visualizations are incorporated into the analysis and displayed on your website's project page.
* 10 pts - Your website's project page includes your final conclusions from your notebook.

These are just the baseline requirements. In order to completely analyze the idea you choose to explore, more intermediate steps may be necessary! 

## Getting Started

You will get the data needed by "pulling" from the course workspace repository. 

### Pushing
Before You Pull, you want to make sure you've saved all of your recent work! You do this by _pushing_ it to Github!

1. Open the Source Control panel (Command Palette: "Show Source Control" or click the icon with three circles and lines on the activity panel).
2. Notice the files listed under Changes. These are files you've made modifications to since your last backup.
3. Move your mouse's cursor over the word _Changes_ and notice the + symbol that appears. Click that plus symbol to add all changes to the next backup. You will now see the files listed under "Staged Changes".
   - If you do not want to backup _all_ changed files, you can select them individually. For this course you're encouraged to back everything up.
4. In the Message box, give a brief description of what you've changed and are backing up. This will help you find a specific backup (called a "commit") if needed. In this case a message such as, "Finished Exercise 00!" will suffice.
5. Press the Commit button to make a _Commit_ (a version) of your work.
6. In the Terminal, type the command `git push`. If your terminal was closed, go to the Terminal menu and select "New Terminal". This command "pushed" your changes to your backup repository on GitHub.



### Pulling

Now, you can _pull_ the files added by your instructors!

Be sure you are in your course workspace. Open the file explorer and you should see your work for the course. If you do not, open your course workspace through File > Open Recent.

1. Open the _Source Control View_ by clicking the 3-node (circles) graph (connected by lines) icon in your sidebar or opening the command palatte and searching for _Source Control_.
2. Click the Ellipses in the Source Control pane and select "Pull, Push" from the drop-down menu, then select "Pull from..." A box will appear and you should select either "origin" or "upstream", but not "backup". This will begin the pulling process from the course repository. It should silently succeed.
3. Return to the File Explorer pane and open the `data` directory. You should see it now contains the csv file with the survey results called `survey.csv`. 
4. In your workspace's `exercises` directory, you will see a folder named `ex09`. Inside that folder, there is a file named `analysis.ipynb` for this assignment. 
5. Additionally, there will be another file in `ex09` called `data_utils.py`. Copy your functions from the lesson on data into this file!

`data_utils.py` is where you will define the functions you create in part 0, and `analysis.ipynb` is the notebook file that will contain the majority of the instructions for this assignment and will also be where you write your analysis. Once you are done reading this write-up, go read all of `analysis.ipynb` *before* starting to program!

### Troubleshooting
If you're having trouble pulling:

* Make sure you PUSHED all of your changes to backup first!!!
* In your terminal, type `git config pull.rebase false`
* In your Visual Studio command center, select `Pull From...` -> `Upstream` -> `Upstream/Head`. (If not an option, do `Origin` -> `Main`.) 

If you're still having issues, come to office hours!


## Tour of the Data

`row` -- Row number. Unique for each row of the CSV.

`year` -- Expected graduation year. Possible values: 26, 27, 28, 29, 30, None (Note: This is clearly a non-exhaustive list. Just simplified for the sake of the project)

`unc_status` -- UNC status. Possible values: Freshman, Sophomore, Junior, Senior, Graduate, None

`transfer` -- Transfer student or not a transfer student. Possible values: Yes, No

`comp_major` -- Intention to major in CS. Possible values: Yes - BS, Yes - BA, Yes - Minor, No

`primary_major` -- Primary Major. Possible values: Advertising and PR, Applied Sciences, Asian Studies, Biology, Biomedical Engineering, Biostatistics, Business, Chemistry, Clinical Lab Science, Communication, Communications, Computer Science, Cultural Anthropology, Data Science, Dramatic Art, Earth Science, Economics, English, Environmental Science/Studies, Environmental Health Sciences, Exercise and Sports Science, Geology, Global Studies, HPM, Human Development and Family Science, Information Science, Interdisciplinary Studies, Linguistics, Management and Society, Mathematics, Media and Journalism, Medical Anthropology, Music Performance, Neuroscience, Nursing, Nutrition, Peace, War, and Defense, Philosophy, Physics, Political Science, Psychology, Public Policy, Radiology, Sociology, Sports Administration, Statistics and Analytics, Studio Art, Undecided

`prereqs` -- Prerequisites satisfied. Possible values are **any combination** of the following: MATH 129P, MATH 130, MATH 152, MATH 210, MATH 231, MATH 232, MATH 233, MATH 347, MATH 381, PHIL 155, PSYC 210, PSYC 215, STOR 112, STOR 113, STOR 120, STOR 151, STOR 155

`prior_exp` -- Prior experience. Possible values: None to less than one month!, 2-6 months, 7-12 months, 1-2 years, Over 2 years

`ap_principles` -- Completed AP Computer Science Principles. Possible values: Yes, No

`ap_a` -- Completed AP Computer Science A. Possible values: Yes, No

`other_comp` -- Completed a different, formal programming class. Possible values: UNC, Another college or community college, High school course (IB or other), On-line course, Other, None

`prior_time` -- Amount of time spent self-directed programming learning. Possible values: None to less than one month!, 1 month or so, 2-6 months, 7-12 months, 1-2 years, > 2 years

`languages` -- Programming languages student can identify by reading w/o reference material. Possible values are **any combination** of the following: Python, Java / C#, C / C++, JavaScript / TypeScript, Go, LISP / Scheme / Racket, Haskell, R / Matlab / SAS, BASIC, HTML / CSS, SQL, Bash, Other

`hours_online_social` -- Number of hours a day spent interacting with digital technology for personal uses (e.g. social media, entertainment, personal communication)? Possible values: None, 0 to 2 hours, 3 to 5 hours, 5 to 10 hours, 10+ hours.

`hours_online_work` --  Number of hours a day spent interacting with digital technology for work/school uses. Possible values: None, 0 to 2 hours, 3 to 5 hours, 5 to 10 hours, 10+ hours.

`tech_best_interests` -- "The technologies I use in my daily life have my personal best interests prioritized first and foremost." Possible values _(1 being Strongly Disagree and 7 being Strongly Agree)_: 1, 2, 3, 4, 5, 6, 7

`apps_accessible` -- "The apps and social media platforms I interact with are accessible to everyone." Possible values _(1 being Strongly Disagree and 7 being Strongly Agree)_: 1, 2, 3, 4, 5, 6, 7

`identity_my_interaction` -- "My personal identity (race/gender/sexuality/etc) impacts how I interact with technology." Possible values _(1 being Strongly Disagree and 7 being Strongly Agree)_: 1, 2, 3, 4, 5, 6, 7

`id_interact_with_me` -- "My personal identity (race/gender/sexuality/etc) impacts how technology interacts with me." Possible values _(1 being Strongly Disagree and 7 being Strongly Agree)_: 1, 2, 3, 4, 5, 6, 7

`interested_connections` -- "I am interested in the connections between computer science and other fields." Possible values _(1 being Strongly Disagree and 7 being Strongly Agree)_: 1, 2, 3, 4, 5, 6, 7

`social_issues` -- "Social issues are relevant to computer scientists and software engineers." Possible values _(1 being Strongly Disagree and 7 being Strongly Agree)_: 1, 2, 3, 4, 5, 6, 7

`research_biases` -- "Scientific research is influenced by individual and/or societal biases."" Possible values _(1 being Strongly Disagree and 7 being Strongly Agree)_: 1, 2, 3, 4, 5, 6, 7

`researchers_unbiased` -- "I believe scientific researchers can be unbiased." Possible values _(1 being Strongly Disagree and 7 being Strongly Agree)_: 1, 2, 3, 4, 5, 6, 7

`empirical_data` -- "Empirical data can always be trusted." Possible values _(1 being Strongly Disagree and 7 being Strongly Agree)_: 1, 2, 3, 4, 5, 6, 7

`cs_objective` -- "Computer science is an objective science." Possible values _(1 being Strongly Disagree and 7 being Strongly Agree)_: 1, 2, 3, 4, 5, 6, 7

`algorithms_objective` -- "Computer programs and algorithms are more objective than humans." Possible values _(1 being Strongly Disagree and 7 being Strongly Agree)_: 1, 2, 3, 4, 5, 6, 7

`tech_impact` -- "Computing technologies positively impact our society." Possible values _(1 being Strongly Disagree and 7 being Strongly Agree)_: 1, 2, 3, 4, 5, 6, 7

`pre_lecture_videos` -- Student believes that optional pre-lecture videos that prepare students for the content of each lecture would be helpful for their learning. Possible values _(1 being Strongly Disagree and 7 being Strongly Agree)_: 1, 2, 3, 4, 5, 6, 7

`add_livestream` -- Moving forward in the semester, student believes in-person lectures should be live streamed so that not everyone is required to attend in-person. Possible values _(1 being Strongly Disagree and 7 being Strongly Agree)_: 1, 2, 3, 4, 5, 6, 7

`own_notes` -- Student keeps own notes for topics covered in lecture.  Possible values _(1 being Never and 7 being Always)_: 1, 2, 3, 4, 5, 6, 7

`own_examples` -- When uncertain of how a concept works, student tries to come up with own examples in code. Possible values _(1 being Never and 7 being Always)_: 1, 2, 3, 4, 5, 6, 7

`oh_visits` -- On average, for a single programming exercise or project in this course, student typically needs to seek help in office hours about this many times. Possible values _(0 being Zero and 5 being Five or More)_: 0, 1, 2, 3, 4, 5

`ls_effective` -- Lesson videos are effective in helping student learn the topics of the course. Possible values _(1 being Strongly Disagree and 7 being Strongly Agree)_: 1, 2, 3, 4, 5, 6, 7

`lsqs_effective` -- Post-lesson questions on Gradescope are effective in helping student learn the topics of the course. Possible values _(1 being Strongly Disagree and 7 being Strongly Agree)_: 1, 2, 3, 4, 5, 6, 7

`programming_effective` -- Programming assignments are effective in helping student learn the topics of the course. Possible values _(1 being Strongly Disagree and 7 being Strongly Agree)_: 1, 2, 3, 4, 5, 6, 7

`qz_effective` -- Preparing for quizzes is effective in helping student learn the topics of the course. Possible values _(1 being Strongly Disagree and 7 being Strongly Agree)_: 1, 2, 3, 4, 5, 6, 7

`oh_effective` -- Office hours 1:1 appointments are effective in helping student learn the topics of the course. Possible values _(1 being Strongly Disagree and 7 being Strongly Agree, Empty string if student has not attended OH)_: 1, 2, 3, 4, 5, 6, 7, ""

`tutoring_effective` -- Tutoring is effective in helping student learn the topics of the course. Possible values _(1 being Strongly Disagree and 7 being Strongly Agree, Empty string if student has not attended tutoring)_: 1, 2, 3, 4, 5, 6, 7, ""

`pace` -- Student finds the pace of COMP110 to be moving... Possible values _(1 being Very Slowly and 7 being Very Quickly)_: 1, 2, 3, 4, 5, 6, 7

`difficulty` -- Student is finding COMP110 to be... Possible values _(1 being Very Easy and 7 being Very Difficult)_: 1, 2, 3, 4, 5, 6, 7

`understanding` -- So far, student is feeling like they typically... Possible values _(1 being Are Lost and 7 being Understand Everything)_: 1, 2, 3, 4, 5, 6, 7

`interesting` -- Student believes the topics they are learning in this course are intellectually interesting. Possible values _(1 being Strongly Disagree and 7 being Strongly Agree)_: 1, 2, 3, 4, 5, 6, 7

`valuable` -- Student believes the skills they are learning in this course will be valuable to them in the future. Possible values _(1 being Strongly Disagree and 7 being Strongly Agree)_: 1, 2, 3, 4, 5, 6, 7

`would_recommend` -- Student would recommend this course to other students in the Fall. Possible values _(1 being Strongly Disagree and 7 being Strongly Agree)_: 1, 2, 3, 4, 5, 6, 7

## Some notes before you begin

* Some of the survey questions were optional, so there will not be a data value for every column in every row. This is expected. Instead the value will just be the empty `str` or `""`.
* When you read in the CSV as a `list[dict[str, str]]` with your `read_csv_rows` function, every value is interpreted as a `str`, including numerical ones! Analysis on columns that include Likert data (ratings 1-7), for example, will need to be converted to a numeric type for numeric analysis.

## Submission Instructions

Save your notebook!

One group member should log in to Gradescope and select the assignment named "EX09 - Data Project". You'll see an area to upload a zip file. To produce a zip file for autograding, return back to Visual Studio Code.

If you _do not_ see a Terminal at the bottom of your screen, open the Command Palette and search for "View: Toggle Integrated Terminal".

To produce a zip file for `ex09`, type the following command (all on a single line):

`python -m tools.submission exercises/ex09`

<!-- If you right click on this file and select "Reveal in File Explorer" on Windows or "Reveal in Finder" on Mac, the zip file's location on your computer will open. Upload this file to Gradescope to submit your work for this exercise. -->

In the file explorer pane, look to find the zip file named "yy.mm.dd-hh.mm-exercises-ex09.zip". The "mm", "dd", and so on, are timestamps with the current year, month, day, hour, minute. 

After you submit the zip file and you are satisfied with your submission, make sure to add your partner to the submission by clicking on "View or edit group" near where your name is, searching for your partner's name/PID, and then click on their name to add them. **Important**: One partner will *make* a submission but both partners will be added to a submission, and the non-submitting partner **should double-check this** on their own Gradescope!

Don't forget to backup your work by creating a commit and pushing it to GitHub. For a reminder of this process, see the previous exercises.

Some of the points for this project will be handgraded, so your autograder score will not be the same as your final score for this exercise. Refer to the rubric above for which parts are autograded and which are handgraded.