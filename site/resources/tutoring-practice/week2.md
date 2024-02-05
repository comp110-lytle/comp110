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
x: int = 10
result:str = ""

while x > 0:
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

# Solutions
### Elif
1. `elif` is more efficient and readable than normal `if-else` statements. To achieve the function of `elif`, a deep nested `if-else` statement might be used and therefore make the code difficult to interpret. 

2. The order of `elif` statements is sequential, only the first conditional statement that evaluates to `True` will get executed, the rest of the `elif` statements are skipped.

3. What would be the output of the following codes?
3.1 
D

3.2 say x=15 or any number greater than 14

3.3 A, B, C will all get printed in sequence.

4. Rewrite the following codes with `elif`:
~~~
course: int = 110

if course == 110:
    print("Welcome to COMP 110!")
elif course < 110:
    print("Enrolled!")
else:
    print("Prerequisites not satisfied")
~~~


### While-Loop
1. 
a. Repeat Block: block inside the while loop
b. Condition: i<10
c. Increment: i+=1

2. False, if the conditional statement at the start never met, the repeat block never got executed.


3. "12510"

4. Try to count (if possible) how my iterations of do following loops have:
4.1: 8

4.2: 5

4.3 Infinity

5. See if there is something wrong with the following loops, if so, how can you correct them?
5.1: No increment on i, causing infinite loop

5.2: j-=1 should be placed inside the while loop.

5.3: i is not defined before the loop, meanwhile the condition of the loop will eventually lead to `IndexError`.

5.4: Infinite loop

7. Some taks might need to run continuously until an external condtion or event occurs. Say a server listening loops which need to continuously active to incoming request until it is turned off. 



