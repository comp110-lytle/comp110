---
title: Quiz 02 General Practice
author:
- Alyssa Lytle
- Megan Zhang
- David Karash
- Viktorya Hunanyan
- Carmine Anderson-Falconi
- Benjamin Eldridge
page: lessons
template: overview
---

# Relative Reassignment Operators

1. Refer to the following code snippet to answer the questions below.

    ```py
        def change_number(number: int, modifier: int) -> int:
            idx: int = 0
            end: int = 3
            while idx < end:
                number __ modifier
                idx += 1
            return number

        print(change_number(16, 3))
    ```

    1.1. What would be the output if we ran this code and `__` was replaced with `+=`?

    1.2. What would be the output if we ran this code and `__` was replaced with `-=`?

    1.3. What would be the output if we ran this code and `__` was replaced with `*=`?

2. What would you put in the blank spaces (marked with `_`'s) in the code snippet below to make this a `while` loop that prints the powers of three (1, 3, 9, ...) less than 1000? (Your answer should fit in the blanks)

    ```py
        idx: int = _
        end: int = 1000
        while idx < end:
            print(idx)
            idx __ _
    ```

<details>
<summary>SHOW SOLUTIONS</summary>

1. Answers:

    1.1. `25`

    1.2. `7`

    1.3. `432`

2. Here is the completed code snippet:

    ```py
        idx: int = 1
        end: int = 1000
        while idx < end:
            print(idx)
            idx *= 3
    ```

</details>

# Lists and `while` loops

1. How do you modify an element located at a specific location within a `list`? Give an example. 

2. The following questions will refer to the list below:
    ```python
        my_list: list[int] = list()
    ```
    2.1. Write line(s) of code that would add the number `8`, `0`, `3`, and `-1` to the list. 

    2.2. Write line(s) of code that removes `3` from the list.

    2.3. Write line(s) of code that assigns the variable `dog` to the element at the second index.

    2.4. Write line(s) of code that prints the amount of items in the list. 

    2.5. Change the value `8` to `0`. 

    2.6. We now have a function, `sum` that adds the elements of my_list and returns this amount. Write a line of code that instantiates a `list[int]` with the first value returned from calling `sum` on `my_list`.

3. The following questions will refer to the `animals` list below. Commas are used in place of new lines for the sample outputs.

    ```python
        animals: list[str] = ["dog", "cat", "mouse", "bird", "whale"]
    ```

    3.1. What will print from the following code: 

    ```python
        for x in range(1, len(animals)): 
            print(animals[x])
    ```

    (a) `cat, mouse, bird, whale`

    (b) `dog, cat, mouse, bird`
    
    (c) `1, 2, 3, 4` 
    
    (d) An error will occur when this code is run.

    3.2. What will print from the following code: 

    ```python
        for x in range(1, len(animals) - 1): 
            print(x)
    ```

    (a) `1, 2, 3, 4`

    (b) `cat, mouse, bird`

    (c) `1, 2, 3`

    (d) An error will occur when this code is run.

    3.3. What will print from the following code: 

    ```python
        for animal in animals: 
            print(animal)
    ```

    (a) `dog, cat, mouse, bird, whale`

    (b) `dog, cat, mouse, bird`

    (c) `0, 1, 2, 3, 4`

    (d) An error will occur when this code is run.

    3.4. What will print from the following code: 

    ```python
        for x in animals: 
            print(animals[x])
    ```

    (a) `0, 1, 2, 3, 4`
    
    (b) `dog, cat, mouse, bird, whale`
    
    (c) `1, 2, 3, 4`
    
    (d) An error will occur when this code is run.

    3.5. What will print from the following code: 

    ```python
        x: int = 0
        while x < len(animals): 
            print(x)
            x += 2
    ```

    (a) `0, 1, 2, 3, 4`
    
    (b) `dog, cat, mouse, bird, whale`
    
    (c) `0, 2, 4`
    
    (d) An error will occur when this code is run.

    3.6. What will print from the following code: 

    ```python
        x: int = len(animals) - 1
        while x >= 0: 
            print(animals[x])
            x -= 1
    ```

    (a) `4, 3, 2, 1, 0`
    
    (b) `whale, bird, mouse, cat, dog`
    
    (c) `bird, mouse, cat, dog`
    
    (d) An error will occur when this code is run.

    3.7. What will print from the following code:

    ```python
        for x in range(1, len(animals) - 1, 2): 
            print(x)
    ```

    (a) `1, 3, 4`

    (b) `cat, mouse, bird`

    (c) `1, 3`

    (d) An error will occur when this code is run.

    3.8. What will print from the following code: 

    ```python
        x: int = len(animals) - 1
        while x >= 0: 
            print(animals[x])
            print(x)
            x -= 2
    ```

    (a) `4, 2, 0`
    
    (b) `dog, 0, mouse, 2, whale, 4`
    
    (c) `whale, 4, mouse, 2, dog, 0`
    
    (d) An error will occur when this code is run.


<details>
<summary>SHOW SOLUTIONS</summary>

1. Lists in Python are ordered, 0-indexed collections of values, which means each element has a specific index, starting from 0 and going to the length of the list minus one. You can access elements in a list using these indices via subscription notation, which means using the index within square brackets `[]` next to the name of the list (`list_name[index]`). Then you can modify this element using the assignment operator `=` with the new value you want to assign to that place in the list to the right of the assignment operator (`list_name[index] = new_value`).

    For example: 

    ```python
        my_list: list[str] = [“bark”, “meow”, “tweet”]
    ```

    In this example, if we wanted to change "meow", which is at index 1, to "moo", we would use the square brackets for subscription notation, assigning a new value at that index like this:

    ```python
        my_list[1] = “moo”
    ```

2. List Manipulations

    ```python
        my_list: list[int] = list()

        # 2.1. Add the numbers 8, 0, 3, and -1 to the list.
        my_list.append(8)
        my_list.append(0)
        my_list.append(3)
        my_list.append(-1)

        # 2.2. Remove the number 3 from the list.
        my_list.pop(2)

        # 2.3. Assign the element at the second index to a variable named 'dog'.
        dog = my_list[2]

        # 2.4. Print the number of items in the list.
        print(len(my_list))

        # 2.5. Change the value 8 to 0.
        my_list[0] = 0

        # 2.6. Instantiate a list[int] with the first value returned from calling sum on my_list.
        summed_list = [sum(my_list)]
    ```

3. The example list `animals` is repeated below for convenience.

    ```python
        animals: list[str] = ["dog", "cat", "mouse", "bird", "whale"]
    ```

    3.1. (a) `cat, mouse, bird, whale`

    3.2. (c) `1, 2, 3`

    3.3. (a) `dog, cat, mouse, bird, whale`

    3.4. (d) An error will occur when this code is run. (An error will occur because we are attempting to use the string values of the list as indices in subscription notation, which will not work.)

    3.5. (c) `0, 2, 4`
    
    3.6. (b) `whale, bird, mouse, cat, dog`

    3.7. (c) `1, 3`

    3.8. (c) `whale, 4, mouse, 2, dog, 0`

    
</details>

# Sets

1. Sets in Python are ordered collections of data with values that aren't necessarily unique (T/F).

2. Syntax Practice: How would you declare a set named `classes` of the strings `"110"`, `"210"`, and `"311"`? After this line, add two lines that add makes the condition `classes == {"110", "311", "455"}` be `True`. 

<details>
<summary>SHOW SOLUTIONS</summary>

1. False, sets in Python both have unique values and are unordered.

2. Answer code:

    ```py
        classes: set[str] = {"110", "210", "311"}
        classes.add("455")
        classes.remove("210")
    ```

</details>

# Dictionaries and `for` loops

1. Refer to the following code snippet to answer these questions:
    ```py
        stats: list[int] = [7, 8, 9]
        index: int = 0
        total: int = 100
        while index < len(stats):
            total -= stats[index]
            index += 1
    ```

    1.1. Rewrite the following code snippet with the same functionality using a `for ... in` loop.

    1.2. Rewrite the following code snippet with the same functionality using a `for ... in range(...)` loop.

2. Dictionaries in Python can have duplicate keys. (T/F)

3. What act as your indices in a dict? How can you tell what the type of these indices are? How can you tell what the type of the values are?

4. Given the following code, answer the following question:

    ```py
        tarheels_numbers: dict[str, int] = {"Wilson": 8, "Trimble": 7, "Veesaar": 13, "Evans": 0, "Bogavac": 44}
    ```

    Coach Hubert Davis needs your help, Luka Bogavac is exhausted and needs to be substituted out for Freshman Derek Dixon who wears the jersey number 3. However, Hubert Davis can't remember how to add key-value pairs to a dictionary or how to remove them. How would you write two lines of code to substitute Derek Dixon for Luka Bogavac? (Make sure there's still only five players in the dictionary at the end!)

