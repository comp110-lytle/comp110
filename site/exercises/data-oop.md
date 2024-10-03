---
title: EX09 - Data Utility Methods
author:
    - Alyssa Lytle
    - Kris Jordan
page: exercises
template: overview
---


For this exercise, you are going to get more practice writing classes while writing functions and methods to analyze some data!


## Part 0. Pull the skeleton code

You will find the starter files needed by "pulling" from the course workspace repository. Before beginning, be sure to:

0. Be sure you are in your course workspace. Open the file explorer and you should see your work for the course. If you do not, open your course workspace through File > Open Recent.
1. Open the _Source Control View_ by clicking the 3-node (circles) graph (connected by lines) icon in your sidebar or opening the command palatte and searching for _Source Control_.
2. Click the Ellipses in the Source Control pane and select "Pull" from the drop-down menu. This will begin the pulling process from the course repository. It should silently succeed.
3. Return to the File Explorer pane and open the `exercises` directory. You should see it now contains another directory named `ex08`. If you expand that directory, you should see the starter files for the code you'll be writing.
4. If you do not see the `ex08` directory, try once more but selecting `"Pull From"` and select `origin` in step 2.

### Understanding the Exercise files

In your `ex08` directory, you should now have the following three files:

- `analyze_data.py`: this is where you are going to import and test your functions from `data_utils` and methods from `DataFrame`
- `data_utils.py`: this is where you will define some functions to read csv files and manipulate the imported data
- `DataFrame.py`: this is where you will create your DataFrame class and define methods to manipulate and analyze the DataFrame objects.

You'll notice these files already have some skeleton code in them. They provide an outline of what your code will look like, but it's your job to give them functionality! 

Additionally, you should see a `data` folder appear in your workspace with some .csv files! This is the data we are going to use in `analyze_data.py` to test your functions and methods! There are two datasets of popular baby names in New York from different year ranges.

## Part 1: Data Utils

For this part, you're going to be working in `data_utils.py` to write some functions that will help you pull the data from the .csv files and prepare them to be made into `DataFrame`s!

### 1.0 `read_csv_rows`

Complete the implementation of the `read_csv_rows` function in `data_utils.py`.

Purpose: Read an entire CSV of data into a `list` of rows, each row represented as `dict[str, str]`.

* Function Name: `read_csv_rows`
* Parameter: 
    1. `str` path to CSV file
* Return Type: `list[dict[str, str]]` 

Implementation hint: refer back to the code you wrote in lecture for reading a CSV file. We give you the code for this function.

#### Test your function

In `analyze_data.py`, you'll see that there are two lines of code to import both data files:

```
early_data: list[dict[str, str]] = read_csv_rows("data/baby_names_2012_2017.csv")
```
```
later_data: list[dict[str, str]] = read_csv_rows("data/baby_names_2018_2021.csv")
```

To check that your function works, you can check the *length* of both `early_data` and `later_data`. 

`early_data` should have a length of 48041 and `later_data` should have a length of 21173. *(That's a lot of data!)*

### 1.1 `column_values`

Define and implement this function in `data_utils.py`.

Purpose: Produce a `list[str]` of all values in a single `column` whose name is the second parameter.

* Function Name: `column_values`
* Parameters: 
    1. `list[dict[str, str]]` - a list of rows representing a _table_
    2. `str` - the name of the column (key) whose values are being selected
* Return Type: `list[str]`

Implementation strategy: Establish an empty list to store your column values. Loop through every row in the first parameter. Append the value associated with the key ("column") given as the second parameter to your list of column values. After looping through every row, return the list of column values.

#### Test your function

In `analyze_data.py`, you'll see there is a line of code to test this function: 

```
names_early_data: list[str] = column_values(early_data, "name")
```

The length of `names_early_data` should be 48041.

### 1.2 `columnar`

Finally, you are going to reformat your data to get it ready to be made into a `DataFrame`!

Define and implement this function in `data_utils.py`.

Purpose: _Transform_ a table represented as a list of rows (e.g. `list[dict[str, str]]`) into one represented as a dictionary of columns (e.g. `dict[str, list[str]]`).

Why is this function useful? Many types of analysis are much easier to perform column-wise.

* Function Name: `columnar`
* Parameter: `list[dict[str, str]]` - a "table" organized as a list of rows
* Return Type: `dict[str, list[str]]` - a "table" organized as a dictionary of columns

Implementation strategy: Establish an empty dictionary to the your column-oriented table you are building up to ultimately return. Loop through each of the column names in the first row of the parameter. Get a list of each column's values via your `column_values` function defined previously. Then, associate the column name with the list of its values in the dictionary you established. After looping through every column name, return the dictionary.

### Test your function

In `analyze_data.py`, you'll see there two lines of code to test this function: 

```
columnar_early_data: dict[str, list[str]] = columnar(early_data)
```

```
columnar_later_data: dict[str, list[str]] = columnar(later_data)
```

Both `columnar_early_data` and `columnar_later_data` should be dictionaries with the keys ['year', 'gender', 'ethnicity', 'name', 'count'].

## Part 2: `DataFrames` Class

Now, you are going to add some functionality to the `DataFrames` class!

### 2.0 `__init__`

### 2.1 `__add__`

### 2.2 `head`

### 2.3 `select`

### 2.4 `filter_by_col_value`

### 2.5 `filter_by_rank`

## Part 3. Push to Backup

## Part 4. Submission