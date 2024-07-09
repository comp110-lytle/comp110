---
title: Pandas Exercise
author:
- Kyle Sorensen
page: explore
---

# exds_00: Getting Started (Exercise)

### Introduction:
Now that you are familiar with some of the basics of `pandas` and have learned a little bit about how to manipulate data in the form of `DataFrame`'s, it is time to put your skills to the test. At this point you should be familiar with the following:

* importing `pandas`
* creating a `DataFrame`, underlying structure
* reading from and writing to .csv files
* observing the structure of a specific `DataFrame`
* selecting data by column and by row
* some basic analysis using `numpy`

Additionally, if you have completed one of the recent projects, you will also be familiar with the `survey.csv` data, which details course evaluation responses from a previous semester. Below you will see some tasks, each with increasing difficulty, that test your newfound data science skills. You may complete this exercise in a new Jupyter Notebook file or in a normal Python file.


### Task 1:
As before, we have to get the data into a usable form for `pandas`. Load the `survey.csv` data into a `DataFrame` called `survey`.


### Task 2:
It is a best practice to gain an understanding of the sturcture of data before trying to conduct any sort of analysis. Use the `.info()` method to get a look at the "big picture" of your `DataFrame`.

### Task 3: 
Often, you will deal with data that has ambiguous variable naming conventions. While `survey.csv` is not one of those datasets, thankfully, it is still essential to understand what each column is trying to tell you about students! Look at the columns labeled `kaki_effective`, `interested`,  and `oh_visits` by themselves and describe what they represent below.

### Task 4:
At first glance, this seems to be quite a large dataset with many variables, so it may be helpful to only look at columns of interest. Create a new `DataFrame` called `survey_new` which contains only the columns `row_number`,`pace`,`difficulty`,`understanding`,`interested`,`valuable`,`grade`,and `would_recommend`. Note that there are many ways to do this, some MUCH more efficient than others. A potential use for this new data would be if we want a more streamlined look at whether perception of difficulty aligns with a student's grade.

### Task 5:
Perhaps something we are interested in is the difference in `difficulty` between first-year students and returning students. Subset the data such that only first-year students are included, and store this in a new `DataFrame` called `first_year`. Similarly, store returning students in a `DataFrame` called `returning`. Then, calculate the average grade and standard deviation using `numpy` for these two groups. Write a brief statement about these two quantities.

### Task 6: Statistics Challenge
An essential skill for any data scientist (or any professional that uses programming) is the ability to research new techniques and read documentation. 

In this _challenging_ task, we want to analyse the difference we saw above, but more rigorously! :)
 
Research hypothesis tests specifically for the difference of two means. Write a brief paragraph about your findings, especially detailing the t-distribution. Then look into the `scipy` `.ttest_ind()` method and [read the documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html). Write a brief statement about your findings. Finally, conduct the hypothesis test for the null hypothesis that the mean `difficulty` for first-years is equal to that for returning students. Report your findings!