5. The following questions will refer to the dictionary below:

    ```python
        my_dict: dict[int, str] = {}
    ```

    5.1. Write line(s) of code that would add the following key-value pairs to the dictionary: 
    - `8: 'eight'`
    - `0: 'zero'`
    - `3: 'three'`
    - `-1: 'negative one'`

    5.2. Write line(s) of code that removes value `three`.

    5.3. Write line(s) of code that assign the value associated with the key `0` in `my_dict` to a variable called `cat`.

    5.4. Write line(s) of code that print the number of keys in `my_dict`.

    5.5. Write line(s) of code that print the number of values in `my_dict`.

    5.6. Change the value associated with the key `8` to `'zero'`.

    5.7. Suppose we have a function `sum_dict_keys` that sums the keys of `my_dict` and returns this amount. Write a line of code that instantiates a `dict[str, int]` containing a single value, which is the result of calling `sum_dict_keys(my_dict)` and a key of "returned_amount".

6. The following questions will refer to the dictionary below:

    ```python
        my_dict: dict[int, str] = {10: "dog", 20: "cat", 100: "mouse", 50: "bird", 5: "whale"}
    ```

    6.1. What will print from the following code: 

    ```python
        for x in my_dict: 
            print(my_dict[x])
    ```

    (a) `dog, cat, mouse, bird, whale`

    (b) `dog, cat, mouse, bird`

    (c) `IndexOutOfRange`

    (d) An error will occur when this code is run.

    6.2. What will print from the following code: 

    ```python
        for x in my_dict: 
            print(x)
    ```

    (a) `dog, 10, cat, 20, mouse, 100, bird, 50, whale, 5`
    
    (b) `dog, cat, mouse, bird, whale`
    
    (c) `10, 20, 100, 50, 5`
    
    (d) An error will occur when this code is run.



