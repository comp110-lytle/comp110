---
title: Function Writing Practice Problems
author:
- Alyssa Lytle
- Megan Zhang
- David Karash
- Coralee Vickers
- Carolyn Pierce
page: lessons
template: overview
---

# Questions

## Lists

### `multiples`

 Write a function called `multiples`. Given a `list[int]`, `multiples` should return a `list[bool]` that tells whether each `int` value is a multiple of the previous value.  For the first number in the list, you should wrap around the list and compare this `int` to the last number in the list.  
Example: `multiples([2, 3, 4, 8, 16, 2, 4, 2])` should return `[True, False, False, True, True, False, True, False]`.



### `reverse_multiply`

Write a function called `reverse_multiply`. Given a `list[int]`, `reverse_multiply` should return a `list[int]` with the values from the original list doubled and in reverse order.  
Example: `reverse_multiply([1, 2, 3])` should return `[6, 4, 2]`.

[Solution](#function-writing-solutions)

## Dictionaries

### `value_exists`

* The function name is value\_exists and is called with a `dict[str,int]` and an `int` as an argument.
* The function should return a `bool`.
* The function should return `True` if the `int` exists as a value in the dictionary, and `False` otherwise.
* The function should not mutate (modify) the input dict.
* Explicitly type variables, parameters, and return types. 
* The following REPL examples demonstrate expected functionality of your `value\_exists` function:

<pre>
<div class="terminal">
>>> test_dict: dict[str,int] = {"a": 2, "b": 4, "c": 7, "d": 1}
>>> test_val: int = 4
>>> value_exists(test_dict, test_val)
True
>>> value_exists(test_dict, 5)
False
</div>
</pre>

[Solution](#value_exists-solution)

### `plus_or_minus_n` 

* The function name is `plus_or_minus_n` and is called with `inp: dict[str,int]` and `n: int` as an argument.
* The function should return `None`. It instead *mutates* the input dictionary `inp`.
* The function should check if each *value* in `inp` is even or odd. If it is even, add `n` to that value. If it is odd, subtract `n`.
* Explicitly type variables, parameters, and return types. 
* The following REPL examples demonstrate expected functionality of your function:

[Solution](#plus_or_minus_n-solution)

### `free_biscuits`

Write a function called `free_biscuits`. Given a dictionary with `str` keys (representing basketball games) and `list[int]` values (representing points scored by players), `free_biscuits` should return a new dictionary of type `dict[str, bool]` that maps each game to a boolean value for free biscuits. (`True` if the points add up to 100+, `False` if otherwise)  
Example: `free_biscuits({ “UNCvsDuke”: [38, 20, 42] , “UNCvsState”: [9, 51, 16, 23] })` should return `{ “UNCvsDuke”: True, “UNCvsState”: False }`.

<pre>
<div class="terminal">
>>> test_dict: dict[str,int] = {"a": 2, "b": 4, "c": 7, "d": 1}
>>> test_val: int = 4
>>> plus_or_minus_n(test_dict, test_val)
>>> test_dict
{"a": 6, "b": 8, "c": 3, "d": -3}
</div>
</pre>

[Solution](#free_biscuits-solution)

### `max_key`

 Write a function called `max_key`. Given a dictionary with `str` keys  and `list[int]` values, return a `str` with the name of the key whose list has the highest *sum* of values.
Example: `max_key({"a": [1,2,3], "b": [4,5,6]})` should return `"b"` because the sum of `a`'s elements is 1 + 2 + 3 = 6 and the sum of `b`'s elements is 4 + 5 + 6 = 15, and 15 > 6.

[Solution](#max_key-solution)

### `merge_lists`

Write a function called `merge_lists`. Given a `list[str]` and a `list[int]`, `merge_lists` should return a `dict[str, int]` that maps each item in the first list to its corresponding item in the second (based on index).  If the lists are not the same size, the function should return an empty dictionary.  
Example: `merge_lists([“blue”, “yellow”, “red”], [5, 2, 4])` should return `{"blue": 5, "yellow": 2, "red": 4}`.





# Solutions

## Lists

### `multiples` solution

*(Coming Soon)*

### `reverse_multiply` solution


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




## Dictionaries

### `value_exists` solution

~~~
    def value_exists(d: dict[str, int], num: int) -> bool:
        for key in d:
            if d[key] == num:
                return True
        return False
~~~


~~~
    def value_exists(d: dict[str, int], num: int) -> bool:
        exists: bool = False
        for key in d:
            if d[key] == num:
                exists = True
        return exists
~~~

### `plus_or_minus_n` solution


~~~
    def plus_or_minus_n(inp: dict[str, int], n: int) -> None:
        for key in inp:
            if inp[key] % 2 == 0:
                inp[key] = inp[key] + n
            else: # element is odd
                inp[key] = inp[key] - n
~~~


~~~
    def plus_or_minus_n(inp: dict[str, int], n: int) -> None:
        for key in inp:
            if inp[key] % 2 == 0:
                inp[key] += n
            else: # element is odd
                inp[key] -= n
~~~

### `free_biscuits` solution

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

### `max_key` solution

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

### `merge_lists` solution

*(Coming Soon.)*

