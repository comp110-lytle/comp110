---
title: Final Exam Practice
author:
- David Karash
- Megan Zhang
- Alyssa Lytle
page: lessons
template: overview
---
<!--
Note: this is a modified copy of the final worksheet from resources/practice/fa21.
-->
# Reviewing for the Final

This review is not comprehensive of all content that will be on the final exam, but rather provides a few extra practice questions.  All concepts (except magic methods) have been covered on previous quizzes! 

The best resources for studying are:

- Your previous quizzes
- [Practice Memory Diagrams](/resources/practice/MemDiagrams.html)
- LS assignments
- Previous Quiz Review Sheets
    - [QZ00](/resources/practice/sp24/qz00.html)
    - [QZ01](/resources/practice/sp24/qz01.html)
    - [QZ02](/resources/practice/sp24/qz02.html)
    - [QZ03](/resources/practice/sp24/qz03.html)
    - [QZ04](/resources/practice/sp24/qz04.html)


# Class and Function Writing



## Function Writing

1. Write a function called `free_biscuits`. Given a dictionary with `str` keys (representing basketball games) and `list[int]` values (representing points scored by players), `free_biscuits` should return a new dictionary of type `dict[str, bool]` that maps each game to a boolean value for free biscuits. (`True` if the points add up to 100+, `False` if otherwise)  
Example: `free_biscuits({ “UNCvsDuke”: [38, 20, 42] , “UNCvsState”: [9, 51, 16, 23] })` should return `{ “UNCvsDuke”: True, “UNCvsState”: False }`.

2. Write a function called `max_key`. Given a dictionary with `str` keys  and `list[int]` values, return a `str` with the name of the key whose list has the highest *sum* of values.
Example: `max_key({"a": [1,2,3], "b": [4,5,6]})` should return `"b"` because the sum of `a`'s elements is 1 + 2 + 3 = 6 and the sum of `b`'s elements is 4 + 5 + 6 = 15, and 15 > 6.

<!-- 3. Write a function called `multiples`. Given a `list[int]`, `multiples` should return a `list[bool]` that tells whether each `int` value is a multiple of the previous value.  For the first number in the list, you should wrap around the list and compare this `int` to the last number in the list.  
Example: `multiples([2, 3, 4, 8, 16, 2, 4, 2])` should return `[True, False, False, True, True, False, True, False]`.

4. Write a function called `merge_lists`. Given a `list[str]` and a `list[int]`, `merge_lists` should return a `dict[str, int]` that maps each item in the first list to its corresponding item in the second (based on index).  If the lists are not the same size, the function should return an empty dictionary.  
Example: `merge_lists([“blue”, “yellow”, “red”], [5, 2, 4])` should return `{"blue": 5, "yellow": 2, "red": 4}`.  -->

3. Write a function called `reverse_multiply`. Given a `list[int]`, `reverse_multiply` should return a `list[int]` with the values from the original list doubled and in reverse order.  
Example: `reverse_multiply([1, 2, 3])` should return `[6, 4, 2]`.