7. The following questions will refer to the dictionary below:

    ```python
    tarheels_numbers: dict[str, int] = {"Wilson": 8, "Trimble": 7, "Veesaar": 13, "Evans": 0, "Bogavac": 44}
    ```

    7.1. What will print from the following code: 

    ```python
        for x in range(0, len(tarheels_numbers)): 
            print(tarheels_numbers[x])
    ```

    (a) `0, 1, 2, 3, 4`
    
    (b) `Wilson, Trimble, Veesaar, Evans, Bogavac`
    
    (c) `8, 7, 13, 0, 44`
    
    (d) An error will occur when this code is run.

    7.2. What will print from the following code: 

    ```python
        for x in range(0, len(tarheels_numbers)): 
            print(x)
    ```

    (a) `0, 1, 2, 3, 4`
    
    (b) `Wilson, Trimble, Veesaar, Evans, Bogavac`
    
    (c) `8, 7, 13, 0, 44`
    
    (d) An error will occur when this code is run.

    7.3. What will print from the following code: 

    ```python
        for x in tarheels_numbers: 
            print(tarheels_numbers[x])
    ```

    (a) `0, 1, 2, 3, 4`
    
    (b) `Wilson, Trimble, Veesaar, Evans, Bogavac`
    
    (c) `8, 7, 13, 0, 44`
    
    (d) An error will occur when this code is run.

    7.4. What will print from the following code: 

    ```python
        for x in tarheels_numbers: 
            print(x)
    ```

    (a) `0, 1, 2, 3, 4`
    
    (b) `Wilson, Trimble, Veesaar, Evans, Bogavac`
    
    (c) `8, 7, 13, 0, 44`
    
    (d) An error will occur when this code is run.

    7.5. What will print from the following code: 

    ```python
        x: int = 0
        while x < int(len(tarheels_numbers) / 2): 
            print(x)
            x += 1
    ```

    (a) `0, 1`
    
    (b) `Wilson, Trimble`
    
    (c) `8, 7`
    
    (d) An error will occur when this code is run.


8. Create a new dictionary called `my_dictionary` with `str` keys and `float` values and initialize it as an empty dictionary.

9. Using the following dictionary, `msg: dict[str, int] = {"Hello": 1, "Yall": 2}`, access the *value* stored under key "Yall". 

10. Using the following dictionary, `msg: dict[str, int] = {"Hello": 1, "Yall": 2}`, increase the *value* stored under key "Yall" by 3.

11. Using the following dictionary, `ids: dict[int, str] = {100: "Alyssa", 200: "Carmine"}`,
remove the value "Alyssa", stored at key 100.

12. Using the following dictionary, `ids: dict[int, str] = {100: "Alyssa", 200: "Carmine"}`,
write a line of code to get the number of key/value pairs in the dictionary.

13. Using the following dictionary, `inventory: dict[str, int] = {"pens": 10, "notebooks": 5, "erasers": 8}`, add a new key-value pair `"markers": 15`.

