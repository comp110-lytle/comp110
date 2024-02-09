---
title: Week 2 Practice
author:
  - Vincent Li
page: resources
template: overview
---

# Concepts Reviewed

These questions are optional supplements that ideally help you get prepared for the quizzes ahead of time. Before working through these practice questions, you should get familiar with the concepts covered in the lessons of the third week.

<br>

# Questions
These questions might not be in the same format as quizzes. Don't hesitate to bring them to the Tutoring section for help.

### Functions
1. Answer the 1.1 and 1.2 based on the following codes:
~~~
def foo(x):
  return x + 1

def bar(x):
  return x * 2

print(foo(bar(3))) 
~~~
1.1 Do you know from the above codes, which function has been called the first? Foo or bar?

1.2 What will be the final line’s output?

2. This is an open-ended question, as we have learned the creation of function, can you think of the benefits of using functions in programming?

3. Regarding the naming convention or naming rule for naming a function in Python, identify the following statements as either true or false.
- The name could start with a number, 1, 2, 3, etc
- The name can only contain letters, numbers, and underscores
- The name can contain any characters as long as the first one is a letter or an underscore.
- The name can be a reserved keyword in Python that is capitalized. (such as DEF, IF, FOR)
- It is encouraged to have the first letter of the name capitalized as it is also the convention we follow in daily writing. 

4. What is the difference between a function definition and a function call?

5. 
5.1 Write a function called `odd_or_even`. Given a list of `ints` and one `string` of either `even` or `odd`, the function will return a substring containing only the even or odd numbers based on the input `string`.

5.2 Write a function called `even_and3`. Given a list of `int`s, the function should return a substring with numbers that are either `even` or at the `index of multiple of 3`.

5.3 Based on the codes you wrote for 5.1 and 5.2, could you identify the following elements with the codes? 
a. return type declaration
b. arguments
c. parameters
d. returned value
e. function signature

6. What is the difference between a return statement and a print statement in a function?

7. What is the purpose of the global keyword in a function?

8. What is the scope of a variable in a function? (Hints: Think of global scope and function scope)


9. What is the output of this code?
~~~
x = 10

def foo():
  x = 20
  print(x)

foo()
print(x)
~~~

10. What is the output of this code?
~~~
x = 10

def foo():
  global x
  x = 20
  print(x)

foo()
print(x)
~~~

11. What is the output of this code?
~~~
x = 10

def foo():
  x = 20
  def bar():
    global x
    x = 30
  bar()
  print(x)

foo()
print(x)
~~~


# Solutions

### Functions
1. Answer the 1.1 and 1.2 based on the following codes:

1.1 Do you know from the above codes, which function has been called the first? Foo or bar?
- `bar` will be called the first.

1.2 What will be the final line’s output?
Answer: 7

2. This is an open-ended question, as we have learned the creation of function, can you think of the benefits of using functions in programming?
- Benefits of using functions include code reuse, organization, readability, and maybe ease of debugging.rstudi

3.1 False
3.2 True
3.3 True
3.4 False
3.5 False

4. What is the difference between a function definition and a function call?
- A function definition specifies the name, parameters, and body of the function, while a function call executes the function with given arguments.

5. Open-ended questions, feel free to go VSCode to try it or tutoring.

6. A return statement sends a value back to the caller and exits the function, while a print statement outputs a value to the console without exiting or returning to the caller.

7. The purpose of the global keyword is to declare that a variable inside a function is global, allowing the function to modify the variable outside of its local scope.

8. The scope of a variable in a function is limited to the function itself unless it is declared global.


9. What is the output of this code?
~~~
x = 10

def foo():
  x = 20
  print(x)

foo()
print(x)
~~~
20
10

10. What is the output of this code?
~~~
x = 10

def foo():
  global x
  x = 20
  print(x)

foo()
print(x)
~~~
20
20

11. What is the output of this code?
~~~
x = 10

def foo():
  x = 20
  def bar():
    global x
    x = 30
  bar()
  print(x)

foo()
print(x)
~~~
20
30

