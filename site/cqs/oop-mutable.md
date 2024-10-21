---
title: Challenge Question 
author:
- Alyssa Byrnes
page: lessons
template: overview
---

# Intro To Object Oriented Programming 

## Introduction

Previously, we've talked about whether or not a function *mutates* (aka changes) a variable. 

For example, we might want a function that takes a `list` as an input and *mutates* that list, OR we might want a function that takes a `list` as an input, does NOT mutate that list, but instead tells us something about that list or returns a new `list` with changes made to it. 

This idea also applies to methods! As we've talked about previously, methods often *mutate* (or change) the object they belong to. Think about our `Pizza` class from the lesson. The `add_toppings` method *mutates* a Pizza object by changing the value of `self.toppings`. On the other hand, the `price` method did not change the value of any attributes, so it does NOT mutate the Pizza object.

For this CQ, we are going to create and compare two similar methods. They both have similar functionality, but one *mutates* the class object and one does not.

## 0. Set up files
Create a new folder inside "lessons" called "CQ08" and a new file inside of it titled "point.py".

## 1. Create `Point` class

We are creating a `Point` class that has both an `x` and a `y` attribute. Think of it as the representation of a point on an (x,y) coordinate graph. We are going to talk about methods that *scale* a point, or change its value by multiplying the `x` and `y` values by some value.

Create a class with the following properties:

* The class name is `Point`
* It has the attributes `x` and `y` which are both `floats`

Now, define a constructor (aka an `__init__` method) that takes as input `x_init: float` and `y_init: float` and assigns those as the initial values for the attributes `x` and `y`. 

## 2. Mutating Method: `Point#scale_by`

Now, you are going to write a method that belongs to the Point class and *mutates* a `Point`. 

It should have the following properties:

* Method name: `scale_by`
* Parameters: `self` and `factor: int` (In general, the first parameter of a method should always be `self`)
* Return Type: None
* Behavior: It should update the x and y attributes so that `x = x * factor` and `y = y * factor`



## 3. Non-Mutating Method: `Point#scale`

Now, you are going to write a method that belongs to the Point class and instead of *mutating* a `Point`, it creates a new `Point`. 

It should have the following properties:

* Method name: `scale`
* Parameters: `self` and `factor: int` (In general, the first parameter of a method should always be `self`)
* Return Type: `Point` *
* Behavior: It should return a new `Point` with x and y attributes equal to `self.x * factor` and `self.y * factor`. 

*Reminder: if we are defining a method that returns its own type (e.g. a method in our `Point` class that returns a `Point`), we also need to add the line `from __future__ import annotations` to the top of our file. For an example, look back at our `Pizza` class!

## Checking Your Methods For Correctness

Check your methods by creating a new file in your `CQ08` file called `make_points.py` and importing your `Point` class using `from lessons.CQ08.point import Point`. Then create a new point and call the methods.

Check that calling `Point#scale` does not mutate the `x` and `y` values of your original Point.

## 4. Submission

Create your submission with the following command:

```
python -m tools.submission lessons/CQ08
```