14. Using the following dictionary, `prices: dict[str, float] = {"bread": 2.99, "milk": 1.99, "eggs": 3.49}`, update the value of `"milk"` to `2.50`.

15. Using the dictionary `scores: dict[str, int] = {"Alice": 85, "Bob": 90, "Charlie": 88}`, print out all the keys in the dictionary.

16. Using the dictionary `fruit_count: dict[str, int] = {"apples": 5, "bananas": 8}`, iterate over the key-value pairs and print them in the format "key: value". 

<!-- 2. (Challenge Question) Can you iterate through a list or dictionary using a `for` loop while also removing or adding elements? What about modifying elements? -->

<details>
<summary>SHOW SOLUTIONS</summary>

1. Original code copied for reference:

    ```py
        stats: list[int] = [7, 8, 9]
        index: int = 0
        total: int = 100
        while index < len(stats):
            total -= stats[index]
            index += 1
    ```

    1.1. With a `for ... in` loop:

    ```py
        stats: list[int] = [7, 8, 9]
        total: int = 100
        for elem in stats:
            total -= elem
    ```

    1.2. With a `for ... in range(...)` loop.

    ```py
        stats: list[int] = [7, 8, 9]
        total: int = 100
        for index in range(0, len(stats)):
            total -= stats[index]
    ```

2. False. Python dictionaries cannot have duplicate keys. Each key in a dictionary must be unique. If you attempt to create a dictionary with duplicate keys, the latest key-value pair will overwrite the previous one. For example:

    ```py
        my_dict = {"a": 1}
        my_dict["a"] = 2
        print(my_dict)
        # Output: {'a': 2}
    ```


3. In a Python dictionary, the keys act as the "indices." Unlike lists, where numerical indices are used to access elements, dictionaries use keys to access values and these keys can be of any type. You can see the type of both the keys and the values from the type declaration of the dictionary, as the first type within the square brackets `[]` will be the key type and the second will be the value type. For example:

    ```py
        tarheels_numbers: dict[str, int] = {"Wilson": 8, "Trimble": 7, "Veesaar": 13, "Evans": 0, "Bogavac": 44}
    ```

    In this example, the first type listed in the square brackets is `str` and the second type is `int`, thus the keys are of type `str` and the values are of type `int`.


4. Here's how you can help Coach Davis (either order of these two lines is fine):

    ```py
        tarheels_numbers.pop("Bogavac")
        tarheels_numbers["Dixon"] = 3
    ```

5. Dictionary Manipulations

    ```python
        my_dict: dict[int, str] = {}

        # 5.1. Add key-value pairs to the dictionary.
        my_dict[8] = 'eight'
        my_dict[0] = 'zero'
        my_dict[3] = 'three'
        my_dict[-1] = 'negative one'

        # 5.2. Remove the key-value pair where the value is 'three'.
        my_dict.pop(3) # recall that pop takes an index and in the case of dictionaries or indicies are essentially our keys

        # 5.3. Assign the value associated with the key 0 to a variable called 'cat'.
        cat = my_dict[0]

        # 5.4. Print the number of keys in the dictionary.
        print(len(my_dict))

        # 5.5. Print the number of values in the dictionary.
        print(len(my_dict))

        # 5.6. Change the value associated with the key 8 to 'zero'.
        my_dict[8] = 'zero'

        # 5.7. Instantiate a dict[str, int] with the key 'returned_amount' and the value from sum_dict_keys(my_dict).
        result_dict = {'returned_amount': sum_dict_keys(my_dict)}
    ```


6. The following answers refer to the dictionary below:

    ```python
        tarheels_numbers: dict[str, int] = {"Wilson": 8, "Trimble": 7, "Veesaar": 13, "Evans": 0, "Bogavac": 44}
    ```

    6.1. (a) `dog, cat, mouse, bird, whale`
    6.2. (c) `10, 20, 100, 50, 5`



7. The following answers refer to the dictionary below:

    ```python
        tarheels_numbers: dict[str, int] = {"Wilson": 8, "Trimble": 7, "Veesaar": 13, "Evans": 0, "Bogavac": 44}
    ```

    7.1. (d) An error will occur when this code is run. (`range` and `while` loops are generally incompatible with dictionaries as unlike lists, they are not indexed by sequential integers beginning at 0. In this case `range` produces invalid keys since our keys are of type `str`.)

    7.2. (a) `0, 1, 2, 3, 4`

    7.3. (c) `8, 7, 13, 0, 44`

    7.4. (b) `Wilson, Trimble, Veesaar, Evans, Bogavac`

    7.5. (d) An error will occur when this code is run. (`range` and `while` loops are generally incompatible with dictionaries as unlike lists, they are not indexed by sequential integers beginning at 0. In this case a `while` loop that increments an indexing variable `x` produces invalid keys since our keys are of type `str`.)


