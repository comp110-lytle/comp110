---
title: Week 2 Practice
author:
  - Vincent Li
page: resources
template: overview
---

# Concepts Reviewed

These questions are optional supplements that ideally help you get prepared for the quizzes ahead of time. (Some of them are also designed for elaboration purposes as you can see from the tag. Don't worry them if you just want to get prepared for the quizzes)  Before working through this week's practice questions, be sure to get familiar with the `for-in` loop syntax

<br>

# Questions

### For-In Loop

1. Which of the following loops can be put on the blank and can iterate over each character in the string s = "Python" and print them? (Choose all that apply)
~~~
for _______________:
    print(s[i])
~~~

A) for i in range(0, s):
B) for i in range(0, len(s)):
C) for i in s:
D) for i in range(s):

2. (Continue on Q1) What will be the correct option if we change the body of the loop to:
~~~
print(i)
~~~

3. Given a list `lst = [10, 20, 30, 40, 50]`, what will the following code snippet print?
~~~
for i in range(0, len(lst)):
    print(i)
~~~
A) It will print numbers from 0 to 4.
B) It will print each element in `lst`.
C) It will result in a `TypeError`.
D) It will print numbers from 1 to 5.

4. (Continue on Q3) Given a list `lst = [10, 20, 30, 40, 50]`, what will the following code snippet print?
~~~
for i in lst:
    print(lst[i])
~~~
A) It will print numbers from 0 to 4.
B) It will print each element in `lst`.
C) It will result in a `TypeError`.
D) It will print numbers from 1 to 5.

5. What is the difference between for item in list: and for i in range(len(list)): when iterating over a list named list?

A) The first iterates over each index of the list, while the second iterates over each item.
B) The first iterates over each item of the list, while the second iterates over each index.
C) There is no difference; both iterate over the list items.
D) The first can only be used with lists, while the second can be used with any iterable.

6. (For elaboration) Which of the following is the correct way to double each element in a list nums = [1, 2, 3, 4, 5] using a for loop?
A).
~~~
for n in nums:
    n = n * 2
~~~

B).
~~~
for i in range(len(nums)):
    nums[i] = nums[i] * 2
~~~

C).
for i in nums:
    nums[i] = i * 2

D). Both Option A and Option B are correct

7. (For elaboration - `range()` function)
Which of the following for loops will print all the even numbers from 2 to 10, inclusive?

A) for i in range(2, 11, 2): print(i)
B) for i in range(2, 10): if i % 2 == 0: print(i)
C) for i in range(1, 6): print(i * 2)
D) Both A and C are correct.

8. Compare the following two codes and tell their difference (if any)
~~~
for x in range(10):
    print(x, end=" ")
~~~

~~~
for x in range(0, 10):
    print(x, end=" ")
~~~
A) The first loop prints 0 to 9, the second loop prints 0 to 10

B) The first loop prints 1 to 10, the second loop prints 0 to 9

C) The first loop prints 0 to 9, the second loop prints 1 to 10

D) There is no difference, both loops print 0 to 9

9. Given that `nums = [0, 1, 2, 3, 4, 5]`. Write a for-in loop that doubles each element in the list. (`nums`should be `[0, 2, 4, 6, 8, 10]` after the loop)

10. Write a for-in loop that can print out the number from 2 to 10.

11. (For elaboration) If you are confident with `range()`function, can you write a for-in loop that can print out the `even` number from 2 to 10

<br>

### List Memory Diagram
- Work through the `Example 0` to `Example 3` (110 site > resources > Practice Memory Diagrams > Topic: Lists) Feel Free to bring those exercises to tutoring for help and discussion

# Solutions

### For-In Loop

1. B, C

2. C

3. A

4. C

5. 
B) The first iterates over each item of the list, while the second iterates over each index.


6. B

7. D

8. D

9. One possible answer can be: (Notice that here `for i in nums` and double `i` will not work)
~~~
for i in range(len(nums)):
    nums[i] = nums[i] * 2
~~~

10. One possible answer can be:
~~~
for i in range(2, 11):
    print(i)
~~~

11. One possible answer can be:
~~~
for i in range(2, 11, 2):
    print(i)
~~~
