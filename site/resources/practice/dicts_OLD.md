---
title: Dictionary Conceptual Questions
author:
- Alyssa Lytle
- Viktorya Hunanyan
- Carmine Anderson-Falconi
page: lessons
template: overview
---

# Questions

## Conceptual
For the following, you must prove your answer to each question. Prove using either memory diagrams or code in VS code.

1. Dictionaries in Python can have duplicate keys. (T/F)
2. Dictionaries in Python can be nested, meaning a dictionary can contain another dictionary as a value. (T/F)
3. Can you remove only a key without removing a value (or vice versa)? 
4. What act as your indices in a dict? 

## Dict General Questions

5. Explain in words how you modify elements in a dict? How would you do this in python? Give an example. 
6. How do you remove elements in a dict? What does this actually remove? 
7. How do you modify a key in a dict?
8. Write the general formula of how you remove a key-value pair to a dictionary object using the following. You might not need to use all and can use any multiple times: `pop`, `append`, `()`, `<object_variable>`, `.` , `<key>`, `<value>`, and `[]`. Give examples.
9. Write the general formula of how you remove a key-value pair to a dictionary object using the following. You might not need to use all and can use any multiple times: `pop`, `append`, `()`, `<object_variable>`, `.` , `<key>`, `<value>`, and `[]`. Give examples.

## Dictionary Practice

10. Create a new dictionary called `my_dictionary` with `str` keys and `float` values and initialize it as an empty dictionary.

11. Using the following dictionary, `msg: dict[str, int] = {"Hello": 1, "Yall": 2}`, access the *value* stored under key "Yall". 

12. Using the following dictionary, `msg: dict[str, int] = {"Hello": 1, "Yall": 2}`, increase the *value* stored under key "Yall" by 3.

13. Using the following dictionary, `ids: dict[int, str] = {100: "Alyssa", 200: "Carmine"}`,
remove the value "Alyssa", stored at key 100.

14. Using the following dictionary, `ids: dict[int, str] = {100: "Alyssa", 200: "Carmine"}`,
write a line of code to get the number of key/value pairs in the dictionary.

15. Using the following dictionary, `inventory: dict[str, int] = {"pens": 10, "notebooks": 5, "erasers": 8}`, add a new key-value pair `"markers": 15`.

16. Using the following dictionary, `prices: dict[str, float] = {"bread": 2.99, "milk": 1.99, "eggs": 3.49}`, update the value of `"milk"` to `2.50`.

17. Using the dictionary `scores: dict[str, int] = {"Alice": 85, "Bob": 90, "Charlie": 88}`, print out all the keys in the dictionary.

18. Using the dictionary `scores: dict[str, int] = {"Alice": 85, "Bob": 90, "Charlie": 88}`, write a line of code that returns the sum of all the values (scores) in the dictionary. Assume that we have a written a `sum` function that will do this for us when passing in a `dict`. Store this value in a variable `total_score`. 

    - 18a. Write the same line of code except using key-word arguments assuming that the only parameter in `sum` is called `inp_dict`. 

19. Using the dictionary `fruit_count: dict[str, int] = {"apples": 5, "bananas": 8}`, iterate over the key-value pairs and print them in the format "key: value". 

20. Create a new dictionary by combining the two dictionaries. Store this new object by assiging it's reference to a variable called `combo_dict`:

```python
    first_dict: dict[str, int] = {"a": 1, "b": 2}
    second_dict: dict[str, int] = {"c": 3, "d": 4}
```

# Answers

## Conceptul

1. False. Python dictionaries cannot have duplicate keys. Each key in a dictionary must be unique. If you attempt to create a dictionary with duplicate keys, the latest key-value pair will overwrite the previous one. For example:

```
my_dict = {"a": 1, "a": 2}
print(my_dict)
# Output: {'a': 2}
```

2. True, Python dictionaries can be nested. This means that a dictionary can hold another dictionary as a value. You can use this feature to create more complex data structures. For example:

```
nested_dict = {
    "key1": {"nested_key1": 1, "nested_key2": 2},
    "key2": {"nested_key3": 3, "nested_key4": 4}
}
```

3. False. No, you cannot remove just a key or just a value in a dictionary. A key-value pair is considered a single entity in a dictionary. If you remove the key, the corresponding value is also removed.


4. In a Python dictionary, the keys act as the "indices." Unlike lists, where numerical indices are used to access elements, dictionaries use keys to access values and these keys can be of any type. Each key must be unique, and it serves as the identifier for accessing the corresponding value. For example:

```
my_dict = {"name": "Alice", "age": 25}
print(my_dict["name"])  # Output: Alice
```

## Dict General Questions

5. To modify an element in a Python dictionary, you use the key associated with the value you want to change. You can access the value using the key, and then assign a new value to it. In order to access the value, we use subscription notation, `[]`, on the object that we want to access the value at. This replaces the old value with the new one.

```
my_dict = {"name": "Alice", "age": 25}
my_dict["age"] = 26  # Modifying the value associated with the key "age"
print(my_dict)
# Output: {"name": "Alice", "age": 26}
```

6. To remove elements from a dictionary, we use the the pop() method. This method will remove the key and its corresponding value (key-value pair). The pop() method allows you to retrieve the value that was removed (not discussed in lecture but a very cool fact).

```
my_dict = {"name": "Alice", "age": 25}
removed_value = my_dict.pop("age")  # Removes the key "age" and returns the value
print(my_dict)  # Output: {"name": "Alice"}
print(removed_value)  # Output: 25
```

7. To modify a key in a Python dictionary, we can follow these steps:
- 1. Add a new key with the same value as the old key.
- 2. Use pop() to remove the old key-value pair.

```
my_dict = {"name": "Alice", "age": 25}

# Step 1: Create a new key-value pair using the value from the old key
my_dict["years_old"] = my_dict.pop("age")

print(my_dict)
# Output: {"name": "Alice", "years_old": 25}
```

8. `<object_variable>.pop(<key>)`

```
my_dict = {"name": "Alice", "age": 25}
removed_value = my_dict.pop("name")  # Removes the key "name" and returns its value
print(my_dict)
# Output: {"age": 25}
```

9. `<object_variable>[<key>] = <value>`

```
my_dict = {"name": "Alice", "age": 25}
my_dict["location"] = "New York"  # Adds a new key-value pair to the dictionary
print(my_dict)
# Output: {"name": "Alice", "age": 25, "location": "New York"}
```

## Dictionary Practice

10. `my_dictionary: dict[str, float] = {}` or `my_dictionary: dict[str, float] = dict()`

11. `msg["Yall"]`

12. `msg["Yall"] += 3` or `msg["Yall"] = 5`

13. `ids.pop(100)`

14. `len(ids)`

15. `inventory["markers"] = 15`

16. `prices["milk"] = 2.50`

17. Code below:

```
for x in scores:
    print(x)
```

18. `total_score = sum(scores)`

- 18a. `total_score = sum(inp_dict=scores)`

19. Code below: 

```python
for boo in fruit_count:
    ghost = fruit_count[boo]
    print(f"{boo}: {ghost}")
```

20. `combo_dict: dict[str, int] = {"a": 1, "b": 2, "c": 3, "d": 4}`