8. `my_dictionary: dict[str, float] = {}` or `my_dictionary: dict[str, float] = dict()`

9. `msg["Yall"]`

10. `msg["Yall"] += 3` or `msg["Yall"] = 5`

11. `ids.pop(100)`

12. `len(ids)`

13. `inventory["markers"] = 15`

14. `prices["milk"] = 2.50`

15. Code below:

    ```py
        for x in scores:
            print(x)
    ```

16. Code below: 

    ```python
        for boo in fruit_count:
            ghost = fruit_count[boo]
            print(f"{boo}: {ghost}")
    ```

<!-- 2. No, generally you cannot safely iterate through a list or dictionary while simultaneously modifying it by adding or removing elements during the iteration. Doing so can lead to unexpected behavior or errors like the `RuntimeError: dictionary changed size during iteration`. When you iterate over an object, Python keeps track of the size and structure of that object. If you add or remove elements, this can disrupt the iteration process because the underlying data structure changes during traversal. However, you can modify values as you iterate through a list or dictionary (we've done this many times in the class) as long as you do not change the size of the list or dictionary.

    Removing elements: Can cause the iteration to skip items or crash because the index or key you're iterating over might no longer exist.
    Adding elements: Can lead to the same type of issue, as the size of the object changes unexpectedly, leading to errors.

    Take for example this code: 

    ```python
        def add_task(todo_list, task):
            task_found: bool = False
            for existing_task in todo_list:
                if existing_task == task:
                    task_found = True

                if not task_found:
                    todo_list[task] = 'not done'

        def mark_done(todo_list, task):
            # This is fine since we do not change the size of the dictionary
            for existing_task in todo_list:
                if existing_task == task:
                    todo_list[existing_task] = 'done'

        def main():
            todo_list: dict[str, str] = {'Buy groceries': 'not done', 'Read a book': 'done', 'Write report': 'not done', 'Call mom': 'done'}

            add_task(todo_list, 'Finish homework')

            mark_done(todo_list, 'Write report')

            print("Current to-do list:", todo_list)

        if __name__ == "__main__":
            main()
    ``` -->


</details>

# Unit Tests (Conceptual Practice Only)

1. Testing Syntax:

    1.1. What key word do we use within a test function to ensure that a boolean expression is true?

    1.2. What does each test function's name have to begin with?

    1.3. What does each test file's name have to end with?

2. If a function passes all of its associated unit tests, then the function is implemented correctly for all possible inputs (True/False).

3. What is the difference between testing a use case versus an edge case of a function in general?

    a. Testing an edge case is testing a function when it is given expected or normal inputs, while testing a use case is testing a function when it is given unexpected or incorrect inputs to a function, very often an "empty" input.

    b. Testing an edge case is testing a function when it is given unexpected or incorrect inputs to a function, very often an "empty" input, while testing a use case is testing a function when it is given expected or normal inputs.

    c. Testing an edge case is when you test what happens when a function is given an empty input, while testing a use case is when you test what happens when a function is given nonempty input.

    d. None of the above.

4. Consider the following code snippet:

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


<details>
<summary>SOLUTIONS</summary>

1. Question 1 Answers:

    1.1. `assert`

    1.2. `test_`

    1.3. `_test.py`

2. This is False, as unit tests themselves can be incorrect so all tests passing is no guarantee of correctness even for the inputs the unit tests are testing for. Even if the unit tests are correct, there can still be certain inputs that they do not test for and therefore the unit tests cannot assure you that a function will always work properly. Unit tests are a helpful tool that can work well when implemented over a wide range of test inputs, but they must be accompanied by thoughtful implementation of the original function.

3. b. Testing an edge case is testing a function when it is given unexpected or incorrect inputs to a function, very often an "empty" input, while testing a use case is testing a function when it is given expected or normal inputs.

    The reason it is not answer choice c is because while empty vs nonempty inputs is often a distinction between edge cases and use cases, this is not true in all cases (some functions could expect empty inputs, for example).

4. `list_A` and `list_C` would be use cases since this is how we would expect this function to be used and `list_B` would be an edge case as this is essentially attempting to make a function call that would construct a list of negative length since our `length` argument is -2. In this edge case the result would be an empty list since we would never enter the `while` loop. It is possible that this is the intended behavior, or that maybe the original programmer never thought anyone would give a negative argument for `length`.

</details>
