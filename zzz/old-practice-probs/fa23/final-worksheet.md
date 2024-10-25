---
title: Final Exam Practice
author:
- David Karash
- Megan Zhang
- Alyssa Byrnes
page: lessons
template: overview
---

The final exam only includes one new concept: recursion! We will be adding practice recursive memory diagrams to the [practice memory diagram page](/resources/practice/MemDiagrams.html) soon! You also should make sure you are more comfortable with nested data structures (e.g. lists of dicts), as that's what we worked on with DataWrangling!

Otherwise, to practice, you should review the practice problems for the previous quizzes:

* [QZ01](/resources/practice/fa23/qz01.html)
* [QZ02](/resources/practice/fa23/qz02.html)
* [QZ03](/resources/practice/fa23/qz03.html)

Additionally, you will be expected to do more advanced function writing for the final, so we've included more function writing practice problems below.

# Questions

This review is not comprehensive of all content that will be on the final exam, but rather provides a few extra practice questions.  Previous quizzes/practice questions are also valuable in reviewing for the final exam.  Lecture videos are another valuable resource.

Solutions for each problem can be found at the bottom of this page. Keep in mind that there may be multiple solutions to each problem.

## Function Writing



1. Write a function called `free_biscuits`. Given a dictionary with `str` keys (representing basketball games) and `list[int]` values (representing points scored by players), `free_biscuits` should return a new dictionary of type `dict[str, bool]` that maps each game to a boolean value for free biscuits. (`True` if the points add up to 100+, `False` if otherwise)  
Example: `free_biscuits({ “UNCvsDuke”: [38, 20, 42] , “UNCvsState”: [9, 51, 16, 23] })` should return `{ “UNCvsDuke”: True, “UNCvsState”: False }`.

2. Write a function called `max_key`. Given a dictionary with `str` keys  and `list[int]` values, return a `str` with the name of the key whose list has the highest *sum* of values.
Example: `max_key({"a": [1,2,3], "b": [4,5,6]})` should return `"b"` because the sum of `a`'s elements is 1 + 2 + 3 = 6 and the sum of `b`'s elements is 4 + 5 + 6 = 15, and 15 > 6.

3. Write a function called `multiples`. Given a `list[int]`, `multiples` should return a `list[bool]` that tells whether each `int` value is a multiple of the previous value.  For the first number in the list, you should wrap around the list and compare this `int` to the last number in the list.  (Hint: `x` is a multiple of `y` if and only if `x % y` is `0`.)
Example: `multiples([2, 3, 4, 8, 16, 2, 4, 2])` should return `[True, False, False, True, True, False, True, False]`.

4. Write a function called `merge_lists`. Given a `list[str]` and a `list[int]`, `merge_lists` should return a `dict[str, int]` that maps each item in the first list to its corresponding item in the second (based on index).  If the lists are not the same size, the function should return an empty dictionary.  
Example: `merge_lists([“blue”, “yellow”, “red”], [5, 2, 4])` should return `{"blue": 5, "yellow": 2, "red": 4}`. 

5. Write a function called `reverse_multiply`. Given a `list[int]`, `reverse_multiply` should return a `list[int]` with the values from the original list doubled and in reverse order.  
Example: `reverse_multiply([1, 2, 3])` should return `[6, 4, 2]`.

<!-- ## Class Writing

6. Create a class called `HotCocoa` with the following specifications:
    a. Each `HotCocoa` object has a `bool` attribute called `has_whip`, a `str` attribute called `flavor`, and two `int` attributes called `marshmallow_count` and `sweetness`.
    b. The class should have a constructor that takes in and sets up each of its attribute’s values.
    c. Write a method called `mallow_adder` that takes in an `int` called `mallows`, increases the `marshmallow_count` by that amount, and increases the `sweetness` by that amount times 2.
    d. Write a method called `calorie_count` that returns a `float`. If the `flavor` of the `HotCocoa` is “vanilla” or “peppermint”, increase the calorie count by 30, otherwise increase it by 20. If the `HotCocoa` has whipped cream (`has_whip` is `True`), increase the calorie count by 100. Finally, increase the calorie count by half the number of marshmallows. The calorie count should be calculated and returned when this method is called.  


