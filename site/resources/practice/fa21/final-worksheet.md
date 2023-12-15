---
title: Final Exam Practice
author:
- Megan Zhang
- David Karash
page: lessons
template: overview
---

# Questions

This practice is intended to help you become more comfortable with code writing style questions, though the final will have other types of questions as well.

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

# Solutions

## Function Writing

1. ![](/static/practice_worksheets/fa21/final-solution1.png)

2. ![](/static/practice_worksheets/fa21/final-solution2.png)

3. ![](/static/practice_worksheets/fa21/final-solution3.png)

4. ![](/static/practice_worksheets/fa21/final-solution4.png)

## Class Writing

5. ![](/static/practice_worksheets/fa21/final-solution5.png)

6. ![](/static/practice_worksheets/fa21/final-solution6.png)