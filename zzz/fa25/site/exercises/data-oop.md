---
title: EX08 - Data Utility Methods
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

### Understanding the Exercise Files + Install Required Library

In your `ex08` directory, you should now have the following three files:

- `analyze_data.py`: this is where you are going to import and test your functions from `data_utils` and methods from `DataFrame`
- `data_utils.py`: this is where you will define some functions to read csv files and manipulate the imported data
- `DataFrame.py`: this is where you will create your DataFrame class and define methods to manipulate and analyze the DataFrame objects.

You'll notice these files already have some skeleton code in them. They provide an outline of what your code will look like, but it's your job to give them functionality! 

Additionally, you should see a `data` folder appear in your workspace with some .csv files! This is the data we are going to use in `analyze_data.py` to test your functions and methods! There are two datasets of popular baby names in New York from different year ranges.

#### Required Library

You'll need to use the `tabulate` library for visualizing data in this assignment. In order to install this library, paste the following command in your terminal:

<pre><div class="terminal">python -m pip install tabulate
</div>
</pre>

***IF YOU RESTART YOUR CONTAINER, YOU'LL HAVE TO RERUN THIS COMMAND!***

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

#### Test your function

In `analyze_data.py`, you'll see there two lines of code to test this function: 

```
columnar_early_data: dict[str, list[str]] = columnar(early_data)
```

```
columnar_later_data: dict[str, list[str]] = columnar(later_data)
```

Both `columnar_early_data` and `columnar_later_data` should be dictionaries with the keys ['year', 'gender', 'ethnicity', 'name', 'count'].

## Part 2: `DataFrame` Class

Now, you are going to add some functionality to the `DataFrame` class!

### 2.0 `__init__`

Your `DataFrames` class is only going to have one attribute: `data: dict[str, list[str]]`. The idea is that once you reformat your data using `columnar`, you'll be able to store it as the `data` attribute in a `DataFrame` object.

Define your `DataFrame` class, declare your `data` attribute, and write an `__init__` method that takes a `input_data: dict[str, list[str]]` as a parameter and initializes your `data` attribute to equal `input_data`.

#### Test your function

You can test your `DataFrame` class in the REPL with the following small example:

<pre><div class="terminal">/workspace (main*) » python                                                                         
>>> from exercises.ex08.DataFrame import DataFrame
>>> data: dict[str, list[str]] = {"first_name": ["alyssa", "izzi"], "last_name": ["lytle","hinks"]}
>>> df: DataFrame = DataFrame(data)
>>> df.data
{'first_name': ['alyssa', 'izzi'], 'last_name': ['lytle', 'hinks']}
</div>
</pre>

In `analyze_data.py`, you'll see there two lines of code to turn both sets of baby name data into `DataFrame`s: 

```
df_early: DataFrame = DataFrame(columnar_early_data)
```

```
df_later: DataFrame = DataFrame(columnar_later_data)
```

#### `tabulate`

You'll see in `DataFrame.py`, there is a method called `tabulate` that has already been written for you! It allows you to visualize your data as a table. In analyze_data.py, you'll see it called:

```
df_early.tabulate()
```

### 2.1 `__add__`

For this next method, we are going to give the plus `+` sign some functionality between two `DataFrame` objects. 

The main idea behind this method is the following: 

Given two `DataFrame`s with the same keys (aka column headers), concatenate them to create one large `DataFrame`.

* Method Name: `__add__`
* Parameter: `self` (which is a `DataFrame`) and an additional `DataFrame` object
* Return Type: `DataFrame`

You can test your `__add__` method in the REPL with the following small example:

<pre><div class="terminal">/workspace (main*) » python                                                                         
>>> from exercises.ex08.DataFrame import DataFrame
>>> data: dict[str, list[str]] = {"first_name": ["alyssa", "izzi"], "last_name": ["lytle","hinks"]}
>>> df: DataFrame = DataFrame(data)
>>> more_data:  dict[str, list[str]] = {"first_name": ["sophie"], "last_name": ["jiang"]}
>>> df2: DataFrame = DataFrame(more_data)
>>> big_frame: DataFrame = df + df2
>>> big_frame.tabulate()
+--------------+-------------+
| first_name   | last_name   |
+==============+=============+
| alyssa       | lytle       |
+--------------+-------------+
| izzi         | hinks       |
+--------------+-------------+
| sophie       | jiang       |
+--------------+-------------+
</div>
</pre>

In `analyze_data.py`, you'll see the `__add__` magic method is used: 

```
df: DataFrame = df_early + df_later
```

Try running `df.tabulate()` to visualize your new dataset! (Warning: it'll be a loooong output!)

### 2.2 `head`

Let's find a way to deal with these long outputs! Let's write a method that let's us look at a subset of the data! `head` should return a DataFrame with only the first `N` (a parameter) rows of data for each column.


* Method name: `head`
* Parameters: `self` and an `int` to represent the number of "rows" to include in the resulting `DataFrame`
* Return type: `Data Frame`

Implementation strategy: 

1. Establish an empty dictionary that will serve as the returned dictionary this function is building up. 
2. Loop through each of the columns in the first row of the table given as a parameter. 
    1. Inside of the loop, establish an empty list to store each of the first N values in the column. 
    2. Loop through the first N items of the table's column, 
        1. Appending each item to the previously list established in step 2.1. 
    3. Assign the produced list of column values to the dictionary established in step 1.
3. Use the dictionary to create a new `DataFrame` and return it!


#### Test your method


You can test your method in the REPL with the following small example:

<pre><div class="terminal">/workspace (main*) » python
>>> from exercises.ex08.DataFrame import DataFrame
>>> data: dict[str, list[str]] = {"first_name": ["alyssa", "izzi", "sophie", "viktorya"], "last_name": ["lytle","hink
s", "jiang", "hunanyan"]}
>>> df: DataFrame = DataFrame(data)
>>> df.tabulate()
+--------------+-------------+
| first_name   | last_name   |
+==============+=============+
| alyssa       | lytle       |
+--------------+-------------+
| izzi         | hinks       |
+--------------+-------------+
| sophie       | jiang       |
+--------------+-------------+
| viktorya     | hunanyan    |
+--------------+-------------+
>>> subset: DataFrame = df.head(2)
>>> subset.tabulate()
+--------------+-------------+
| first_name   | last_name   |
+==============+=============+
| alyssa       | lytle       |
+--------------+-------------+
| izzi         | hinks       |
+--------------+-------------+
</div></pre>

In `analyze_data.py`, you'll see the `head` method is used to get the first 10 entries of data.

```
first_ten: DataFrame = df.head(10)
```

Visualize the result using 

```
first_ten.tabulate()
```

### 2.3 `select`

Now, say we want to reason about a subset of the *columns* in our table. 

Many data tables will contain many columns that are not related to the analysis you are trying to perform. _Selecting_ only the columns you care about makes it easier to focus your attention on the problem at hand.

* Function Name: `select`
* Parameters:
    1. `self` - a `DataFrame`
    2. `list[str]` - the names of the columns to copy to the new, returned `DataFrame`
* Return type: `DataFrame`

Implementation strategy:

1. Establish an empty dictionary.
2. Loop through each of the columns _in the second parameter of the function_
    1. Assign to the column key of the result dictionary the list of values stored in the input dictionary at the same column
3. Use the dictionary to create a new `DataFrame` and return it!

#### Test your method

You can test your method in the REPL with the following small example:

<pre><div class="terminal">/workspace (main*) » python
>>> from exercises.ex08.DataFrame import DataFrame
>>> data: dict[str, list[str]] = {"first_name": ["alyssa", "izzi"], "last_name": ["lytle","hinks"], "title": ["Professor", "Professor"]}
>>> df: DataFrame = DataFrame(data)
>>> df.tabulate()
+--------------+-------------+-----------+
| first_name   | last_name   | title     |
+==============+=============+===========+
| alyssa       | lytle       | Professor |
+--------------+-------------+-----------+
| izzi         | hinks       | Professor |
+--------------+-------------+-----------+
>>> just_names: DataFrame = df.select(["first_name", "last_name"])
>>> just_names.tabulate()
+--------------+-------------+
| first_name   | last_name   |
+==============+=============+
| alyssa       | lytle       |
+--------------+-------------+
| izzi         | hinks       |
+--------------+-------------+
</div></pre>

In `analyze_data.py`, you'll see the `select` and `head` methods are used together to get just the `name` and `count` of the first 10 entries of data.

```
name_and_count: DataFrame = df.head(10).select(["name", "count"])
```

Visualize the result using 

```
name_and_count.tabulate()
```


### 2.4 `filter_by_col_value`

Now, say you want to filter out the data in your table so that you only have entries with specific values in a given column.

Now, say we want to reason about a subset of the *columns* in our table. 

Many data tables will contain many columns that are not related to the analysis you are trying to perform. _Selecting_ only the columns you care about makes it easier to focus your attention on the problem at hand.

* Function Name: `select`
* Parameters:
    1. `self` - a `DataFrame`
    2. `str` - the names of the column that has the value to filter
    3. `str` - the specific value that will be filtered out
* Return type: `DataFrame`

Implementation strategy:

*TODO*

#### Test your method


You can test your method in the REPL with the following small example:

<pre><div class="terminal">/workspace (main*) » python
>>> from exercises.ex08.DataFrame import DataFrame
>>> data: dict[str, list[str]] = {"first_name": ["alyssa", "izzi", "sophie", "viktorya"], "last_name": ["lytle","hinks", "jiang", "hunanyan"], "title" : ["Professor", "Professor", "TA", "TA"]}
>>> df: DataFrame = DataFrame(data)
>>> df.tabulate()
+--------------+-------------+-----------+
| first_name   | last_name   | title     |
+==============+=============+===========+
| alyssa       | lytle       | Professor |
+--------------+-------------+-----------+
| izzi         | hinks       | Professor |
+--------------+-------------+-----------+
| sophie       | jiang       | TA        |
+--------------+-------------+-----------+
| viktorya     | hunanyan    | TA        |
+--------------+-------------+-----------+
>>> TA_df: DataFrame = df.filter_by_col_value("title", "TA")
>>> TA_df.tabulate()
+--------------+-------------+---------+
| first_name   | last_name   | title   |
+==============+=============+=========+
| sophie       | jiang       | TA      |
+--------------+-------------+---------+
| viktorya     | hunanyan    | TA      |
+--------------+-------------+---------+
</div></pre>

In `analyze_data.py`, you'll see `filter_by_col_value` method is used to get just the names data of babies born in 2020.

```
names_2020: DataFrame = df.filter_by_col_value("year", "2020")
```

Visualize the result using 

```
names_2020.tabulate()
```

## Make a Backup Checkpoint "Commit"

As you make progress on this exercise, making backups is encouraged.

1. Open the Source Control panel (Command Palette: "Show SCM" or click the icon with three circles and lines on the activity panel).
2. Notice the files listed under Changes. These are files you've made modifications to since your last backup.
3. Move your mouse's cursor over the word _Changes_ and notice the + symbol that appears. Click that plus symbol to add all changes to the next backup. You will now see the files listed under "Staged Changes".
   - If you do not want to backup _all_ changed files, you can select them individually. For this course you're encouraged to back everything up.
4. In the Message box, give a brief description of what you've changed and are backing up. This will help you find a specific backup (called a "commit") if needed. In this case a message such as, "Progress on Exercise N" will suffice, where N is the current exercise.
5. Press the Check icon to make a _Commit_ (a version) of your work.
6. Finally, press the Ellipses icon (...), look for "Pull/Push" submenu, and select "Push to...", and in the dropdown select your backup repository.


## Submit to Gradescope for Grading

All that's left now is to hand-in your work on Gradescope for grading!

Type the following command (all on a single line):

`python -m tools.submission exercises/ex08`

In the file explorer pane, look to find the zip file named "yy.mm.dd-hh.mm-exercises-ex08.zip". The "yy", "mm", "dd", and so on, are timestamps with the current year, month, day, hour, minute. If you right click on this file and select "Reveal in File Explorer" on Windows or "Reveal in Finder" on Mac, the zip file's location on your computer will open. Upload this file to Gradescope to submit your work for this exercise.

