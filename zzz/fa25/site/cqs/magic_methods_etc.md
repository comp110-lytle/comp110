---
title: Challenge Question 
author:
- Alyssa Lytle
page: CQs
template: overview
---

# Magic Methods, Operator Overloads, and Union Types

## 0: Setup

For this challenge question, you're going to modify the `Point` and `Line` classes we wrote together in class to add more functionality! This will mean modifying the `point.py` and `line.py` files inside `CQs/cq04`, so make sure you've set up those files correctly according to the instructions from class!

## 1: `Point#__str__`

First, you are going to write a `__str__` magic method to return Points in a readable way! It should return

```(<x value>, <y value>)```

where `<x value>` and `<y value>` are the `x` and `y` attributes of the `Point`, respectively.

### Example Usage

<pre>
<div class="terminal">$ python 
>>> from CQs.cq04.point import Point
>>> my_point: Point = Point(1.0, 2.0)
>>> print(str(my_point))
(1.0, 2.0)
</div>
</pre>

## 2: `Point#__mul__`

Now, you are going to add a `__mul__` method to overload the multiplication `*` operator!

The goal is that when multiplying a `Point` object with a `factor: int`, it should create a new `Point` where both the `x` and `y` attributes should be the previous points attributes multiplied by `factor`. 

### Example Usage:

<pre>
<div class="terminal">$ python 
>>> from CQs.cq04.point import Point
>>> my_point: Point = Point(1.0, 2.0)
>>> new_point: Point = my_point * 3
>>> print(new_point)
(3.0, 6.0)
</div>
</pre>

## 3: `Line#__str__`

Now that we have a way to visualize `Point` objects, you can use the `str` interpretation of Points to visualize a line!

It should return 

```(<p1> <-> <p2>)```

where `<p1>` and `<p2>` are the `p1` and `p2` attributes of the `Line`, respectively.

(Note that you should NOT need to manually access the x and y attributes of each Point to print them! You should be able to just convert the points to a string using the `__str__` magic method you defined in Part 1.)

### Example Usage:

<pre>
<div class="terminal">$ python 
>>> from CQs.cq04.line import Line
>>> from CQs.cq04.point import Point
>>> point_1: Point = Point(1.0, 2.0)
>>> point_2: Point = Point(3.0, 4.0)
>>> my_line: Line = Line(point_1, point_2)
>>> print(str(my_line))
(1.0, 2.0) <-> (3.0, 4.0)
</div>
</pre>


## 4: `Line#__mul__`

Now, you are going to add a `__mul__` method to `Line` to overload the multiplication `*` operator!

The goal is that when multiplying a `Line` object with a `factor: int`, it should create a new `Line` where both the `p1` and `p2` attributes should be the previous Line's attributes multiplied by `factor`. 

(Note that you should NOT need to manually access the x and y attributes of each Point to print them! You should be able to just multiply the points by `factor` using the `__mul__` magic method you defined in Part 2.)


### Example Usage:

<pre>
<div class="terminal">$ python 
>>> from CQs.cq04.line import Line
>>> from CQs.cq04.point import Point
>>> point_1: Point = Point(1.0, 2.0)
>>> point_2: Point = Point(3.0, 4.0)
>>> my_line: Line = Line(point_1, point_2)
>>> new_line: Line = my_line * 2
>>> print(str(new_line))
(2.0, 4.0) <-> (6.0, 8.0)
</div>
</pre>

<!-- ## 1.1: Union Types
Now, modify `__mul__` so that the `factor` parameter can be either a `float` or an `int`!

### Example Usage:
<pre>
<div class="terminal">$ python 
>>> from CQs.cq04.point import Point
>>> my_point: Point = Point(1.0, 2.0)
>>> new_point: Point = my_point * 3.0
>>> print(new_point)
x: 3.0; y: 6.0
</div>
</pre> -->

<!-- ## 2: `__add__()`

Now, you are going to add an `__add__()` method to overload the addition `+` operator!

It should behave similarly to multiplication, where it creates a new `Point`, but now *adds* to the `x` and `y` attributes.

<pre>
<div class="terminal">$ python 
>>> from CQs.cq04.point import Point
>>> my_point: Point = Point(1.0, 2.0)
>>> new_point: Point = my_point + 3.0
>>> print(new_point)
x: 4.0; y: 5.0
</div>
</pre>

## 2.1: Union Types
Now, modify `__add__` so that the `factor` parameter can be either a `float` or an `int`! -->



## 5: Submission

Create your submission with the following command:

```
python -m tools.submission CQs/cq04
```