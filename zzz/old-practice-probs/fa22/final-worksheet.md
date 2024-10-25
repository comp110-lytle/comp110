---
title: Final Exam Practice
author:
- David Karash
- Megan Zhang
page: lessons
template: overview
---
<!--
Note: this is a copy of the final worksheet from resources/practice/fa21 with some added questions for this sp22's content.
-->
# Questions

This review is not comprehensive of all content that will be on the final exam, but rather provides a few extra practice questions and some questions on concepts after quiz 3.  Previous quizzes/practice questions are also valuable in reviewing for the final exam.  Lecture videos are another valuable resource.

Solutions for each problem can be found at the bottom of this page. Keep in mind that there may be multiple solutions to each problem.

## Function Writing

1. Write a function called `reverse_multiply`. Given a `list[int]`, `reverse_multiply` should return a `list[int]` with the values from the original list doubled and in reverse order.  
Example: `reverse_multiply([1, 2, 3])` should return `[6, 4, 2]`.

2. Write a function called `free_biscuits`. Given a dictionary with `str` keys (representing basketball games) and `list[int]` values (representing points scored by players), `free_biscuits` should return a new dictionary of type `dict[str, bool]` that maps each game to a boolean value for free biscuits. (`True` if the points add up to 100+, `False` if otherwise)  
Example: `free_biscuits({ “UNCvsDuke”: [38, 20, 42] , “UNCvsState”: [9, 51, 16, 23] })` should return `{ “UNCvsDuke”: True, “UNCvsState”: False }`.

3. Write a function called `multiples`. Given a `list[int]`, `multiples` should return a `list[bool]` that tells whether each `int` value is a multiple of the previous value.  For the first number in the list, you should wrap around the list and compare this `int` to the last number in the list.  
Example: `multiples([2, 3, 4, 8, 16, 2, 4, 2])` should return `[True, False, False, True, True, False, True, False]`.

4. Write a function called `merge_lists`. Given a `list[str]` and a `list[int]`, `merge_lists` should return a `dict[str, int]` that maps each item in the first list to its corresponding item in the second (based on index).  If the lists are not the same size, the function should return an empty dictionary.  
Example: `merge_lists([“blue”, “yellow”, “red”], [5, 2, 4])` should return `{"blue": 5, "yellow": 2, "red": 4}`. 

5. Write a function named `reverse_string` that reverses the characters of a string without using the `reverse` built-in function.

## Class Writing

5. Create a class called `HotCocoa` with the following specifications:
    a. Each `HotCocoa` object has a `bool` attribute called `has_whip`, a `str` attribute called `flavor`, and two `int` attributes called `marshmallow_count` and `sweetness`.
    b. The class should have a constructor that takes in and sets up each of its attribute’s values.
    c. Write a method called `mallow_adder` that takes in an `int` called `mallows`, increases the `marshmallow_count` by that amount, and increases the `sweetness` by that amount times 2.
    d. Write a method called `calorie_count` that returns a `float`. If the `flavor` of the `HotCocoa` is “vanilla” or “peppermint”, increase the calorie count by 30, otherwise increase it by 20. If the `HotCocoa` has whipped cream (`has_whip` is `True`), increase the calorie count by 100. Finally, increase the calorie count by half the number of marshmallows. The calorie count should be calculated and returned when this method is called.  


6. Create a class called `TimeSpent` with the following specifications:
    a. Each `TimeSpent` object has a `str` attribute called `name`, a `str` attribute called `purpose`, and an `int` attribute called `minutes`.
    b. The class should have a constructor that takes in and sets up each of its attribute’s values.
    c. Write a method called `add_time` that takes in an `int` and increases the `minutes` attribute by this amount. The method should return `None`.
    d. Write a method called `reset` that resets the amount of time that is stored in the `minutes` attribute.  The method should return the amount that was stored in `minutes`. 
    e. Write a method called `report` that prints a line reporting information about the current `TimeSpent` object.  Suppose a `TimeSpent` object has `name` = `“Ariana”`, `purpose` = `“screen time”`, and `minutes` = `130`.  The report method should print: `“Ariana has spent 2 hours and 10 minutes on screen time.”`

## Recursion

7. What is it that makes a function/structure recursive?
8. A recursive function must have a recursive case. (T/F)
9. A recursive function may define multiple recursive cases. (T/F)
10. What happens if a recursive function does not make progress toward a base case?
11. Write a recursive factorial function.  The factorial of a positive integer is the product of that integer with all of the positive integers less than it.  `!n` is used to denote the factorial of a positive integer `n`. (`4! = 4*3*2*1 = 24`)  Ex: `factorial(4)` should return `24`, `factorial(5)` should return `120`, `factorial(1)` should return `1`.
12. Diagram the following call to `factorial` using the solution provided below.
13. EXTRA PRACTICE:  Diagram calls to functions from EX10: Linked List Utils.  For obvious reasons, we cannot provide solutions to these, but having practice diagramming recursive structures as well as recursive functions such as `factorial` is great practice for the final!  The examples in lecture videos can be helpful if this is difficult, and as always office hours is a great resource if you struggle with this.

# Solutions

## Function Writing

1. ![](/static/practice_worksheets/fa21/final-solution1.png)

2. ![](/static/practice_worksheets/fa21/final-solution2.png)

3. ![](/static/practice_worksheets/fa21/final-solution3.png)

4. ![](/static/practice_worksheets/fa21/final-solution4.png)

5.

~~~
def reverse_string(input: str) -> str:
    """Reverse the characters of a string without using reverse."""
    result: str = ""
    i: int = len(input) - 1
    while i >= 0:
        result += input[i]
        i -= 1
    return result
~~~

## Class Writing

5. ![](/static/practice_worksheets/fa21/final-solution5.png)

6. ![](/static/practice_worksheets/fa21/final-solution6.png)

## Recursion

7. A recursive function is a function that calls itself, and recursive structures are defined in terms of themselves.
8. T
9. T
10. If a recursive function does not make progress toward a base case, it will result in infinite recursion and python will stop its execution with a RecursionError.
11. ![](/static/practice_worksheets/sp22/final-wkst-solution11.png)
12. ![](/static/practice_worksheets/sp22/final-wkst-solution12.png)