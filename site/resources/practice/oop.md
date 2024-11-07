---
title: OOP Conceptual Questions
author:
- Viktorya Hunanyan
- David Karash
- Megan Zhang
- Alyssa Lytle
page: lessons
template: overview
---

# Conceptual Questions
1. What does `__init__` return? Why is it important for it to return this? 
2. Does every class need an `__init__` method? 
3. Let’s say you have a class with 5 attributes. When you call the constructor of this class, do you need to pass 5 arguments to the constructor? Is it possible to pass less than 5? How so? 
4. How many methods does a class have to have? 
5. A class definition provides a pattern for creating objects, but doesn’t make any objects itself. (T/F)
6. By convention, Python class names start with a lowercase letter. (T/F)
7. When you define a method in a class, all objects of that class have that method associated with it. (T/F)
8. The first parameter of a method is a copy of the object the method is called on called `self`. (T/F)
9. A class *definition* must come before an object of that class is *instantiated*. (T/F)
10. You must have an instance of a class (an object) to call the class’s constructor. (T/F)
11. Constructors must have the `self` parameter in their signature. (T/F)
12. Constructors must take at least one parameter other than the self parameter. (T/F)
13. Objects are passed into functions by reference. (T/F)
14. The type of an object is the same as the name of the class it is an instance of. (T/F)
15. `__init__` doesn't take `self` as an argument when the constructor is called, but it does have it as a parameter. (T/F)
16. `__init__` doesn't contain a `return` statement, but it does return something. (T/F)
17. Similar to how a function is first *defined* then *called*, a class is first *defined* then ____.

# Magic Methods Conceptual Questions

The following questions will refer to the following code: 

```
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2
print(v1)
print(v2)
print(v3)
```

1. Where is the `__str__ `method called? How do you know it is called? 
2. Where is the `__add__` method called? How do you know it is called? 
3. What is the output of `print(v1)`?
4. What is the output of `print(v2)`?
5. What is the output of `print(v3)`?
6. From questions 1 and 2, in order to call a magic method, how do you do this? Give an example of calling a `__mul__` method on the vector object v1. This method will take in an int and multiple each component of the input vector by that int. 
7. Implement the `__mul__` method discussed in question 3. 
8. In general, what is the point of magic methods? To answer this, compare and contrast the `__mul__` method vs the `__add__` method in the Vector class. 

# General Questions

1. Write the general formula of how you instantiate an object belonging to a class using the following. You might not need to use all and can use any multiple times: `:`, `=`, `()`, `<arg>`, `<class_name>`, `<variable_name>`,  `method_name`, `__init__`. 

2. Write the general formula of how you call the constructor of a class using the following. You might not need to use all and can use any multiple times: `:`, `=`, `()`, `<arg>`, `<class_name>`, `<variable_name>`, `method_name`, `__init__`.  

3. Write the general formula of how you call a method of a class on an object stored in `<variable_name>`, using the following. You might not need to use all and can use any multiple times: `:`, `=`, `()`, `<arg>`, `<class_name>`, `<variable_name>`, `method_name`, `__init__`. 

4. Give an example of calling a constructor of a built in type.

5. Give an example of calling a method on an object. Use the methods that we have already practiced. 

6. Given the following class definition, do the following: 

```python
class TA:
    semester_pay: int
    hours_per_week: int
    title: str

    def __init__(self, title: str):
        self.title = title
        if self.title == "Comp 110 TA":
            self.hours_per_week = 5
            self.semester_pay = 1000
        else:
            self.hours_per_week = 5
            self.semester_pay = 0

    def todo_list(self, todo_list: dict[str, bool]) -> dict[str, bool]:
        return todo_list

    def check_off(self, task: str, todo_list: dict[str, bool]) -> dict[str, bool]:
        if task in todo_list:
            todo_list[task] = True
        return todo_list

    def change_class(self, new_title: str) -> "TA":
        return TA(new_title)
```

- 6a. In the fall, you become a TA for Bio 101. Using the class above, create a `TA` object that is a `"Bio 101 TA"`. 
- 6b. The next semester you change the class you TA for. Using the `change_class` method, create a new object of a `"Comp 110 TA"`. 
- 6c. As a comp 110 TA, you have to do the following: 
    - 4 hours of OH
    - 1 hour of AH
    - grade quiz question 6.1

    Using the `todo_list` method create a list of items that you have to do. You need to make sure that you have some way of accessing this list so that you can check off items as you progress through the week. 

- 6d. In your todo list object, check off `"1 hour of AH"`. 
- 6e. In your todo list object, check off `"4 hours of OH"`. 

# Solutions 
## Conceptual Questions Solutions 
1. For the scope of this class we say that `__init__` returns the reference number to the object created. More than likely, when the class that this `__init__` method belongs to is called, it is assigned to a variable. More specifically, the return value of calling the class will be assigned to this variable. It is important for `__init__` to return the object so that the created object can be referenced using the variable it was assigned to. If it wasn't assigned to anything—that is, if the class created an object without returning this object—then this object is not referenced by anything in the stack and is floating in the void of the heap. Without a reference, the object becomes inaccessible, and Python’s garbage collector will eventually remove it from memory, as it’s no longer needed.

