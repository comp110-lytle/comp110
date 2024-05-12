---
title: Linked List Utils
author:
- Kris Jordan
- Kaki Ryan
- Vrinda Desai
page: exercises
template: overview
---

## Overview

In these exercises you will implement a few algorithms to process a singly-linked list data structure. **If you have not completed CQ09 yet, go ahead do that first.** 

Recall in CQ09, we were modifying and writing methods for the `Node` class. In this exercise, you will not be creating new methods, but rather, functions that take in or return `Node` objects. To create functions in the same `linked_list.py` file, make sure you are outside of the body of the class definition. You must use **recursive function calls** to implement the functions below. If you use loops, your work for that function will be disqualified.

## `value_at` 

Given a `head` `Node | None` and an `index` `int` as inputs, return the _data_ of the Node stored at the given index, or raise an `IndexError` if the `index` does not exist.

Hint #0: In the recursive case, you will need to modify both arguments to bring your recursive call closer to the base case of hint #2. Start by diagramming on paper what this means for a call to `value_at` with a list of two or more nodes and an initial index of 1.

Hint #1: An edge case occurs when the list is empty. Raise an `IndexError`, e.g.: `raise IndexError("Index is out of bounds on the list.")`

Hint #2: A second base case occurs when the index is 0. Here you should return the data of the current `Node` being processed on the list.

Skeleton function implementation:

~~~
    def value_at(head: Node | None, index: int) -> int:
        raise IndexError("Index is out of bounds on the list.")
~~~

Example usage:

<pre>
<div class="terminal">
>>> from exercises.ex10.linked_list import Node, value_at
>>> value_at(Node(10, Node(20, Node(30, None))), 0)
10
>>> value_at(Node(10, Node(20, Node(30, None))), 1)
20
>>> value_at(Node(10, Node(20, Node(30, None))), 2)
30
>>> value_at(Node(10, Node(20, Node(30, None))), 3)
IndexError: Index is out of bounds on the list.
</div>
</pre>

## `max` 

Given a `head` `Node`, return the maximum data value in the linked list. If the linked list is empty, raise a `ValueError`.

Skeleton function implementation:

~~~
    def max(head: Node | None) -> int:
        raise ValueError("Cannot call max with None")
~~~

<pre>
<div class="terminal">
>>> from exercises.ex10.linked_list import Node, max
>>> max(Node(10, Node(20, Node(30, None))))
30
>>> max(Node(10, Node(30, Node(20, None))))
30
>>> max(Node(30, Node(20, Node(10, None))))
30
>>> max(None)
ValueError: Cannot call max with None.
</div>
</pre>


## `linkify` 

Given a `list[int]`, your `linkify` function should return a Linked List of Nodes with the same values, in the same order, as the input `list`.

A skeleton for `linkify` is:

~~~
    def linkify(items: list[int]) -> Node | None:
        return None
~~~

You will find it helpful to use Python's slice subscription notation here, which we haven't discussed in full but you should now be able to pickup quickly. Try the following in the REPL:

<pre>
<div class="terminal">
>>> items = [10, 20, 30, 40]
>>> items[1]
20
>>> items[1:3]
[20, 30]
>>> items[:3]
[10, 20, 30]
>>> items[1:]
[20, 30, 40]
</div>
</pre>

Notice when using slice notation a new `list` is returned to you whose values start with the first index number, inclusive, and end with the index number following the colon, exclusive. If you leave off the starting index, it defaults to `0`. If you leave off the ending index, it defaults to the `len` of the `list`.

Example usage:

<pre>
<div class="terminal">
>>> from exercises.ex10.linked_list import linkify
>>> linkify([1, 2, 3])
1 -> 2 -> 3 -> None
</div>
</pre>

After you are certain of the correctness of your `linkify` function, you may find it valuable to use in writing test cases for the following functions.

## `scale` 

Given a head `Node` of a linked list and a `int` `factor` to scale by, return a new linked list of `Node`s where each value in the original list is scaled (multiplied) by the scaling `factor`.

Skeleton function implementation:

~~~
    def scale(head: Node | None, factor: int) -> Node | None:
        return None
~~~

Example usage:

<pre>
<div class="terminal">
>>> from exercises.ex10.linked_list import scale, linkify
>>> scale(linkify([1, 2, 3]), 2)
2 -> 4 -> 6 -> None
</div>
</pre>


## Linting and Type Correctness 

Your code will need to pass the common stylistic and type checking guidelines used throughout the semester.


## Hand-in Will Open Soon

You should utilize the REPL or write your own tests to be confident of your implementations. None of these functions require much code to complete, but will take some mental gymnastics to think about approaching recursively.

Remember: Focus on what you need to do with only the head node and then leave the rest of the problem working through the rest of the list to the recursive function call.

When you are ready to submit for grading, run the following command:

`python -m tools.submission exercises/ex10`