[Solutions](#function-writing-solutions)

## Class Writing

1. Create a class called `HotCocoa` with the following specifications:
    a. Each `HotCocoa` object has a `bool` attribute called `has_whip`, a `str` attribute called `flavor`, and two `int` attributes called `marshmallow_count` and `sweetness`.
    b. The class should have a constructor that takes in and sets up each of its attribute’s values.
    c. Write a method called `mallow_adder` that takes in an `int` called `mallows`, increases the `marshmallow_count` by that amount, and increases the `sweetness` by that amount times 2.
    d. Write a `__str__` magic method that displays the details of the hot cocoa order mimicing the following:
        - If it has whipped cream:
            `"A <flavor> cocoa with whip, <marshmallow_count> marshmallows, and level <sweetness> sweetness.`
        - If it doesn't have whipped cream:
            `"A <flavor> cocoa without whip, <marshmallow_count> marshmallows, and level <sweetness> sweetness.`
    e. Write an `order_cost` *function* that takes as input a `list` of `HotCocoa` objects to represent an order and returns the total cost of the order. A `HotCocoa` with whip is $2.50 and without whip is $2.00.

2. Create a class called `TimeSpent` with the following specifications:
    a. Each `TimeSpent` object has a `str` attribute called `name`, a `str` attribute called `purpose`, and an `int` attribute called `minutes`.
    b. The class should have a constructor that takes in and sets up each of its attribute’s values.
    c. Write a method called `add_time` that takes in an `int` and increases the `minutes` attribute by this amount. The method should return `None`.
    d. Write an `__add__` magic method that takes in an `int` called `added_minutes` and returns a new `TimeSpent` object with the same attribute values except that `minutes` is increased by `added_minutes`.
    e. Write a method called `reset` that resets the amount of time that is stored in the `minutes` attribute.  The method should also return the amount that was stored in `minutes`. 
    f. Write a `__str__` magic method returns a line reporting information about the current `TimeSpent` object.  Suppose a `TimeSpent` object has `name` = `“Ariana”`, `purpose` = `“screen time”`, and `minutes` = `130`.  The method should return: `“Ariana has spent 2 hours and 10 minutes on screen time.”`
    g. Write a *function* called `most_by_purpose` that takes as input a `list` of `TimeSpent` objects and a `str` to represent a purpose, and returns the name of the person who spent the most time doing that specific activity. 
    - Example usage: 
    <pre>
    <div class="terminal">
    >>> a: TimeSpent = TimeSpent("Alyssa", "studying", 5)
    >>> b: TimeSpent = TimeSpent("Alyssa", "doom scrolling", 100)
    >>> c: TimeSpent = TimeSpent("Vrinda", "studying", 200)
    >>> most_by_purpose([a, b, c], "studying")
    'Vrinda'
    </div>
    </pre>

    

[Solutions](#class-writing-solutions)

# Solutions

## Function Writing Solutions

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

```
    def reverse_multiply(vals: list[int]) -> list[int]:
        """Reverse the list and double all elements."""
        # iterate through the list backwards
        idx: int = len(vals) - 1 # index of last element
        new_vals: list[int] = []
        while idx >= 0:
            new_vals.append(vals[idx] * 2)
            idx -= 1
        return new_vals
```

```
    def reverse_multiply(vals: list[int]) -> list[int]:
        """Reverse the list and double all elements."""
        # iterate through the list forwards, but get index of the "opposite" element 
        idx: int = 0 # index of last element
        new_vals: list[int] = []
        while idx < len(vals):
            idx_of_opposite: int = len(vals) - 1 - idx
            new_vals.append(vals[idx_of_opposite] * 2)
            idx += 1
        return new_vals
```

## Class Writing Solutions

1.
```
    class HotCocoa:
        
        has_whip: bool
        flavor: str
        marshmallow_count: int
        sweetness: int
        
        def __init__(self, whip: bool, flavor: str, marshmallows: int, sweetness: int):
            self.has_whip = whip
            self.flavor = flavor
            self.marshmallow_count = marshmallows
            self.sweetness = sweetness
        
        def mallow_adder(self, mallows: int) -> None:
            self.marshmallow_count += mallows
            self.sweetness += (mallows * 2)
            
        def __str__(self) -> str:
            if self.has_whip:
                return f"A {self.flavor} cocoa with whip, {self.marshmallow_count} marshmallows, and level {self.sweetness} sweetness."
            else:
                return f"A {self.flavor} cocoa without whip, {self.marshmallow_count} marshmallows, and level {self.sweetness} sweetness."
            
    def order_cost(order: list[HotCocoa]) -> float:
        cost: float = 0.0
        for cocoa in order:
            if cocoa.has_whip:
                cost += 2.50
            else:
                cost += 2.00
        return cost
```

2. 
```
    class TimeSpent:
        
        name: str
        purpose: str
        minutes: int
        
        def __init__(self, name: str, purpose: str, minutes: int):
            self.name = name
            self.purpose = purpose
            self.minutes = minutes

        def add_time(self, increase: int) -> None:
            self.minutes += increase
        
        def __add__(self, added_minutes: int) -> TimeSpent:
            return TimeSpent(self.name, self.purpose, self.minutes + added_minutes)
        
        def reset(self) -> None:
            old_value: int = self.minutes
            self.minutes = 0
            return old_value
        
        def __str__(self) -> str:
            minutes: int = self.time % 60
            hours: int = (self.time - minutes)/ 60
            return f"{self.name} has spent {hours} hours and {minutes} minutes on screen time."

    def most_by_purpose(times: list[TimeSpent], activity: str) -> str:
        max_time: int = 0
        max_name: str = ""
        for elem in times:
            if (elem.purpose == activity) and (elem.minutes > max_time):
                max_time = elem.minutes
                max_name = elem.name
        return max_name
```