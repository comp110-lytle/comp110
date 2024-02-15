---
title: Week 2 Practice
author:
  - Vincent Li
page: resources
template: overview
---

# Concepts Reviewed

These questions are optional supplements that ideally help you get prepared for the quizzes ahead of time. Before working through these practice questions, you should get familiar with the concepts covered in the lessons of the forth week.

<br>

# Questions
These questions might not be in the same format as quizzes. Don't hesitate to bring them to the Tutoring section for help.

### Lists
1. What happens when you assign one list to another (e.g., list1 = list2) and then modify one of the lists? Say we now modified the values of list2, will values of list 1 also get changed?

2. 
~~~
list1 = [1, 2, 3, 4]
list2 = list1
list2.append(5)
print(list1)
~~~
Consider the above codes, what would be printed out as the output?
A) [1, 2, 3, 4, 5] B) [1, 2, 3, 4] C) [5, 4, 3, 2, 1] D) Error

3. Where should we put a newly created list in Memory Diagram? 

4. Recall the Chapter when we learn `String`, how to use index to access the last item within a list without calling the function `len()`?

5. Function writing relates with list:
5.1 Could you write a function that will taking a list of `int` and return the average of this list of `int`?

6. Identify the usage and difference of `pop()` and `append()` in list.

7. In Python, which method can be used to combine two lists into a single list?

A) combine()
B) append()
C) extend()
D) join()

8. Identify the following statements regarding list slicing are True of False:
1. list[::2] returns items at even indices only.
2. list[::-1] reverses the list.
3. list[1:3] returns the first three items.
4. list[:3] returns the last three items.

9. 
~~~
a = [1, 2, 3]
b = a * 2
b[0] = 5
print(a)
print(b)
~~~
Consider the above codes, what would be the outputs of last two print() function?

10. Say I have a new `item` that, instead of adding it to the end of the list, but at the `specific index`. Which build-in function would be the correct one to use for this purpose?

11. Identify the following statements are True of False:

1. Lists can contain elements of different data types.
2. Lists are mutable.
3. The + operator can be used to append elements to a list.
4. Lists can be nested within other lists.

12. 
~~~
my_list = ['Python', 'is', 'awesome', 'is', '110', 'is','cool']
~~~
Write a one line code that can return the index of `110` in this list.

13. Continue on 12: 
~~~
print(my_list.index('is'))
~~~
What would be the output of this line of code based on the `my_list` from Q12?
A) 1
B) 2
C) 3
D) [1, 3]



# Solutions

### Lists
1. Yes, it will get changed. In Python, list is a reference data type. So assigning list1 = list2 means they are now referring to the same list. 

2. A

3. Heap

4. list[-1]

6. The append() method adds a single element to the end of the list. Whereas the The pop() method removes and returns the last element of the list. If an index is given, it removes and returns the element at that index.

7. C

8. 
8.1 True
8.2 True
8.3 False
8.4 False

9. [1, 2, 3] and [5, 2, 3, 5, 2, 3]

10. .insert()

11. 
11.1 True
11.2 True
11.3 False
11.4 True

12. print(my_list.index('110'))

13. A
