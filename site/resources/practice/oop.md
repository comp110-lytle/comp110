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
        """Marks a task as done in the todo list."""
        if task in todo_list:
            todo_list[task] = True
        return todo_list

    def change_class(self, new_title: str) -> "TA":
        """Creates a new TA object with the given title."""
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

# Conceptual Questions Solutions
*Question 1-4 Coming Soon*

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

# General Questions Solutions
*Coming Soon*
