---
title: Week 5 Practice
author:
  - Vincent Li
page: resources
template: overview
---

# Concepts Reviewed

These questions are optional supplements that ideally help you get prepared for the quizzes ahead of time.(Some of them are also designed for elaboration purposes as you can see from the tag. Don't worry them if you just want to get prepared for the quizzes) Before working through these practice questions, you should get familiar with the concepts covered in the lessons of the Fifth Week.

<br>

# Questions
These questions might not be in the same format as quizzes. Don't hesitate to bring them to the Tutoring section for help.

### List Memory
1. In Python, when you create a variable of type `list`, where does it get stored? (Hint: Stack or Heap?)

2. In the Memory Diagram, how do we represent something that is stored in the Heap? (Instead of drawing an Arrow, how do we represent the reference to Heap?)

3. When we see the code like `x: list[int] = [1, 2, 3]`, how do you handle that in Memory Diagram? Will you write anything in Stack? 

4. Is `list` in Python fixed length or infinite? (For elaboration: Do you think the `list` in Python is infinitely long? What will happen eventually?)

<br>

### Import
1. What is the purpose of having `import` statements in Python? When will we use it?

2. If we import a file say `fileA.py` to `fileB.py` do you think the functions from `fileA.py` will get executed after being imported?

3. (Continue on Question 2) You might have noticed that we have a line of code: `if __name__ == "__main__"`. After knowing the answer to previous questions, do you know the purpose we have this line of code?

4. What is the syntax of writing an `import` statement to import a function `helperA` from a module called `ex01` inside the package called `comp110`?

<br>

### For Loop
1. Use the `range()` function to create a `for-in` loop which behaves the same as the following loop:
~~~
i: int = 0
while (i < len(list1)):
    print(list1[i])
    i+=1
~~~

2. Can you think of the reasons why we will prefer the `for-in` loop over the `while` loop?

3. Fill in the following blank:
~~~
str1: str = "I love COMP110"
for _________:
    print(char)
~~~

4. Can we nested a loop? If so, could you state one purpose of doing so?

5. (Elaborate on For-In Loop) Unlike the normal while loop with index, the `for-in` loop might be a little inconvenient to use if we also need to take the `index` into account. Is there a function (beyond 110's scope) that will record the index while also using the `for-in` loops' syntax?

6. What would be the output of the following `for-in` loop?
~~~
for i in range(5):
    result = i * 2
print(result)
~~~

7. Is the following way of writing `for-in` loop encouraged? Why not or why yes?
~~~
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number % 2 == 0:
        numbers.remove(number)
print(numbers)
~~~

8. Any problem with the following codes? If not, what is the output?
~~~
course: list[str] = ["110", "210", "211", "301"]
for num in course:
    print(num + 100)
~~~

# Solutions

### List Memory
1. The list gets stored in the heap. The variable in the stack holds a reference to the list in the heap.

2. The reference address associated with the list in the heap.

3. We first write the name (which is `x`) inside the stack, then we write the address associated with the `list [1, 2, 3]` from the Heap.

4. Unlike the lists from some other languages, Python's lists are not fixed in length. However, they are not considered infinite as they will be limited by the available memory. 

<br>

### Import
1. Import statement promote code reusability by importing and using functionality that is defined elsewhere.

2. (This is an elaborated question) When a file (e.g., fileA.py) is imported into another file (fileB.py), Python executes the top-level code in fileA.py once during the import. However, functions or classes defined in fileA.py are not automatically executed upon import; they must be called explicitly in fileB.py.

3. This line of code will check if the file is run as the main file or gets imported. Prevent the file from executing unnecessarily.

4. 
~~~
from comp110.ex01 import helperA
~~~

<br>

### For Loop
1. 
~~~
for i in range(len(list1)):
    print(list1[i])
~~~

2. Readability, Simplicity, or Less Error(Such as no risk of having infinite loop)

3. Fill in the following blank:
~~~
for char in str1:
~~~

4. Yes. Nested loops are useful for working with multi-dimensional data structures, say a matrix.

5. (Elaborate on For-In Loop) There is a function called `enumerate()` fill free to Google it. 

6. It will only print 8

7. This is not encouraged since if we remove elements from a list while iterating it. Since the index get updated during the iteration lead to the risk that some elements get skipped. 

8. The course is a list of string instead of int. Applying `for-in` loop will return each string from it which cannot be applied with `addition` between a string and numbers.