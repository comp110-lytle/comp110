---
title: OOP Questions
author:
- Benjamin Eldridge
- Izzi Hinks
- Viktorya Hunanyan
- David Karash
- Megan Zhang
- Alyssa Lytle
page: lessons
template: overview
---

## Multiple Choice

1. True or False: A class definition provides a pattern for creating objects, but doesn’t make any objects itself.

    a. True
    
    b. False

2. True or False: All instances of a class have the same attribute values.

    a. True
    
    b. False

3. True or False: An object's attribute values cannot be accessed from outside the class.

    a. True
    
    b. False

4. What is the difference between a class and an object?

    a. A class is a collection of objects
    
    b. A class is a blueprint; an object is a specific instance of that blueprint

    c. They are the same in Python

    d. An object can contain classes, but not the other way around

5. True or False: Because class definitions have attributes, local variables are not allowed inside method definitions.

    a. True
    
    b. False

6. What does it mean to "instantiate" a class?

    a. Define the class
    
    b. Import a module

    c. Create an object from a class

    d. Define attributes

7. True or False: The constructor of a class is only called once in a program, no matter how many objects of that class are constructed.

    a. True
    
    b. False

8. The first parameter of any method is _____ and it is given a reference to the object the method was called on.

    a. me
    
    b. self

    c. init

    d. this

    e. current

9. An instance of a class is stored in the: 

    a. stack

    b. heap

    c. output

10. True or False: Once attributes are initialized in the initializer/constructor, the values cannot be changed.

    a. True
    
    b. False

11. True or False: A class definition introduces a new data type, or type of object, in your program.

    a. True
    
    b. False

<details>
<summary>SOLUTIONS</summary>

1. True

2. False

2. False

3. A class is a blueprint; an object is a specific instance of that blueprint

4. False

5. Create an object from a class

6. False

7. self

8. heap

9. False

10. True

</details>

## Select All That Apply

Consider the following code listing. Select all lines on which any of the concepts below are found. Select \code{N/A} if the concept is not in the code listing.

```py
    class Point:
        x: float
        y: float
 
        def __init__(self, x: float, y: float):
            self.x = x
            self.y = y
 
        def flip(self) -> None:
            temp: float = self.x
            self.x = self.y
            self.y = temp

        def shift_y(self, dy: float) -> None:
            self.y += dy

        def diff(self) -> float:
            return self.x - self.y
```


1. Constructor Declaration

    a. 1

    b. 2

    c. 5

    d. 9

    e. 11

2. Attribute Declaration

    a. 2

    b. 3

    c. 6

    d. 7

    e. 10

3. Attribute Initialization

    a. 2

    b. 3

    c. 6

    d. 7

    e. 10

4. Method Declaration

    a. 1

    b. 9

    c. 10

    d. 14

    e. 17

5. Local Variable Declaration

    a. 2

    b. 3

    c. 6

    d. 7

    e. 10

6. Instantiation

    a. 1

    b. 5

    c. 9

    d. 10

    e. N/A

<details>
<summary>SOLUTIONS</summary>

1. Line 5 only

2. Lines 2 and 3

3. Lines 6 and 7

4. Lines 9, 14, and 17

5. Line 10

6. N/A

</details>

## Short Answer

1. What does `self` refer to in Python classes?
 
2. Similar to how a function is first *defined* then *called*, a class is first *defined* then ____.

3. When a method is called, do you have to pass an argument to the `self` parameter?

4. When is `self` used outside of a class definition?

5. Use the following point class to answer the questions.

    ```py
        class Point:
            x: float
            y: float
    
            def __init__(self, x: float, y: float):
                self.x = x
                self.y = y
    
            def flip(self) -> None:
                temp: float = self.x
                self.x = self.y
                self.y = temp
    
            def shift_y(self, dy: float) -> None:
                self.y += dy
    
            def diff(self) -> float:
                return self.x - self.y
    ```

    5.1. Write a line of code to create an explicitly typed instance of the Point class called my_point with an x of 3.7 and y of 2.3. 

    5.2. Write a line of code to change the value of the my_point variable's x attribute to 2.0. 

    5.3. Write a line of code to cause the my_point variable's y attribute to increase by 1.0 using a method call.

    5.4. Write a line of code to declare an explicitly typed variable named x. Initialize x to the result of calling the diff method on my_point.


<details>
<summary>SOLUTIONS</summary>

1. `self` refers to the current instance of the class that the methods will operate on if those methods are called in the future on an instance of that class.

2. Instantiated

3. No! When you call the constructor for a class, `self` is automatically made by python in order for the rest of the constructor to finish making the object. In the case of other methods, python knows that `self` is the object that you called the method on, often the variable name that comes before the method call (e.g. for `my_point.shift_y(1.0)`, `self` is `my_point`).

4. `self` is not used outside of a class definition. Outside of a class definition you use the name of the variable storing an object to refer to it.

5.1. `my_point: Point = Point(x=3.7, y=2.3)`

5.2. `my_point.x = 2.0`

5.3. `my_point.shift_y(1.0)`

5.4. `x: float = my_point.diff()`

</details>