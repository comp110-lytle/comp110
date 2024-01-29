---
title: Week 2 Practice
author:
  - Vincent Li
page: resources
template: overview
---

# Concepts Reviewed

These questions are optional supplements that ideally help you get prepared for the quizzes ahead of time. Before working through these practice questions, you should get familiar with the concepts covered in the lessons of the second week (1.22 and Memory Diagrams).

<br>

# Questions
These questions might not be in the same format as quizzes. Don't hesitate to bring them to the Tutoring section for help.

### Elif
1. What is the purpose of using `elif`? In other words, in what circumstance do we want to use `elif` over a bunch of nested `if-else` statements?

2. What is the operation order of `elif` statements? For example, if you have multiple `elif` statements and all of them evaluate to `True`, only the first one will get executed or the last one? Or maybe all of them?

3. What would be the output of the following codes?
3.1 
~~~
x = 4

if x < 5:
    print("A")
elif x < 10:
    print("B")
elif x < 15:
    print("C")
else:
    print("D")
~~~
A. `ABCD`   B. `ABC`    C. `D`  D. `A`

3.2 Reassign the value of `x`, so that only `D` will get printed.

3.3 What will be the output if we change all the `elif` statements above to the `if` statement?

4. Rewrite the following codes with `elif`:
~~~
course: int = 110

if course == 110:
    print("Welcome to COMP 110!")
else:
    if course < 110:
        print("Enrolled!")
    else:
        print("Prerequisites not satisfied")
~~~

<br>

### While-Loop
1. Given the following codes: match them with the corresponding term:
~~~
i: int = 0
while i < 10:
    print(i)
    i += 1
~~~
a. Repeat Block
b. Condition
c. Increment

2. (True or False) Codes within the repeat block of the while loop will always get executed at least once.


3. Try to evaluate the following codes:
~~~
x: int = 110
output:str = ""

while x >= 0:
    if x % 3 == 0:
        result = result + str(x)
    else:
        result = str(x) + result
    x = x // 2
print(result)
~~~

4. Try to count (if possible) how my iterations of do following loops have:
4.1
~~~
course = "comp110"
i: int = 0
while i < len(course):
    # Codes omitted
    i += 1
~~~

4.2
~~~
j: int = 1
while j < 10:
    # Codes omitted
    j += 2
~~~

4.3 
~~~
z:float = 10.0
while z > 0:
    # Codes omitted
    z = z ** (1/2)
~~~

5. See if there is something wrong with the following loops, if so, how can you correct them?
5.1 
~~~
i = 0
while i < 5:
    print(i)
~~~

5.2
~~~
j = 10
while j > 0:
    print(j)
j -= 1
~~~

5.3
~~~
number:str = "11111"
while i <= len(number):
    print(number[i])
    i += 1
~~~

5.4
~~~
while True:
    print("True")
~~~

6. Design a loop that can achieve the desired requirements:
6.1 Create a loop that can print all even numbers between 1 to 100

6.2 Given this string `ComputerScience`, use a loop that can print the characters that have `odd` indies. (Index 0, 2, 4, 6, 8...)

6.3 (Continued on 5.2)How about a loop that can print every character except the last one? (Be careful with the IndexOutOfBound!)

6.4 A loop that will print numbers from 0 all the way to negative infinity

7. Elaborate on your thought, when will the infinite loops get intentionally used in real-life scenarios?    


