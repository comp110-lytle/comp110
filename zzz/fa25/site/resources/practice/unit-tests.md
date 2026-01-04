---
title: Unit Tests Practice Questions
author:
- Viktorya Hunanyan
- Alyssa Lytle
page: lessons
template: overview
---

# Questions

---

## General 
1. How do you create a test function? What identifies the function as a test? 
2. How do you create a file to write all your unit tests?  
3. What does the assert statement do?
4. Explain the difference between a use case and an edge case. Give an example of both within a function. 
5. If a function passes all of its associated unit tests, then the function is implemented correctly for all possible inputs (True/False).

[Solutions](#conceptual-solutions)

---

## Unit Test Writing and Classifying

6. Suppose you have the following function, designed to return the index of the first even number in a list.

```python
def find_even(nums: list[int]) -> int:
    idx: int = 0
    while idx < len(nums):
        if nums[idx] % 2 == 0:
            return idx
        idx += 1
    return -1
```

Fill in this unit test with a use case.

```python
def test_find_even_use_case() -> None:
    """Put code here."""
```

---

7. Suppose you have the following function, designed to calculate the sum of the elements in a list.

```python
def sum_numbers(numbers: list[int]) -> int:
    if len(numbers) == 0: 
        raise Exception("Empty list - no elements to add")
    
    total: int = numbers[0]
    for i in range(1, len(numbers)): 
        total += numbers[i]
        
    return total
```

Fill in this unit test with a use case.

```python
def test_list_sum_use_case() -> None:
    """Put code here."""
```

---

8. Suppose you have the following function, designed to determine if a number is prime.

```python
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

Fill in this unit test with a use case.

```python
def test_is_prime_use_case() -> None:
    """Put code here."""
```

---

9. Suppose you want to test that a list of dictionaries will be mutated correctly. Here's a function that mutates a list of dictionaries by adding a new key-value pair to each dictionary in the list.

```python
def add_key_to_dicts(dicts: list[dict], key: str, value: int) -> None:
    for d in dicts:
        d[key] = value
```

Fill in this unit test with a use case to verify that the list of dictionaries is mutated correctly.

```python
def test_add_key_to_dicts_use_case() -> None:
    """Put code here."""
```

---

10. Suppose you want to test that a dictionary will be mutated correctly. Here's a function that mutates a dictionary by incrementing the value of a given key by 1.

```python
def increment_dict_value(d: dict[str, int], key: str) -> None:
    if key in d:
        d[key] += 1
    else:
        d[key] = 1
```

Fill in this unit test with a use case to verify that the dictionary is mutated correctly.

```python
def test_increment_dict_value_use_case() -> None:
    """Put code here."""
```

---

11. Suppose you have the following function, designed to sum the elements in a dictionary of list values and return the key with the largest summed value.

```python
def max_sum_dict(d: dict[str, list[int]]) -> str:
    keys = []
    for key in d:
        keys.append(key)

    values_list_1 = d[keys[0]]
    values_list_2 = d[keys[1]]

    total_1 = 0
    for value in values_list_1:
        total_1 += value

    total_2 = 0
    for value in values_list_2:
        total_2 += value

    if total_1 > total_2:
        return keys[0]
    else:
        return keys[1]
```

Fill in this unit test with a use case to verify that the function returns the key with the largest summed value.

```python
def test_max_sum_dict_use_case() -> None:
    """Put code here."""
```

---

12. Write three unit tests for the following function, two testing use cases and one testing an edge case.

```py
def divide_list(input_list: list[int], divisor: int) -> list[float]:
    """Returns a new list where each value is the value from input_list divided by divisor"""
    result: list[int] = []

    for num in input_list:
        result.append(num / divisor)

    return result
```

---

13. Consider the following code snippet:

```py
def fill_list(num: int, length: int) -> list[int]:
    """Fill a list with a single value."""
    result: list[int] = []

    i: int = 0
    while i < length:
        result.append[num]
        i += 1

    return result

list_A: list[int] = fill_list(4, 19) 
list_B: list[int] = fill_list(55, -2)
list_C: list[int] = fill_list(1, 110)
```

Which function calls would be considered a use case of this function (list the associated variable name e.g. `list_A`)? Which would be considered edge cases? If there are any edge cases, what result would you get in the associated variable(s)?

# Solutions

## Conceptual Solutions

1. A test function is created just like any other Python function, but it is identified as a test by starting its name with `test_`. In frameworks like pytest, any function that starts with `test_` is automatically detected and run as a test.

2. Create a new Python file, often named `<module_name>_test.py`, in the same directory as your module. Write all your test functions in this file.

3. The assert statement checks if a condition is true. If the condition is false, an AssertionError is raised, indicating that the test has failed.

4. A use case is a typical scenario where the function is expected to work as intended. For example, in a function that sums a list, a use case would be passing a list like `[1, 2, 3]`.
An edge case is a situation where the function might struggle or behave differently, like passing an empty list `[]` to a sum function.

5. This is False, as unit tests themselves can be incorrect so all tests passing is no guarantee of correctness even for the inputs the unit tests are testing for. Even if the unit tests are correct, there can still be certain inputs that they do not test for and therefore the unit tests cannot assure you that a function will always work properly. Unit tests are a helpful tool that can work well when implemented over a wide range of test inputs, but they must be accompanied by thoughtful implementation of the original function.

## Unit Test Writing

6. Solution below: 

```python
def test_find_even_use_case() -> None:
    nums = [1, 3, 5, 4, 7]
    assert find_even(nums) == 3
```

---

7. Solution below:

```python
def test_list_sum_use_case() -> None:
    # Test case 1: Normal list of positive numbers
    assert sum_numbers([1, 2, 3, 4, 5]) == 15

    # Test case 2: List with negative numbers
    assert sum_numbers([-1, -2, -3, -4, -5]) == -15

    # Test case 3: Mixed positive and negative numbers
    assert sum_numbers([1, -1, 2, -2, 3, -3]) == 0

    # Test case 4: List with a single element
    assert sum_numbers([10]) == 10

    # Do not worry about handling the exception! 
    # That is out of the scope of the class :)
```

---

8. Solution below:

```python
def test_is_prime_use_case() -> None:
    assert is_prime(7) is True
    assert is_prime(8) is False
```

---

9. Solution below:

```python
def test_add_key_to_dicts_use_case() -> None:
    dicts = [{"a": 1}, {"b": 2}]
    add_key_to_dicts(dicts, "c", 3)
    assert dicts == [{"a": 1, "c": 3}, {"b": 2, "c": 3}]
```

---

10. Solution below: 

```python
def test_increment_dict_value_use_case() -> None:
    d = {"a": 1, "b": 2}
    increment_dict_value(d, "a")
    assert d["a"] == 2
    increment_dict_value(d, "c")
    assert d["c"] == 1
```

---

11. Solution below: 

```python
def test_max_sum_dict_use_case() -> None:
    d = {"a": [1, 2, 3], "b": [4, 5]}
    assert max_sum_dict(d) == "b"
```

12. `list_A` and `list_C` would be use cases since this is how we would expect this function to be used and `list_B` would be an edge case as this is essentially attempting to make a function call that would construct a list of negative length since our `length` argument is -2. In this edge case the result would be an empty list since we would never enter the `while` loop.

13. Note: These are just some examples of what you could test for, but they will likely not be the same as what you wrote as there are many correct answers.

    The most straightforward use case test would be ensuring that on a normal input that the output is what you expect:

    ```py
    def test_normal_divide_list() -> None:
        classes: list[int] = [110, 210, 301, 455]
        assert divide_list(classes, 10) = [11.0, 21.0, 30.1, 45.5]
    ```

    Another unit test for an edge case might be to ensure that the original list was not mutated:

    ```py
    def test_no_mutate_divide_list() -> None:
        classes: list[int] = [110, 210, 301, 455]
        divide_list(classes, 10) # We don't need to store the result
        assert classes = [110, 210, 301, 455]
    ```

    Finally, an example of an edge case for this function would be a divisor of zero, which we should expect to result in an error. We can test to ensure that an error occurs like this:

    ```py
    def test_div_zero_error_divide_list() -> None:
        classes: list[int] = [110, 210, 301, 455]
        with pytest.raises(ZeroDivisionError):
            divide_list(classes, 0)
    ```