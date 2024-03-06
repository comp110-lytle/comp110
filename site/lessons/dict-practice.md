---
title: In-Class Coding Activity
author:
- Alyssa Lytle
page: lessons
template: overview
---

# In Class Coding Activity

This is an example mini-exercise that we will go through together in class to get a little more practice with function writing! *(You do not have to write these functions on your own!)*

## Part 0. Setup

Start by opening your workspace in Visual Studio. Right click on the "lessons" folder and select "add folder". Create a folder called "garden". Then, right click on the "garden folder and select "add file". Your file will be named `garden_helpers.py`.

Set up your document by adding the docstring:
`"""Some functions for my garden plan!"""` and initializing the `__author__` variable with your PID.


## Part 1. `add_by_kind()`

We are going to write a function that adds a plant to a garden dictionary that is sorted by the kind of plant. For example, given the dictionary `{"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}`, say we want to add another `"flower"`, like a daisy. This function should allow us to do that by *mutating* the input dictionary.

- Function name: `add_by_kind`
- Parameters: `dict[str, list[str]]`, `str`, `str`
- Return Type: `None`

Example usage:

<pre>
<div class="terminal">python
>>> from lessons.garden_helpers import add_by_kind
>>> by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
>>> add_by_kind(by_kind, "flower", "daisy")
>>> by_kind
{'flower': ['marigold', 'zinnia', 'daisy'], 'vegetable': ['carrots']}
>>> add_by_kind(by_kind, "fruit", "elderberry")
>>> by_kind
{'flower': ['marigold', 'zinnia', 'daisy'], 'vegetable': ['carrots'], 'fruit': ['elderberry']}
</div>
</pre>

## Part 2. `add_by_date()`

We are going to write a function that adds a plant to a garden dictionary that is sorted by the date in which the seeds should be sown. For example, given the dictionary ``, say we want to add another `"flower"`, like a daisy. This function should allow us to do that by *mutating* the input dictionary.

- Function name: `add_by_kind`
- Parameters: `dict[str, list[str]]`, `str`, `str`
- Return Type: `None`

Example usage:

<pre>
<div class="terminal">python
>>> from lessons.garden_helpers import add_by_date
>>> by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"]}
>>> add_by_date(by_date, "April", "daisy")
>>> by_date
{'April': ['marigold', 'daisy'], 'June': ['carrots']}
>>> add_by_date(by_date, "May", "elderberry")
>>> by_date
{'April': ['marigold', 'daisy'], 'June': ['carrots'], 'May': ['elderberry']}
</div>
</pre>

## Part 3. `lookup_by_kind_and_date()`

Finally, we are going to write a function that searches through both dictionaries and returns a list of what plants of a certain kind to plant at a certain date.

- Function name: `lookup_by_kind_and_date`
- Parameters: `dict[str, list[str]]`, `dict[str, list[str]]`, `str`, `str`
- Return Type: `str`

Example usage:

<pre>
<div class="terminal">python
>>> from lessons.garden_helpers import add_by_date
>>> by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
>>> by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"]}
>>> lookup_by_kind_and_date(by_kind, by_date, "flower", "April")
"flowers to plant in April: ['marigold']"
>>> lookup_by_kind_and_date(by_kind, by_date, "flower", "June")
'No flowers to plant in June.'
</div>
</pre>

