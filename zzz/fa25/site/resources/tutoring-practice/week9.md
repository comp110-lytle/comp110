---
title: Week 9 Practice
author:
  - Vincent Li
page: resources
template: overview
---

# Concepts Reviewed

Welcome back from Spring Break!

These questions are optional supplements that ideally help you get prepared for the quizzes ahead of time. (Some of them are also designed for elaboration purposes as you can see from the tag. Don't worry them if you just want to get prepared for the quizzes)
<br>

# Questions 

### Big-O Analysis
1. Define Big O notation and explain its significance in algorithm analysis.

2. (For Elaboration) Big O is not the only annotation of efficiency analysis, do you know the other two?

3. 
~~~
for i in range(n):
    for j in range(n):
        print(i, j)
~~~
For this nested loop, determine the Big O notation of its time complexity.

4. Any difference between the following annotations? (Hints: General Rules of Big-O Ignore Constants)
A. O(n) B.O(2n) C.O(n+100) D.O(3n^2)

5. Given that Big O notation ignores constants and lower-order terms, how would you describe the time complexity of the algorithm with a running time of 3n^2 + 2n + 1?

6. Rank the following Big-O Annotation:
A. O(1) B. O(nlogn) C.O(n) D. O(n^2) E.O(n!) F.O(2^n)

### Selection Sort & Insertion Sort:
1. What is the Big-O when using selection sort algorithm?

2. Explain the basic principle behind Selection Sort. How does it determine which element to place in the next position of the sorted portion of the array?

3. Think of a scenario that Insertion Sort perform significantly better than Selection Sort. (Although they share the same time complexity of the worst case)

4. Describe the process of Insertion Sort. How does it integrate each new element into the already sorted portion of the array?

# Solutions:
### Big-O Analysis:

1. `Definition`: Big O notation is a mathematical notation that describes the `upper bound` of an algorithm's running time or space requirement in the `worst-case scenario`.
`Importance`: providing a standardized way to compare the scalability and performance of different algorithms regardless of external differences.

2. There are Big Theta (Θ) and Big Omega (Ω) notations. Big Theta provides an asymptotically tight bound on the growth rate of a function. Big Omega gives a lower bound.

3. O(n^2) for a nested loop.

4. O(n), O(2n), and O(n+100) are all considered O(n) as we ignore the constant for Big-O. However, O(3n^2) is different because it represents a quadratic time complexity.

5. The highest-order term dominates the growth rate and we ignore the constant: O(n^2)

6. Fastest to Slowest:
O(1)
O(n)
O(nlogn)
O(n²)
O(2^n)
O(n!)

### Selection Sort & Insertion Sort:
1. The Big-O of the selection sort algorithm is O(n^2). It requires scanning each element of the array `n` times.

2. Selection Sort works by repeatedly finding the minimum element from the unsorted part and putting it at the beginning. 

3. On nearly sorted arrays or when the array is small. Since it can insert elements in O(1) time if they are already in the correct position.

4. Insertion Sort works by comparing each new element in the unsorted part with the elements in the sorted part, moving each one step to the right until finding the correct position for the new element. Repeated for all elements.
