---
title: EX08 - Linked List Utils
author:
- Kris Jordan
- Kaki Ryan
page: exercises
---

## Overview

In these exercises you will implement a few algorithms to process a singly-linked list data structure. Just like in the `list` utility functions, these functions will be _pure_ and are well suited for writing test cases. As such, you will also write test cases demonstrating their usage and verifying their correctness.

## Setup

In the `exercises` directory, create a directory named `ex08`.

### `linked_list.py`

In the `ex08` directory, create a file named `linked_list.py` and establish the following starting contents:

~~~python
"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional

__author__ = "Your PID"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> int:
    """Returns the last value of a Linked List, or raises a ValueError if the list is empty."""
    if head is None:
        raise ValueError("last cannot be called with None")
    else:
        return None
~~~

There is some **magic** happening in the above code listing. The `__str__` magic method is used to produce string representations of objects. So if you create a Node object and print it, python will **automagically** call the `__str__` method and print out your custom string message. This will be super helpful when you are creating your own linked lists for testing.

For example, without a `__str__` method defined on our Node class, we would expect to see something like this:

~~~
>>> example_node = Node(3, Node(2, None))
<Node object at 0x7f959129e130>
~~~

But if we have the `__str__` method defined as above, we should get:

~~~
>>> example_node = Node(3, Node(2, None))
3 -> 2 -> None
~~~

Additionally, we have provided the `is_equal` function for testing if two linked lists are equivalent to each other. We will go over this function in class on Thursday, and you should make use of it when writing tests cases for all functions after max. 


### `linked_list_test.py`

Establish a file for your test definitions named `linked_list_test.py` with the following contents:

~~~python
"""Tests for linked list utils."""

import pytest
from exercises.ex08.linked_list import Node, last

__author__ = "Your PID"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3
~~~

As you can see, a skeleton definition of `last` and some simple tests for `last` are provided to help get you started. You will responsible for defining the other functions and writing their tests.

**In order to ask questions about a function in office hours, you must demonstrate example test(s) for it first. If you do not have tests for a function yet, we will only help you setup an example test or two and will ask you to come back for your original question after you have had time to try again.**

To run your tests, run `python -m pytest exercises/ex08/linked_list_test.py` in the terminal. This will be a more reliable way to test your functions than the testing/beaker tab in VSCode.

## Requirements

You must use recursive function calls to implement the functions below. If you use loops your work for that function will be disqualified.

## `last` -- 15 points

Given an `Optional[Node]` representing the `head` Node of a Linked List of any length, including empty, return the `data` of the last node in the list. If the list is empty, raise a `ValueError` as shown below. A skeleton definitition is provided with the correct function signature above and example of how to raise a `ValueError`.

## `value_at` -- 15 points

Given a `head` `Optional[Node]` and an `index` `int` as inputs, return the _data_ of the Node stored at the given index, or raise an `IndexError` if the `index` does not exist.

Hint #0: In the recursive case, you will need to modify both arguments to bring your recursive call closer to the base case of hint #2. Start by diagramming on paper what this means for a call to `value_at` with a list of two or more nodes and an initial index of 1.

Hint #1: An edge case occurs when the list is empty. Raise an `IndexError`, e.g.: `raise IndexError("Index is out of bounds on the list.")`

Hint #2: A second base case occurs when the index is 0. Here you should return the data of the current `Node` being processed on the list.

Example usage:

~~~
>>> value_at(Node(10, Node(20, Node(30, None))), 0)
10
>>> value_at(Node(10, Node(20, Node(30, None))), 1)
20
>>> value_at(Node(10, Node(20, Node(30, None))), 2)
30
>>> value_at(Node(10, Node(20, Node(30, None))), 3)
IndexError: Index is out of bounds on the list.
~~~

Skeleton function implementation:

~~~
def value_at(head: Optional[Node], index: int) -> int:
    raise IndexError("Index is out of bounds on the list.")
~~~

## `max` -- 15 points

Given a `head` `Node`, return the maximum data value in the linked list. If the linked list is empty, raise a `ValueError`.

~~~
>>> max(Node(10, Node(20, Node(30, None))))
30
>>> max(Node(10, Node(30, Node(20, None))))
30
>>> max(Node(30, Node(20, Node(10, None))))
30
>>> max(None)
ValueError: Cannot call max with None.
~~~

Skeleton function implementation:

~~~
def max(head: Optional[Node]) -> int:
    raise ValueError("Cannot call max with None")
~~~


## `linkify` -- 20 points

Given a `list[int]`, your `linkify` function should return a Linked List of Nodes with the same values, in the same order, as the input `list`.

You will find it helpful to use Python's slice subscription notation here, which we haven't discussed in full but you should now be able to pickup quickly. Try the following in the REPL:

~~~
>>> items = [10, 20, 30, 40]
>>> items[1]
20
>>> items[1:3]
[20, 30]
>>> items[:3]
[10, 20, 30]
>>> items[1:]
[20, 30, 40]
~~~

Notice when using slice notation a new `list` is returned to you whose values start with the first index number, inclusive, and end with the index number following the colon, exclusive. If you leave off the starting index, it defaults to `0`. If you leave off the ending index, it defaults to the `len` of the `list`.

A skeleton for `linkify` is:

~~~
def linkify(items: list[int]) -> Optional[Node]:
    return None
~~~

Example usage:

~~~
>>> linkify([1, 2, 3])
1 -> 2 -> 3 -> None
~~~

After you are certain of the correctness of your `linkify` function, you may find it valuable to use in writing test cases for the following functions.

## `scale` -- 20 points

Given a head `Node` of a linked list and a `int` `factor` to scale by, return a new linked list of `Node`s where each value in the original list is scaled (multiplied) by the scaling `factor`.

Example usage:

~~~
>>> scale(linkify([1, 2, 3]), 2)
2 -> 4 -> 6 -> None
~~~

Skeleton function implementation:

~~~
def scale(head: Optional[Node], factor: int) -> Optional[Node]:
    return None
~~~

## Linting and Type Correctness - 15 Points

Your code will need to pass the common stylistic and type checking guidelines used throughout the semester.

## Testing

You are required to write at least 2 tests for each of the functions above. This will be good practice in thinking about the different edge and use cases for each. Our autograder will be checking for this.

Reminder to change function names and rediscover tests as you add them. Test functions must have unique names and their names must begin with test_.

## Hand-in Will Open Soon

You should write your own tests to be confident of your implementations. None of these functions require much code to complete, but will take some mental gymnastics to think about approaching recursively.

Remember: Focus on what you need to do with only the head node and then leave the rest of the problem working through the rest of the list to the recursive function call.

Go ahead and delete any submission zips lingering around in your workspace from the previous exercise.

When you are ready to submit for grading, close out any open Python Debug Console terminals using the Trash Can and then open up a clean, new terminal.

`python -m tools.submission exercises/ex08`