7. Create a class called `TimeSpent` with the following specifications:
    a. Each `TimeSpent` object has a `str` attribute called `name`, a `str` attribute called `purpose`, and an `int` attribute called `minutes`.
    b. The class should have a constructor that takes in and sets up each of its attribute’s values.
    c. Write a method called `add_time` that takes in an `int` and increases the `minutes` attribute by this amount. The method should return `None`.
    d. Write a method called `reset` that resets the amount of time that is stored in the `minutes` attribute.  The method should return the amount that was stored in `minutes`. 
    e. Write a method called `report` that prints a line reporting information about the current `TimeSpent` object.  Suppose a `TimeSpent` object has `name` = `“Ariana”`, `purpose` = `“screen time”`, and `minutes` = `130`.  The report method should print: `“Ariana has spent 2 hours and 10 minutes on screen time.”`
 -->


# Solutions

## Function Writing



1. 

```
    def free_biscuits(input: dict[str, list[int]]) -> dict[str, bool]:
        """Check each game to see if we get free biscuits."""
        result: dict[str, bool] = {}
        # loop over each key in my input dictionary
        for key in input:
            # for each element of the dictionary, sum up its values
            list_to_sum: list[int] = input[key]
            sum: int = 0
            # loop through list and add each value to sum
            for element in list_to_sum:
                sum += element
            # if sum >= 100, store in result under key "key" with value True
            if sum >= 100:
                result[key] = True
            else: # if not, store as False
                result[key] = False
        return result
```

2. 

```
    def max_key(input: dict[str, int]) -> str:
        # Create variables to store max key and max val sum
        max_key: str = ""
        max_val_sum: int = 0
        # Loop through each key of the dictionary
        for key in input:
            # Sum up the values of that key's corresponding list
            val_sum: int = 0
            for value in input[key]:
                val_sum += value
            # If the sum is the max so far, update the max_key and max_val_sum
            if val_sum > max_val_sum:
                max_val_sum = val_sum
                max_key = key 
        return max_key
```

3. 

One Solution:

```
    def multiples(input: list[int]) -> list[bool]:
        """Return a mapping of each element for whether or not it's a multiple of the previous element"""
        # initialize the output
        output: list[bool] = []
        # handle the "wrap around" case to check if the first element is a multiple of the last element
        if input[0] % input[len(input) - 1] == 0: # If first element is a multiple of last
            output.append(True) # Append True
        else:
            output.append(False) # Otherwise, append False
        # now, handle the rest of the list 
        # for idx values 1 to len(input) - 1...
        idx: int = 1
        while idx < len(input):
            # ...we want to see if val at idx is a multiple of val at idx-1
            if input[idx] % input[idx-1] == 0:
                output.append(True)
            else:
                output.append(False)
            idx += 1
        return output
```

Another Solution:

```
    def multiples(input: list[int]) -> list[bool]:
        """Return a mapping of each element for whether or not it's a multiple of the previous element"""
        # initialize the output
        output: list[bool] = []
        # handle the "wrap around" case to check if the first element is a multiple of the last element
        output.append(input[0] % input[len(input) - 1] == 0)
        # now, handle the rest of the list 
        # for idx values 1 to len(input) - 1...
        idx: int = 1
        while idx < len(input):
            # ...we want to see if val at idx is a multiple of val at idx-1
            output.append(input[idx] % input[idx-1] == 0)
            idx += 1
        return output
```

4. ![](/static/practice_worksheets/fa21/final-solution4.png)

5. ![](/static/practice_worksheets/fa21/final-solution1.png)


<!-- 
## Class Writing

6. ![](/static/practice_worksheets/fa21/final-solution5.png)

7. ![](/static/practice_worksheets/fa21/final-solution6.png) -->

