---
title: Recursive Structures Challenge Question
author:
- Alyssa Byrnes
- Vrinda Desai
page: lessons
template: overview
---

In this CQ, you will not only modify a recursive class named `Node` which will be used to represent items in the linked list data structure, but you will be setting up the file that you will need to complete EX10 - Linked List Utils. 

## Setup
In the `exercises` directory, create a directory named `ex10`. In the `ex10` directory, create a file named `linked_list.py` and establish the following starting contents:

~~~python
"""Utility functions for working with Linked Lists."""

from __future__ import annotations

__author__ = "Your PID"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Node | None

    def __init__(self, data: int, next: Node | None):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"
~~~

## Understanding the Starter Code

## Test __init__

In the REPL, instantiate Nodes to make a linked list. The structure of the linked list `node_b` below is 1 -> 2 -> None while the structure of `node_a` is 0 -> 1 -> 2 -> None. Notice that `next` is an attribute of the Node class holds a whole other Node object (or None). To access the actual values in a Node object, you need to utilize the `data` attribute. 

<pre>
<div class="terminal">$ python 
>>> from exercises.ex10.linked_list import Node
>>> node_c: Node = Node(2, None) # base case
>>> node_b: Node = Node(1, node_c)
>>> node_a: Node = Node(0, node_b) # head of list
>>> node_a.data
0
>>> node_a.next.next.data
2
>>> node_a.next.next.next
None
</div>
</pre>

## Test __str__

Alongside the constructer for the `Node` class, you have been given a  `__str__` magic method which will be used to produce string representations of objects. As we discussed in class, if you create a Node object and print it, python will **automagically** call the `__str__` method and print out your custom string message. This will be super helpful when you are creating your own linked lists for testing.

For example, without a `__str__` method defined on our Node class, we would expect to see something like this:

<pre>
<div class="terminal">$ python 
>>> from exercises.ex10.linked_list import Node
>>> example_node = Node(3, Node(2, None))
>>> print(example_node)
<Node object at 0x7f959129e130>
</div>
</pre>

But if we have the `__str__` method defined as above, we should get:

<pre>
<div class="terminal">$ python 
>>> from exercises.ex10.linked_list import Node
>>> example_node = Node(3, Node(2, None))
>>> print(example_node)
3 -> 2 -> None
</div>
</pre>

## Creating New Methods

## `head()` method

You are going to create a method called `head()` which takes in no arguments (other than `self`) and returns an `int`. The method should return the data attribute for the first element in the linked list.

<pre>
<div class="terminal">$ python 
>>> from exercises.ex10.linked_list import Node
>>> node_a: Node = Node(0, Node(1, Node(2, None)))
>>> node_a.head()
0
</div>
</pre>

## `tail()` method

Create a method called `tail()` which takes in no arguments (other than `self`) and it returns a `Node` object (or `None` if linked list is of length 1). It should return a linked list of every element minus the head.

<pre>
<div class="terminal">$ python 
>>> from exercises.ex10.linked_list import Node
>>> node_a: Node = Node(0, Node(1, Node(2, None)))
>>> print(node_a.tail())
1 -> 2 -> None
</div>
</pre>

## `last()` method

Create a method called `last()` which takes in no arguments (other than `self`) and returns an `int`. It should return the data of the last element in the linked list (Hint: Look at __str__!).

<pre>
<div class="terminal">$ python 
>>> from exercises.ex10.linked_list import Node
>>> node_a: Node = Node(0, Node(1, Node(2, None)))
>>> print(node_a)
0 -> 1 -> 2 -> None
>>> node_a.last()
2
</div>
</pre>


# Step 2: Submit!

Create a submission by running: 

`python -m tools.submission exercises/ex10`
