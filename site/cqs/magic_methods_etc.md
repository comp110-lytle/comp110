---
title: Challenge Question 
author:
- Alyssa Byrnes
page: lessons
template: overview
---

# Magic Methods, Operator Overloads, and Union Types

For this challenge question, you're going to modify the `Point` class you previously wrote to add more functionality! (This will mean modifying the `point.py` file inside `lessons/CQ08`.)

## 0: `__str__()`

First, you are going to write a `__str__` magic method to print out points in a readable way! It should print 

```x: <x value>; y: <y value>```

where `<x value>` and `<y value>` are the `x` and `y` attributes of the `Point`, respectively.

### Example Usage

<pre>
<div class="terminal">$ python 
>>> from lessons.CQ08.point import Point
>>> my_point: Point = Point(1.0, 2.0)
>>> print(str(my_point))
x: 1.0; y: 2.0
</div>
</pre>

## 1: `__mul__()`

Now, you are going to add a `__mul__()` method to overload the multiplication `*` operator!

The goal is that when multiplying a `Point` object with a `factor: int`, it should create a new `Point` where both the `x` and `y` attributes should be the previous points attributes multiplied by `factor`. (Hint: This is the same functionality as a method you've already written in `Point`!) 

### Example Usage:

<pre>
<div class="terminal">$ python 
>>> from lessons.CQ08.point import Point
>>> my_point: Point = Point(1.0, 2.0)
>>> new_point: Point = my_point * 3
>>> print(new_point)
x: 3.0; y: 6.0
</div>
</pre>

## 1.1: Union Types
Now, modify `__mul__` so that the `factor` parameter can be either a `float` or an `int`!

### Example Usage:
<pre>
<div class="terminal">$ python 
>>> from lessons.CQ08.point import Point
>>> my_point: Point = Point(1.0, 2.0)
>>> new_point: Point = my_point * 3.0
>>> print(new_point)
x: 3.0; y: 6.0
</div>
</pre>

## 2: `__add__()`

Now, you are going to add an `__add__()` method to overload the addition `+` operator!

It should behave similarly to multiplication, where it creates a new `Point`, but now *adds* to the `x` and `y` attributes.

<pre>
<div class="terminal">$ python 
>>> from lessons.CQ08.point import Point
>>> my_point: Point = Point(1.0, 2.0)
>>> new_point: Point = my_point + 3.0
>>> print(new_point)
x: 4.0; y: 5.0
</div>
</pre>

## 2.1: Union Types
Now, modify `__add__` so that the `factor` parameter can be either a `float` or an `int`!



## 3: Submission

Create your submission with the following command:

```
python -m tools.submission lessons/CQ08
```