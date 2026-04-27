---
title: Runtime/Algorithmic Complexity Practice Questions
author:
- Alyssa Lytle
- Benjamin Eldridge
page: lessons
template: overview
---

# Runtime/Algorithmic Complexity Practice Questions

1. True or False: A function with a big-O notation of $O(n)$ will always run faster than a function with a big-O notation of $O(n^2)$ for all inputs.

2. What type of input does Big-O notation consider?

    a. Best Case
    
    b. Worst Case

    c. Average Case

3. True or False: Big-O notation provides a precise measurement of the actual runtime of an algorithm on a specific machine.

4. If an algorithm has a time complexity of $O(1)$, it means its runtime is:

    a. Linear

    b. Constant

    c. Quadratic

    d. Exponential

5. If an algorithm has a time complexity of $O(n)$, it means its runtime is:

    a. Linear

    b. Constant

    c. Quadratic

    d. Exponential

6. If an algorithm has a time complexity of $O(n^2)$, it means its runtime is:

    a. Linear

    b. Constant

    c. Quadratic

    d. Exponential

7. If an algorithm has a time complexity of $O(2^n)$, it means its runtime is:

    a. Linear

    b. Constant

    c. Quadratic

    d. Exponential


8. Which of the following is true about algorithms?

    a. The result of an algorithm is only affected by its inputs.

    b. An algorithm can have side effects which affect its environment.

    c. An algorithm can take an infinite number of steps to complete.

    d. The only effect that an algorithm can have is on its result.


9. A linear search through an unsorted list of length $n$ has what worst-case runtime?
    
    a.$O(1)$

    b.$O(\log n)$

    c.$O(n)$

    d.$O(n^2)$

10. A nested `for` loop where both loops run $n$ times yields which runtime?

    a. $O(n)$

    b. $O(n \log n)$

    c. $O(n^2)$

    d. $O(2^n)$

11. Big-O notation describes how runtime grows as input size $n$:

    a.decreases 

    b.stays fixed 

    c.grows very large 

    d.changes by constant factor

12. Consider the following function:

    ```py
        def foo(outer_input: list[str], inner_input: list[str]) -> None:
            """Nested loop!"""
            for x in outer_input:
                for y in inner_input:
                    print(f"{x} and {y}!")
            return None
    ```

    12.1. Assuming `outer_input` and `inner_input` both have length $n$, what is the big-O runtime of the function `foo`?

    12.2. If `outer_input` has length $n^2$ and `inner_input` has length $n$, what would be the big-O runtime of the function `foo`?

13. Consider the following code snippets:

    ```py
        unc_pid_range: dict[int, bool] = {730000000: False, 730000001: False, ..., 730999999: False}
        prime_numbers: list[int] = [2, 3, 5, 7, ..., 1000000007]

        for pid in unc_pids:
            if pid in prime_numbers:
                unc_pid_range[pid] = True
                print(f"Prime PID found: {pid}!")
    ```

    ```py
        unc_pid_range: list[int] = [730000000, 730000001, ..., 730999999]
        prime_numbers: dict[int, bool] = {2: False, 3: False, 5: False, 7: False, ..., 1000000007: False}

        for pid in unc_pids:
            if pid in prime_numbers:
                prime_numbers[pid] = True
                print(f"Prime PID found: {pid}!")
    ```

    Let $n$ be the size of the `unc_pid_range` lists and let $m$ be the size of both the `prime_numbers` list and dictionary. What are the runtimes of the two code snippets in big-O notation? Which would you choose to use if you cared the most about speed?

<details>
<summary>SOLUTIONS</summary>

1. This is False. A function with big-O notation of $O(n)$ will theoretically run faster than a function with a big-O notation of $O(n^2)$ on a *worst case* input.

2. Worst Case.

3. False.

4. Constant

5. Linear

6. Quadratic

7. Exponential

8. The answer is b, since algorithms are a finite series of steps (eliminating c) and can be affected by and have an effect on their environment (eliminating a and d, and showing that b is true).

9. $O(n)$

10. $O(n^2)$

11. grows very large

12. 
    12.1. $O(n^2)$

    12.2. $O(n^3)$


13. The first code snippet runs in time $O(m \cdot n)$ and the second runs in time $O(n)$. This is because the lookup time (the `in` operator) takes constant time on a dictionary and linear time on a list, so in the first snippet you do an $O(m)$ operation $n$ times so $O(m \cdot n), but in the second you do an $O(1)$ operation $n$ times so $O(n)$. Thus if you care about speed the most you would use the second method.
</details>