---
title: Recursion Overview
author:
- Tori Hoffmann
page: resource
template: overview
---

### Thinking About Recursion 

A recursive function is a function that calls itself. Recursion is extrememly useful in CS when working with recursively defined data structures, such as lists, and is commonly used in higher level CS courses and in industry. It can be a pretty tricky topic to wrap your head around but once you understand the basics and put it into practice it can make your life as a coder much easier!

When we want to write a recursive function, we need a base case and a recursive case:  

- Our recursive case is where we call our function. 
- In the base case, we do NOT call our function.

When we enter the recursive case of a function, we know we're going to be calling the function again. In order to prevent this from happening without end, we need a way to make it so that eventually we'll enter the base case of our function. To do this, we must change the arguments we provide when we call the function in our recursive case.

### Rules for Recursive Functions 
(1) Test for a base case!
    - The base case is the ending condition for a recursive function (it tells us when to stop).
    - Not including the base case could give us infinite recursion, which would send a stack overflow error our way!

(2) Recursive case
    - Have the function call itself! This is what makes it a recursive function.

(3) Change at least one argument when recurring
    - We need to change the arguments so they get closer and closer to the base case with each step of recursion.
    - If we never change the arguments we call the function with, we'll end up in an endless cycle of calling the function.


## Examples

### Factorial Function

Let's test your knowledge. Can you identify the base case and recursive case for the factorial function below?

~~~ {.python }
    def factorial(n: int):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)
~~~

The recursive case is where the function calls itself. In this case, we recur in the else block when we __return n * factorial(n-1)__.

The base case is what terminates the recursion. In our factorial function, the base case occurs when __n == 0__. By returning 1 instead of a call to factorial, the recursion halts and the result, n!, is returned.

Still a little confused on what's going on? Try drawing an environment diagram for the function call __factorial(4)__ to see what this function looks like in action! 

### Addition Function

Let's try writting a recursive function that sums 2 numbers! Our function will take in a number, n, and how much we want to add to it, m. Calling this function might look like add(2, 3).

So, how do go about thinking recursively? One good starting point is asking yourself, "what is one step I can repeat over and over again to achieve the result I desire?" In the case of addition, adding 1 to n, m times, would result in the sum of m and n. That's the recursive case right there!

Remember that we must change an argument each time we recur in order to get to our base case. When should we reach our base case? When we have successfully added 1 to n, m times. One way we can keep track of this progress is to decrease the value of m every time we hit our recursive case. Thus, when m = 0, we know that we are done recurring! 

We have figured out that we should hit our base case when m = 0. But, what do we do when that happens? Well, when we reach our base case we assume that we are done recurring. Thus, we are trusting that m and n have been summed and we no longer want to add to our return value. So, in this case we just return 0! 
 
 - (Note: Remember every returned value is being added up, essentially we are adding 0 to our total sum when we reach base case)

 - Following this logic, what might be a base case when working with multiplication? Would multiplying our value by 0 be a good idea?

And there we have it! We have figured out how to write a recursive funtion that adds two numbers. This process is a tricky to wrap your head around at first, but stick to the 3 rules of recursive functions and you're golden!

~~~ {.python }
    def add(n: int, m: int):
        if m <= n:
            return 0
        else:
            return 1 + add(n, m - 1)
~~~

Note: In the function our base case actually ends up occuring when __m <= 0__. Can you think of why this might be? Why might using __m == 0__ cause problems? What would happen if we called then function with a negative value for m?

Again, if you are feeling lost, try creating an environment diagram for the call add(3, 2) and trace what is happening.