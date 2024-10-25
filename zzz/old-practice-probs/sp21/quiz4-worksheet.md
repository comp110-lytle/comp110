---
title: Quiz 04 Practice
author:
- Megan Zhang
- Jasper Christie
page: quiz4-worksheet
---

# Questions

Below are optional practice problems for Quiz 04. These problems are intended to help you become more comfortable working with classes and objects. This practice is intended to reinforce important concepts and does not necessarily reflect the format of the questions on the quiz.
Solutions for each problem can be found at the bottom of this page.

## Object-Oriented Programming T/F

1.	A class definition provides a pattern for creating objects, but doesn’t make any objects itself. (T/F)
2.	An object can be declared prior to the class definition. (T/F)
3.	A constructor declaration specifies a return type. (T/F)
4.	Objects are stored in memory on the stack. (T/F)
5.	When an object is passed to a function as an argument, the function accesses a copy of it, rather than a reference to the original object. (T/F)
6.  Attributes are defined on each object. (T/F)
7.  When you define a method in a class, all objects of that class have that method associated with it. (T/F)
8. The first parameter of a method is a reference to the object the method is called on. (T/F)
9. Each time you call a constructor, a new object is created on the heap. (T/F)

## Function Writing

11.	Given the class definition of a `Course`, write a function called `find_courses` that takes in a list of Courses and a string (representing a course prerequisite) to search for. The function should iterate through all of the courses, and return a list of the names of each course that is a 400+ level course and whose `prerequisites` list contains the given string.  
![](/static/practice_worksheets/qz04-function1.png)

## Class Writing

12. Create a `Time` class that has two attributes: hours and minutes.  
Define a constructor for the class that takes in 2 optional values for hours and minutes. The default for hours is 12 and the default for minutes is 0.  
Write an `add_time` method that takes in an additional `Time` object and returns a new `Time` object with the sum of the two times. Note: Result should be in standard (12-hour) time. Example: (10 hr and 50 min) + (4 hr and 20 min) is (3 hr and 10 min)  
Write a `display_time` method that prints out the time in the following format: “Time is __ hours and __ minutes.”  
Write a `display_minute` method that prints out the total minutes in the time. Example: (1 hr 2 min) should print “62 minutes”

13. Write a single line of code that would create a third Time object whose initial hours and minutes values are the sum of the following two Time objects:

~~~
t1: Time = Time(2, 50)
t2: Time = Time(1, 20)
~~~

## Diagramming 

Draw a diagram of the code listing below, and answer the questions that follow.
![](/static/practice_worksheets/qz04-code1.PNG)

14. How many individual `Product` objects were required to evaluate the code listing?
15. What _type_ would `b[0].uses[0]` evaluate to?

## Spot the Error

Answer the questions that follow based on the code listing.

![](/static/practice_worksheets/qz04-code2.PNG)

16. When this code is run, an error ocurrs. What is missing from the `Plant` class constructor that causes an error?
17. Assuming the issue from question 18 is corrected, could you access the `species` attribute of `a` with the line `a[0]`?


# Solutions

## Object-Oriented Programming T/F

1.	T
2.	F
3.	F
4.	F
5.	F
6.  T
7.  T
8.  T
9.  T

## Function Writing
11. ![](/static/practice_worksheets/qz04-function1-answer.png)

## Class Writing
12. ![](/static/practice_worksheets/qz04-class1-answer.png)

13. `t3: Time = t1.addTime(t2)`

## Diagramming 1

![](/static/practice_worksheets/qz04-diag1.png)

14. 2
15. str

## Spot the Error
16. The first parameter in the constructor should be `self` and lines 8 and 9 should use `self` to initialize the attributes. These corrections are shown below:
![](/static/practice_worksheets/qz04-code2-answer.PNG)

17. No, `Plant` objects are not subscriptable the way the class is defined right now. If we, for some reason, wanted to do this, we would define the method `__getitem__`.