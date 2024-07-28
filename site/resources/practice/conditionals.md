---
title: Conditionals Questions
author:
- Alyssa Lytle
- Megan Zhang
- David Karash
page: lessons
template: overview
---

# Questions

## Conceptual

1. Every `if` statement must be followed by a paired `else` branch. (T/F)
2. Lines contained in an `else` branch in Python do not have to be indented. (T/F)
3. You can name a variable `else` in your program without Python confusing your variable's name and the `else` keyword. (If you are unsure, this is a good one to try yourself!) (T/F)

4. All subquestions of this problem will refer to this code snippet:

        x: int = int(input("Pick a number: "))
        y: int = 10
        z: int = 2
        x = x - 1
        if x < 10:
            print("A")
        else:
            if (x % z) == 0:
                print ("B")
        if x == (y + z):
            print("C")
        else: 
            print("D")

For the following subquestions, answer with a valid input value for `x` that would cause the given letter to print. It is OK for your input to cause other letters to print as well.
If there is no such value, write "Unreachable".

4.1 `A`

4.2 `B`

4.3 `C`

4.4 `D`

Now, answer with a valid input value for `x` that
would cause the *exact* given letter(s) to print (no other letters). 
If there is no such value, write "Unreachable".  
4.5 

`A` <br>
`C`

4.6 

`B` <br>
`C`


4.7 

`C`


4.8 

`D`


[solutions](#conceptual-solutions)

# Solutions

## Conceptual Solutions

1. F
2. F
3. F

4.
    
    4.1 Any value < 11

    4.2 Any value >= 11 and odd. (Since `x % z == 0` must be True and `z` is 2, this means `x - 1` must be even.)

    4.3 13

    4.4 Any value != 13

    4.5 Unreachable

    4.6 13

    4.7 Unreachable

    4.8 Any value >= 11 and even