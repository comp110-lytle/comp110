---
title: Variables
author:
- Ezri White
page: resource
template: overview
---

## Basic Data Types

There are four simple data types in python that are important for this course:

~~~ {.python}
int, float, str, bool
~~~

These stand for integer, floating-point number, string, and boolean respectively. These data types are known as __primitives__. These store *single* pieces of data and are the building blocks of everything we will create in code. Primitive data types can be combined together to construct more complicated compound data types.

### integers and floats

The `int` and `float` types are used for numerical data.

`int` values can only hold positive or negative whole numbers:

~~~ {.python}
23
0
-110
~~~

`float` values can hold positive or negative whole numbers and decimal values:

~~~ {.python}
20.20
0.123
110.0
~~~

### strings

The `str` type is used for textual data. All strings are enclosed in quotes. Anything inside of these quotes is part of the string.

Two strings can also be concatenated to be one string!

Examples of string literals:

~~~ {.python}
"Hello, World"
"COMP110"
"42"
"I am " + "5" + " years old!"
~~~

Note: "42" is treated as a string since it's in double quotes. This is NOT the same as the `int` 42.

### booleans

The `bool` or boolean type is used for true and false. A boolean can be either true or false - that's all folks!

Examples of boolean literals (Note the capital letters!):

~~~ {.python}
True
False 
~~~

## Setting Up Variables 

Variables are used to store, change and access data which makes them one of our most powerful tools. Each variable has its own name and holds a specific type of data. Before you use a variable, you must declare it in your program!

### Declaration

When you declare a variable, you're stating that the identifier (the variable's name) will refer to a value of a specific data type.

~~~ {.python}
<variableName>: <type>
~~~

Variable names have no spaces and can only use letters, numbers, and underscores.

If a variable name involves a phrase or multiple words, we often use something called snake case in which words are separated by underscores. This is not required but it can make your variable names easier to read.

Example of camel case:

~~~ {.python}
mybestfriend: str      # without snake case, this is ok
my_best_friend: str    # with snake case, this is better...preferred in fact!
~~~

You cannot declare more than one variable with the same name within the same scope, and you cannot access a variable outside of its scope. Further, no variable can be used before it is declared.

Example of declaration:

~~~ {.python}
my_favorite_number: int
~~~

When you declare a variable without __initializing__ it in the same statement, you must designate the variable's type.


### Initialization

When you assign a value to a variable for the first time, you are giving it an initial value. This is called *initializing* the variable. Here's what this looks like:

~~~ {.python}
<variable_name> = <value>
~~~

The type of the value you assign to the variable must match the type you specified when you *declared* the variable.

Example of initialization:

~~~ {.python}
my_favorite_number: int      # declaration
my_favorite_number = 110        # initialization
~~~

You may also declare and initialize a variable in the same statement:

~~~ {.python}
my_favorite_number: int = 110    # declaration & initialization
~~~

### Assignment

After you *declare* and *initialize* a variable, you can still change its value. All you have to do is *assign* a new value to that variable. When you change a variable's value, you are re*assigning* a new value to that variable. A variable's value is the value most recently assigned to that variable.

Example with my_favorite_number:

~~~ {.python .numberLines startFrom="1"}
my_favorite_number: int = 22     # declaration & initialization
print(my_favorite_number)           # prints out 22
my_favorite_number = 110            # assignment
print(my_favorite_number)           # prints out 110 
~~~

## Scope

__Scope__ refers to the visibility of a variable in your code. In other words, which parts of a program can use a particular variable. The simple rule to remember is: *a variable can only be referenced from within the same code block in which it is defined.*

### Blocks

Each code block is grouped together by whatever is indented after a colon ":". For example:

~~~ {.python}
course: int = 101  

if (course == 110):
    welcome: str = "Welcome to COMP 110!" 
else:
    print("Should've taken 110")

print(welcome) # ERROR 
~~~

In the code above, the *print(welcome)* call would cause an error, because the program is not able to access the welcome variable, as it was declared within the if statement block which we have not accessed.

So how can we fix this? Let's look at another example:

~~~ {.python}
course: int = 101 
welcome: str = "Let's get ready to rumbleeee!"

if (course == 110):
    welcome = "Welcome to COMP 110!" 
else:
    print("Should've taken 110")

print(welcome) # prints "Let's get ready to rumbleeee!" 
~~~

This would now work! Because we have declared the *welcome* variable inside the same block as the print call, *as well as* updating its later in the if block. *Welcome* can be accessed from either point and the code will run!

This rule of scope applies to function blocks, if-then-else blocks, for/while loop blocks, etc.

### Variable Shadowing 

In blocks of code like the one above, where there is a nested 'inner block,' it is possible to declare a variable with the same name as another variable in the outer block. This is known as variable shadowing. 

Although this will not cause an error, it makes it very tricky to remember which variable is storing which piece of data and what you want each one to do.

Therefore, it is good practice to give your variables meaningful names, so you know exactly why you created them and what you want them to do.

An example of variable shadowing is shown below:

~~~ {.python}
test: bool = true
b: int = 1485 
print(b) # prints 1485

if (test):
    b: int = 1200
    print(b) # prints 1200 

print(b) # prints 1485, not 1200!! 
~~~