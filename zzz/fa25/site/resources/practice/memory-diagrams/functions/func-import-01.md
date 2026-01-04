---
title: Practice Memory Diagram
author:
- Created by Lynn Lee
- Reviewed by Olivia Xiao
- Published by Alyssa Lytle
page: lessons
template: overview
---

# Snippet

<pre>
<code class="python">   def subtraction(x: int) -> int:
        if not x == 10 or x > 8:
            while x > 7: 
                x -= 1
        return x

    def to_ten(y: int) -> int:
        while y < 10:
            y += 2
        return y

    def main():
        num1: int = 2
        num1 = to_ten(num1)
        num1 = subtraction(num1)
        print(f"The number is {num1}")

    main()
</code></pre>

# Solution

*(Coming Soon)*

<!-- <img class="img-fluid" src="/static/practice-mem-diagrams/func-import-01-sol.jpg" alt=""/> -->

<!-- 
<img class="img-fluid" src="/static/assets/f23/func-import-01-sol.png" alt="The Memory Diagram has three columns from the left to the right, including the
Stack, the Heap and the Output.
The Stack has 4 frames in the following order from top to bottom including,
Globals, main, to_ten, subtraction.
The Globals frame has 3 variables including subtraction, to_ten, and main.
● subtraction has id 0, it is function on the heap, from lines 1-5
● to_ten has id 1, it is a function on the heap from lines 7-10
● main has id 2, it is a function on the heap from lines 12-16
The main frame has 3 items, including num1, RA, and RV.
● num1 is defined as 2 initially, but changes to 10 after the frame to_ten
finishes, and changes to 7 after the frame subtraction finishes
● RA is defined at line 18
● RV is none
The to_ten frame has 3 items, including y, RA, and RV.
● y is initially 2, but changes to 4, then 6, then 8, then 10.
● RA is defined at line 14
● RV is 10
The subtraction frame has 3 items, including x, RA, and RV.
● x is initially 10, but changes to 9, then 8, then 7.
● RA is defined at line 15
● RV is 7
The Heap includes 3 function objects
The Output includes the phrase: “The number is 7”"  /> --->

*Image Description* The Memory Diagram has three columns from the left to the right, including the
Stack, the Heap and the Output.

The Stack has 4 frames in the following order from top to bottom including,
Globals, main, to_ten, subtraction.

The Globals frame has 3 variables including subtraction, to_ten, and main.

* subtraction has id 0, it is function on the heap, from lines 1-5
* to_ten has id 1, it is a function on the heap from lines 7-10
* main has id 2, it is a function on the heap from lines 12-16
The main frame has 3 items, including num1, RA, and RV.
* num1 is defined as 2 initially, but changes to 10 after the frame to_ten
finishes, and changes to 7 after the frame subtraction finishes
* RA is defined at line 18
* RV is none

The to_ten frame has 3 items, including y, RA, and RV.

* y is initially 2, but changes to 4, then 6, then 8, then 10.
* RA is defined at line 14
* RV is 10

The subtraction frame has 3 items, including x, RA, and RV.

* x is initially 10, but changes to 9, then 8, then 7.
* RA is defined at line 15
* RV is 7

The Heap includes 3 function objects
The Output includes the phrase: “The number is 7”