2. For the scope of this class, yes all classes need an `__init__` method. This because when we want to create an object belonging to a class, we will call the class that the object will belong to. When a class is called, Python allocates memory for a new object of that class. This new object is an empty "shell" instance of the class. After the memory allocation, Python calls the class’s `__init__` method to initialize the object. The new, empty object is automatically passed to `__init__` as self, making self a reference to the specific instance being created. The `__init__` method then goes ahead and adds any attributes to that empty object. 

3. You do not need to pass 5 arguments in order to assign 5 feilds a value. For example the code below has 3 attributes but only passes 1 argument to the constructor: 

```
class Week: 
    day: str
    days_of_the_week: dict[str, int]
    my_num: int

    def __init__(self, day): 
        self.day = day 
        self.days_of_the_week = {"Sun": 0, "Mon": 1, "Tues": 2, "Wed": 3, "Thurs": 4, "Fri": 5, "Sat": 6}

        for days in self.days_of_the_week: 
            if days == day: 
                self.my_num = self.days_of_the_week[days]
```

4. Every class must have at a miniumum 1 method, the `__init__` method. 

5. True
6. False
7. True
8. False
9. True
10. False
11. True
12. False
13. True
14. True
15. True
16. True
17. Instantiated

## Magic Methods Conceptual Questions Solutions
1. The `__str__` method is called when `print(v1)`, `print(v2)`, and `print(v3)` are executed. 
This is because any argument passed to the `print()` function is first passed to the `str()` in order to turn the argument to a string. The `str()` returns a string representation of the argument passed to it's function.

We know how to do things such as: 
```
print(8)
x: str = "float"
print(x)
print(type(x))
print(False)
print(8 + 4.0)
```

All of these will output a string representtion of the simplified argument value passed to the `print()` function. But notice, all the argument above are of type that are built into python already. 
In our case, when we have `print(v1)`, what is the type of `v1`? Well `v1` is of the type `Vector`. Does python know how to print out a `Vector` object?? Is this a type that the creator of python thought everyone would use? 
No, it's a type that we defined! So therefore, when we want to print this object of the type `Vector`, we have to tell python how exactly we want it to print it. More speficially, the `print()` function simply prints out whatever it recieves from the `str()` function therefore, we have to specify how to turn a `Vector` object into a string representation. 
That is where our `__str__` magic method come in. When python calls `print()`, it has no problem entering into the `print()` function but it encounters a problem when it needs to call the `str()` function since it doesn't know how exactly you want to print this object. 
So what python does is it checks to see if there is a magic method to overload this operation -- the counterpart of the `str()`. So it checks in the `Vector` class and sees `__str__` is defined so it passes the argument, otherwise passed to `str()`, to this magic method and evaluates the function body and it returns a string representation of the `Vector` object that it passes back to the print function and print outputs.

2. The same logic for the solution to 1 applies here as well. The `__add__` method is called in the line `v3 = v1 + v2`. This line uses the `+` operator between two `Vector` instances (`v1` and `v2`). When the `+` operator is used, Python automatically calls the `__add__` method of the first operand, in this case, `v1`.

3. `Vector(2, 3)`
4. `Vector(4, 5)`
5. `Vector(6, 8)`
6. To call a magic method, you use the corresponding operator or function associated with that method, rather than calling the method directly. 

For instance:

- For `__str__`, you use `str()` or `print()`.
- For `__add__`, you use the `+` operator.

To implement and call a `__mul__` method that multiplies each component of the `Vector` by an integer, you would use the `*` operator. For example, if `__mul__` were defined in `Vector`, you could call it with `v1 * 3`, which would return a new `Vector` with each component of `v1` multiplied by `3`. 

7. Implementation is below: 

```
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

# Example Usage
v1 = Vector(2, 3)
v4 = v1 * 3
print(v4)
```

8. Magic methods allow classes to define custom behavior for built-in operations and functions, enabling objects to integrate seamlessly with Python’s syntax and operators. They make custom objects behave more like built-in types. 

The `__add__` method allows `Vector` objects to be combined using the `+` operator, resulting in a new `Vector` with summed components. The `__mul__` method enables the use of the `*` operator to scale a `Vector` by multiplying its components by a scalar, yielding a new `Vector`.

The key difference is that `__add__` expects another `Vector` as its argument, while `__mul__` takes a scalar integer. Since Python doesn’t inherently know how to handle operations on custom objects, magic methods allow you to define these operations in any way you choose. For example, in the `__add__` method, we decided that only two vectors should be added together, while in `__mul__`, we allowed scaling the vector by a scalar.


## General Questions Solutions

1. ```<variable_name>: <class_name> = <class_name>(<arg>)```
2. ```<class_name>(<arg>)```
3. ```<variable_name>.<method_name>(<arg>)```
4. ```my_list = list()```
5. ```my_list.append(3)```
6. Answers below: 
- 6a. Code below: 
```
bio_ta = TA("Bio 101 TA")
```
- 6b. Code below: 
```
comp_ta = bio_ta.change_class("Comp 110 TA")
```
- 6c. Code below: 

```
todo_list = {
    "4 hours of OH": False,
    "1 hour of AH": False,
    "grade quiz question 6.1": False
}
comp_todo = comp_ta.todo_list(todo_list)
```
- 6d. Code below: 

```
comp_todo = comp_ta.check_off("1 hour of AH", comp_todo)
```

- 6e. Code below: 

```
comp_todo = comp_ta.check_off("4 hours of OH", comp_todo)
```





