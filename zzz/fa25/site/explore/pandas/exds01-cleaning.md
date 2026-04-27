---
title: Data cleaning
author:
- Jesse Wei
- Kyle Sorensen
page: explore
template: overview
---
## Introduction
This is an exercise about how to clean data using the Python library `pandas`! Data cleaning is vitally important - you can have great skill in manipulating data, but you won't get any good results unless the data you're working with is in a suitable form. You will [NEED TO VISIT THIS LINK](https://github.com/comp110sidequest/downloads/blob/main/exds_01_tutorial.ipynb) to learn about data cleaning in `pandas`. This is a tutorial notebook file meant to show you function and syntax for data cleaning. If you're uncomfortable with `pandas` itself, check out the `pandas` tutorial and exercise on the Explore tab of the course website.  

If you run into trouble, please email Jesse (jessew13@email.unc.edu) and Kyle (kjs20@email.unc.edu)!

### Task 0:
Import `pandas` and `numpy`.
Download this [file](https://github.com/comp110sidequest/downloads/blob/main/AB_NYC_2019_shuffled.csv) and save it to the data directory.
Save the path of the file as a named constant.
Using `read_csv`, read the csv file into a pandas `DataFrame`.
Use the `head` function to get an idea of the data (you can also open up the file with Excel).

### Task 1:
Check that the "id" values are all unique first, and let those values index the `DataFrame`.
Set the optional `inplace` parameter to `True` to cause the changes to be made directly to the `DataFrame`.
Use `head` to check that the `DataFrame` is now indexed by "id".

### Task 2: 
Assume there is no use for the `indices_to_drop`, `latitude`, and `longitude` columns - drop them (set the `inplace` optional parameter to True).
How can you check that you succeeded?

### Task 3:
Notice that we have now indexed the `DataFrame` by the numbers in the id column, but they're out of order. Look up how to sort the rows of a pandas DataFrame by a column and do so (remember to apply changes inplace).
Try to find a suitable website yourself, as it's a VERY valuable skill to have, but if you need help finding a good website, you can [click here](https://pythonexamples.org/pandas-dataframe-sort-by-column/)

### SOS - the resident with ticket id 22209583 has reported a gas leak in their room.

### Task 4: 
Print all the information associated with ticket id `22209583`.
Print out only the `host_name`.
Use position-based indexing to find the same information.

### Task 5: regex
Extract the rows with `host_name` values starting only with the letter J. Use [this cheat sheet](https://www.debuggex.com/cheatsheet/regex/python) for some useful regex expressions! You will probably also need to Google how to use regex in pandas and Python.
Then apply `.dropna` (remember to set `inplace` to `True`) to the dataset.
Check your work!
