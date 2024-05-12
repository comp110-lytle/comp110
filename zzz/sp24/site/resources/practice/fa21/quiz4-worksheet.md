---
title: Quiz 04 Practice
author:
- Megan Zhang
- David Karash
page: lessons
template: overview
---

# Concepts on Quiz 4

Before working through these practice questions, you should first carefully read this page on [Quiz Expectations](/resources/quiz-expectations.html).

Quiz 4 will cover the following concepts:

* Lessons 23 through 26

# Questions

The quiz itself will be similar in difficulty but longer in length than this practice worksheet.

Solutions for each problem can be found at the bottom of this page.

## Conceptual Questions

1. A class definition provides a pattern for creating objects, but doesn’t make any objects itself. (T/F)
2. By convention, Python class names start with a lowercase letter. (T/F)
3. When you define a method in a class, all objects of that class have that method associated with it. (T/F)
4. The first parameter of a method is a copy of the object the method is called on. (T/F)
5. A class definition must come before an object of that class is instantiated. (T/F)
6. You must have an instance of a class (an object) to call the class’s constructor.  (T/F)
7. Constructors must take at least one parameter of type `str`. (T/F)
8. Constructors must have the `self` parameter in their signature. (T/F)
9. Objects are passed into functions by reference. (T/F)
10.  The type of an object is the same as the name of the class it is an instance of. (T/F)

## Memory Diagrams

11. Produce a memory diagram for the following code snippet, being sure to include its stack and output.  
![](/static/practice_worksheets/fa21/qz04-question11.png)  

12. Produce a memory diagram for the following code snippet, being sure to include its stack and output.  
![](/static/practice_worksheets/fa21/qz04-question12.png)

## Class Writing

13. This class is slightly challenging, but take it step by step! Create a `ChristmasTreeFarm` class with the following specifications:
    a. The `ChristmasTreeFarm` class should have one attribute: a `list[int]` named `plots`.  This list will hold values that represent the size of the tree planted in that plot.  If the value in a plot is 0, then the plot is empty (does not have a tree).  Any number other than 0 indicates that a tree is growing in that plot!
    b. The constructor for the class should take two arguments, both of type int.  The first parameter should be called `plots` and is an `int` representing the total number of plots in the farm.  Notice that the attribute `plots` and the parameter `plots` for this constructor are different, and represent different things!  The second parameter should be called `initial_planting` representing the amount of plots that should be planted initially.  These initially planted plots will be trees of size 1.
    The constructor should initialize the `plots` attribute to an empty list, and then append `initial_planting’ trees of size 1.  After that, the constructor should fill the rest of the plots with zeroes to indicate that they are empty!
    c. The class should define a method called `plant`.  This method should take an argument of type `int`, representing the plot index at which a tree should be planted. The tree should be size 1 when planted.
    d. The class should define a method called `growth`.  This method should increase the size of each planted tree by 1. Remember that unplanted plots are represented by a 0 in the `plots` list.
    e. The class should define a method called `harvest`.  This method should take an argument called `replant` of type `bool` that will determine whether this method replants trees (sets them to size 1 after harvest) or leaves the plots empty (sets them to size 0 after harvest). For our method, trees that are at least size 5 will be harvested. The method will return the count of how many trees were successfully harvested (type `int`).  


## Function Writing

14A. Write a function called `find_courses`. Given the following `Course` class definition, `find_courses` should take in a `list[Courses]` and a `str` prerequisite to search for. The function should return a list of the `names` of each Course whose `level` is 400+ and whose `prerequisites` list contains the given string.  
![](/static/practice_worksheets/fa21/qz04-question14.png)  

14B. Write a method called `is_valid_course` for the `Course` class. The method should take in a `str` prerequisite and return a `bool` that represents whether the course’s `level` is 400+ and if its `prerequisites` list contains the given string.

# Solutions

## Conceptual Questions

1. True
2. False
3. True
4. False
5. True
6. False
7. False
8. True
9. True
10. True

## Memory Diagrams

11. ![](/static/practice_worksheets/fa21/qz04-solution11.png)  

12. ![](/static/practice_worksheets/fa21/qz04-solution12.png)

## Class Writing

13. ![](/static/practice_worksheets/fa21/qz04-solution13.png)

## Function Writing

14A. ![](/static/practice_worksheets/fa21/qz04-solution14A.png)

14B. ![](/static/practice_worksheets/fa21/qz04-solution14B.png)