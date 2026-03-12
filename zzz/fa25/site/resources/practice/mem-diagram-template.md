---
title: Practice Memory Diagrams, Organized By Topic
author:
- Alyssa Lytle
- Team 110
page: lessons
template: overview
---
# First Line

<!-- 
If you're struggling with memory diagrams, try filling in the blanks to create a guide for yourself! Try finishing each sentence with *what* you should write and *where* (E.g. "write a box with the variable name in the stack under 'globals'" or "draw this object in the heap with an arrow pointing to it from this variable in the stack") as well as where in the code you should look next (e.g. "continue to the next line" or "exit the function to the return address"). It might also be helpful to include examples or drawings!

As you learn more in this class, there are more concepts you will be diagramming. We try to break these concepts up into "levels" so you can fill in the guide up to your current level. -->

<!-- 

# Level 0: Basics

* When a new variable  of type `int`, `float`, `bool`, or `str` is instantiated:
* When the value of a variable of type `int`, `float`, `bool`, or `str` is updated:
* When the `print` keyword is used:

# Level 1: Functions

* When a function is defined:
* When a function is called with no arguments:
* When a function is called with argument(s) on the stack:
* When the `return` keyword is used and the returned value is an object on the stack (e.g. `int`, `float`, `bool`, or `str`):
* When a new variable  of type `int`, `float`, `bool`, or `str` is instantiated in a function frame: 
* When the value of a variable of type `int`, `float`, `bool`, or `str` is updated in a function frame:

# Level 2: Lists and Dicts

* When a new variable  of type `list` is instantiated:
* When a new variable  of type `dict` is instantiated:
* When a function is called with argument(s) on the heap:
* When, in a function frame, the `return` keyword is used and the returned value is an object on the heap (e.g. `list` or `dict`):
-->

# Level 3: Classes

* When the keyword `class` is used:
* When a constructor (this looks like a function call of the class name) is called:
* When a method is called (mention how you handle arguments, and how you assign value to `self`): 

# Level 4: Magic Methods, Operator Overloads, and Union Types
* When I see the `print()` or `str()` called on a `class` obect, I look and see if this method is defined: 
    * If it is defined, I create a frame for the method call by:
* When I see the `+` called on a `class` object, I look and see if this method is defined:
    * If it is defined, I create a frame for the method call by:
* When I see the `*` called on a `class` object, I look and see if this method is defined: 
    * If it is defined, I create a frame for the method call by: