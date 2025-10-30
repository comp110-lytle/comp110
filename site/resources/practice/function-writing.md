---
title: Function Writing Practice Problems
author:
- Alyssa Lytle
- Megan Zhang
- David Karash
- Coralee Vickers
- Carolyn Pierce
- Viktorya Hunanyan
- Benjamin Eldridge
page: lessons
template: overview
---

## Function Writing Practice

Note: Make sure to click the "Show Solutions" button to reveal the solutions before using one of the "Solution" links underneath each function's description.

### Lists

#### `odd_and_even`

* The function name is `odd_and_even` and has a `list[int]` parameter. 
* The function should return a `list[int]`. 
* The function should return a new `list` containing the elements of the input list that are *odd* and have an *even* index. 
* The function should not mutate (modify) the input list. 
* Explicitly type variables, parameters, and return types. 
* The following REPL examples demonstrate expected functionality of your `value_exists` function:

    <pre>
    <div class="terminal">
    >>> odd_and_even([2,3,4,5])
    []
    >>> odd_and_even([7, 8, 10, 10, 5, 12, 3, 2, 11, 8])
    [7, 5, 3, 11]
    </div>
    </pre>

[Solution](#odd_and_even-solution)

#### `short_words`

* The function name is `short_words` and has a `list[str]` as a parameter. 
* The function should return a new `list[str]` of the words from the input list that are shorter than 5 characters. 
* If a word is not added to the new list because it is too long,the function should print a string stating that it was too long. 
* The function should not mutate(modify) the input list. 
* Explicitly type variables, parameters, andreturn types. 
* Include a Docstring that says: Returns list of words that are shorter than 5 characters. 
* The following REPL examples demonstrate expected functionality of your function:

    <pre>
    <div class="terminal">
    >>> weather: list[str] = ["sun", "cloud", "sky"]
    >>> short_words(weather)
    cloud is too long!
    ['sun', 'sky']
    </div>
    </pre>

[Solution](#short_words-solution)

#### `multiples`

Write a function called `multiples`. Given a `list[int]`, `multiples` should return a `list[bool]` that tells whether each `int` value is a multiple of the previous value.  For the first number in the list, you should wrap around the list and compare this `int` to the last number in the list.  
Example: `multiples([2, 3, 4, 8, 16, 2, 4, 2])` should return `[True, False, False, True, True, False, True, False]`.

[Solution](#multiples-solution)

#### `reverse_multiply`

Write a function called `reverse_multiply`. Given a `list[int]`, `reverse_multiply` should return a `list[int]` with the values from the original list doubled and in reverse order.  
Example: `reverse_multiply([1, 2, 3])` should return `[6, 4, 2]`.

[Solution](#reverse_multiply-solution)

### `process_and_reverse_list`
Your function, `process_and_reverse_list`, should follow a structured approach to transform the input list. Given a `list[int]`, `process_and_reverse_list` should firstly square each element in the list, effectively calculating the square of every integer present. Following this, you must compute the sum of each pair of adjacent squared integers and store these sums in a new list. In cases where the input list contains an odd number of elements, the last element should remain unchanged, as it does not have a pair. Finally, the function should reverse the order of this new list of summed pairs, ensuring that the reversed list is returned as the final output.

[Solution](#process_and_reverse_list-solution)

#### `bubble_up_sort` and `insert`

`insert`:

* The function name is `insert` and has two parameters: a `list[int]` and an `int` to be inserted.
* The function inserts the given integer into the list.
* After inserting, the function calls another helper function `bubble_up_sort` to sort the list in ascending order using a "bubble up" method.
* The function mutates the input list by modifying it in place (no return value).
* Explicitly type variables, parameters, and return types.
* There is no need for a return statement since the list is modified directly.

`bubble_up_sort`:

* The function name is `bubble_up_sort` and has a `list[int]` as a parameter.
* The function iterates through the list, starting from the last element and comparing it to the second-to-last element.
* If the second-to-last element is larger than the last element, the two elements are swapped to move the smaller value upward.
* This process is repeated by shifting both indices (second-to-last and last) toward the beginning of the list until the entire list is sorted in ascending order.
* Explicitly type variables, parameters, and return types.
* The function mutates the list by sorting it in place and does not return anything.
* The following REPL examples demonstrate expected functionality of your function:

    <pre>
    <div class="terminal">
    >>> a: list[int] = []
    >>> insert(a, 10)
    >>> insert(a, 19)
    >>> insert(a, 5)
    >>> insert(a, 2)
    >>> insert(a, 1)
    >>> insert(a, 0)
    >>> insert(a, 14)
    >>> insert(a, -4)
    >>> insert(a, 9)
    >>> print(a)
    [-4, 0, 1, 2, 5, 9, 10, 14, 19]
    </div>
    </pre>


[Solution](#bubble_up_sort_and_insert-solution)

### Dictionaries

#### `value_exists`

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

#### `plus_or_minus_n` 

* The function name is `plus_or_minus_n` and is called with `inp: dict[str,int]` and `n: int` as an argument.
* The function should return `None`. It instead *mutates* the input dictionary `inp`.
* The function should check if each *value* in `inp` is even or odd. If it is even, add `n` to that value. If it is odd, subtract `n`.
* Explicitly type variables, parameters, and return types. 
* The following REPL examples demonstrate expected functionality of your function:

[Solution](#plus_or_minus_n-solution)

#### `free_biscuits`

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

#### `max_key`

Write a function called `max_key`. Given a dictionary with `str` keys  and `list[int]` values, return a `str` with the name of the key whose list has the highest *sum* of values.
Example: `max_key({"a": [1,2,3], "b": [4,5,6]})` should return `"b"` because the sum of `a`'s elements is 1 + 2 + 3 = 6 and the sum of `b`'s elements is 4 + 5 + 6 = 15, and 15 > 6.

[Solution](#max_key-solution)

#### `merge_lists`

Write a function called `merge_lists`. Given a `list[str]` and a `list[int]`, `merge_lists` should return a `dict[str, int]` that maps each item in the first list to its corresponding item in the second (based on index).  If the lists are not the same size, the function should return an empty dictionary.  
Example: `merge_lists([“blue”, “yellow”, “red”], [5, 2, 4])` should return `{"blue": 5, "yellow": 2, "red": 4}`.

[Solution](#merge_lists-solution)


<details>
<summary>SHOW SOLUTIONS</summary>

Note:  Your solution does not need to be identical to these, these are just examples of one of many possible solutions!

## Lists


#### `odd_and_even` solution

```py
    def odd_and_even(list1: list[int]) -> list[int]:
        """Find the odd elements with even indexes."""
        i: int = 0
        list2: list[int] = []

        while i < len(list1):
            if list1[i] % 2 == 1 and i % 2 == 0:
                list2.append(list1[i])
            i += 1

        return list2
```

#### `short_words` solution

```py
    def short_words(inp_list: list[str]) -> list[str]:
        """Filter out the shorter words"""
        ret_list: list[str] = []
        for x in inp_list:
            if len(x) < 5:
                ret_list.append(x)
            else:
                print(f"{x} is too long!")
        return ret_list
```

#### `multiples` solution

```py
    def multiples(vals: list[int]) -> list[bool]:
        mults: list[bool] = []
        # check first value against last value
        # a is a multiple of b means a % b == 0
        mults.append(vals[0] % vals[len(vals) - 1] == 0)
        # start idx at 1 since we already checked idx 0
        idx: int = 1
        while idx < len(vals):
            # a is a multiple of b means a % b == 0
            mults.append(vals[idx] % vals[idx - 1] == 0)
            idx += 1
        return mults
```

```py
    def multiples(vals: list[int]) -> list[bool]:
        mults: list[bool] = []
        # check first value against last value
        # a is a multiple of b means a % b == 0
        if vals[0] % vals[len(vals) - 1] == 0:
            mults.append(True)
        else:
            mults.append(False)
        # start idx at 1 since we already checked idx 0
        idx: int = 1
        while idx < len(vals):
            # a is a multiple of b means a % b == 0
            if vals[idx] % vals[idx - 1] == 0:
                mults.append(True)
            else:
                mults.append(False)
            idx += 1
        return mults
```

#### `reverse_multiply` solution

```py
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

```py
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

#### `process_and_reverse_list` Solution

```python
    def process_and_reverse_list(lst):
    # Initialize a list to hold squared elements
    squared_list = []


    # Squaring each element using a while loop
    index = 0
    while index < len(lst):
        squared_value = lst[index] * lst[index]
        squared_list.append(squared_value)
        index += 1


    # Initialize a list to hold the sum of adjacent pairs
    summed_pairs = []


    # Sum adjacent pairs using a while loop
    index = 0
    while index < len(squared_list) - 1:
        pair_sum = squared_list[index] + squared_list[index + 1]
        summed_pairs.append(pair_sum)
        index += 2  # Move by two to get pairs


    # Handle odd number of elements by adding the last squared element
    if len(squared_list) % 2 != 0:
        summed_pairs.append(squared_list[-1])


    # Reverse the summed_pairs list using a while loop
    reversed_list = []
    index = len(summed_pairs) - 1


    while index >= 0:
        reversed_list.append(summed_pairs[index])
        index -= 1


    return reversed_list

    # Test Cases
    print(process_and_reverse_list([1, 2, 3, 4]))  # Output: [13, 5]
    print(process_and_reverse_list([10, 20, 30]))  # Output: [900, 500]
    print(process_and_reverse_list([5]))           # Output: [25]
    print(process_and_reverse_list([7, 8, 9]))     # Output: [145, 49]
```

#### `bubble_up_sort` and `insert` Solution

```python
    def insert(list: list[int], num_to_insert: int) -> None:
        list.append(num_to_insert)
        bubble_up_sort(list)


    def bubble_up_sort(list: list[int]) -> None:
        second_to_last_idx: int = len(list) - 2
        last_idx: int = len(list) - 1
        while last_idx > 0:
            val_sec_to_last: int = list[second_to_last_idx]
            val_last: int = list[last_idx]
            if list[second_to_last_idx] > list[last_idx]:
                # swap
                list[last_idx] = val_sec_to_last
                list[second_to_last_idx] = val_last


            last_idx -= 1
            second_to_last_idx -= 1

    # example
    a: list[int] = []
    insert(a, 10)
    insert(a, 19)
    insert(a, 5)
    insert(a, 2)
    insert(a, 1)
    insert(a, 0)
    insert(a, 14)
    insert(a, -4)
    insert(a, 9)
    print(a)  # expected [-4, 0, 1, 2, 5, 9, 10, 14, 19]
```

### Dictionaries

#### `value_exists` solution

```py
    def value_exists(d: dict[str, int], num: int) -> bool:
        for key in d:
            if d[key] == num:
                return True
        return False
```


```py
    def value_exists(d: dict[str, int], num: int) -> bool:
        exists: bool = False
        for key in d:
            if d[key] == num:
                exists = True
        return exists
```

#### `plus_or_minus_n` solution


```py
    def plus_or_minus_n(inp: dict[str, int], n: int) -> None:
        for key in inp:
            if inp[key] % 2 == 0:
                inp[key] = inp[key] + n
            else: # element is odd
                inp[key] = inp[key] - n
```


```py
    def plus_or_minus_n(inp: dict[str, int], n: int) -> None:
        for key in inp:
            if inp[key] % 2 == 0:
                inp[key] += n
            else: # element is odd
                inp[key] -= n
```

#### `free_biscuits` solution

```py
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

#### `max_key` solution

```py
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

#### `merge_lists` solution

```py
    def merge_lists(words: list[str], vals: list[int]) -> dict[str, int]:
        # If the lists are not same size return empty dict
        if len(words) != len(vals):
            return {}
        idx: int = 0
        merged: dict[str, int] = {}
        while idx < len(words):
            # at key words[idx] store the number at vals[idx]
            merged[words[idx]] = vals[idx]
            idx += 1
        return merged
```

</details>
