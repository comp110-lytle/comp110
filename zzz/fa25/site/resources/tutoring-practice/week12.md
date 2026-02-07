---
title: Week 12 Practice
author:
  - Vincent Li
page: resources
template: overview
---

# Concepts Reviewed

These questions are optional supplements that ideally help you get prepared for the quizzes ahead of time. (Some of them are also designed for elaboration purposes as you can see from the tag. Don't worry them if you just want to get prepared for the quizzes)
<br>

# Questions 

### Object Oriented Programming(OOP)

##### Conceptual

1. So far, we have learned the idea of `functions`. What do we call them in OOP? (Functions belong to a specific object)

2. What do we call the variables that belong to each instantiation of the object?

3. Which `method` that we need to define in order to create new instances of that object? Which terminology do we use to refer to this `method`?

4. How do you create a `class/object` in Python? Demonstrate by showing a simple example.

5. What is the purpose of `__init__` method?

##### Multiple Choices

1. What is the main feature of object-oriented programming?
A) Use of functions
B) Use of loops and conditions
C) Organization of code into reusable objects
D) Execution of programs from top to bottom

2. In Python, what is a method?
A) A function that is defined outside a class
B) A piece of code that runs automatically
C) A function that is part of a class and can access its attributes
D) A variable stored inside a class


3. Which of the following is the correct way to define a class in Python?
A) class MyClass(){}
B) define MyClass:
C) class MyClass:
D) MyClass = class{}

4. How do you create an instance of a class named Vehicle?
A) Vehicle.new()
B) new Vehicle()
C) Vehicle()
D) instance Vehicle:

<br>

##### True/False

1. True or False: In Python, an object is an instance of a class.
2. True or False: The __init__ method is optional for a Python class.
3. True or False: Every Python class must contain at least one method.
4. (For Elaboration) True or False: Static methods in Python cannot access or modify the class state.
5. True or False: A class in Python can only have one constructor method (__init__).
6. True or False: Attributes defined in the __init__ method are called local variables.

<br>

##### Debugging Questions
1. Debug the following codes
~~~
class Car:
def __init__(self, brand, model):
    self.brand = brand
    self.model = model

my_car = Car("Toyota", "Corolla")
print(my_car.brand, my_car.model)
~~~

2. Debug the following codes
~~~
class Animal:
    def __init__(self, name):
        name = name

my_pet = Animal("Rex")
print(my_pet.name)
~~~


3. Debug the following codes
~~~
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return length * width

my_rectangle = Rectangle(10, 5)
print(my_rectangle.area())
~~~

<br>

# Solutions

##### Conceptual:
1. They are called `methods`

2. They are called `instance variables` or `attributes`

3. They are in general called `constructors`. Here in Python, we define a constructor by using a method named: `__init__`.

4. Here is one example:
~~~
class Car:
    # Constructor method with initialization
    def __init__(self, brand, model):
        self.brand = brand  # Instance variable
        self.model = model  # Instance variable
~~~

5. The purpose of the __init__ method is to initialize the instance variables of a new object.

##### Multiple Choices:
1. Correct Answer: C) Organization of code into reusable objects

2. Correct Answer: C) A function that is part of a class and can access its attributes

3. Correct Answer: C) class MyClass:

4. Correct Answer: C) Vehicle()

##### True/False:
1. True, objects are instances of classes.
2. True, A class can be defined without an init method, although init is commonly used to initialize instance attributes.
3. False, It's entirely possible to define a class without any methods.
4. True
5. True, Python classes can have only one constructor.
6. False, Attributes defined with self.attribute_name in the init method are instance attributes, not local variables.

##### Debug:
1. Issue: Indentation error in the __init__ method definition.
2. Issue: The attribute should be assigned to self.name = name to make it accessible as an instance attribute.
3. Issue: The area method should use self.length and self.width instead of length and width.


