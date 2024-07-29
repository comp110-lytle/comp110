---
title: Challenge Question 
author:
- Alyssa Byrnes
page: lessons
template: overview
---

## Reformatting Data

As dicussed in class, you will be writing a function called `columnar` in `lessons/data_practice/data_utils.py` that takes a variable in the following form:

```
  d: list[dict[str,str]] = [{'Day': 'Monday', 'Low': '56', 'High': '75'}, {'Day': 'Tuesday', 'Low': '53', 'High': '72'}, {'Day': 'Wednesday', 'Low': '50', 'High': '72'}]
```

and converts it to the form:

```
{'Day': ['Monday', 'Tuesday', 'Wednesday'], 'Low': ['56', '53', '50'], 'High': ['75', '72', '72']}
```

## Hints:

### 1. Write the function to just return a dict with keys and empty lists:

In other words, for input:

```
  d: list[dict[str,str]] = [{'Day': 'Monday', 'Low': '56', 'High': '75'}, {'Day': 'Tuesday', 'Low': '53', 'High': '72'}, {'Day': 'Wednesday', 'Low': '50', 'High': '72'}]
```

It'll return 

```
{'Day': [], 'Low': [], 'High': []}
```

### 2. Use the `column_vals` function:

Think about how you can call the column_vals function we defined in class to get the values you need for the lists.

## Submission

Create a .zip file by running the following command in your terminal:

```python -m tools.submission lessons/data_practice```

Then, drag and drop that .zip file into Gradescope!


## Bonus!

Now that you've written your columnar function, try adding the following cell to `csv_data.ipynb` to see a nice visualization of your data!

```
    from data_utils import columnar
    from tabulate import tabulate

    column_data: dict[str,list[str]] = columnar(data)
    tabulate(column_data, column_data.keys(), "html")
```