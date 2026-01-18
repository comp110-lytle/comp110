---
title: Week 7 Practice
author:
  - Vincent Li
page: resources
template: overview
---

# Concepts Reviewed

These questions are optional supplements that ideally help you get prepared for the quizzes ahead of time. (Some of them are also designed for elaboration purposes as you can see from the tag. Don't worry them if you just want to get prepared for the quizzes)

<br>

# Questions

### Dictionary
1. Briefly describe what is a dictionary in Python. (Describe its key components.)

2. Just like we create the empty list using `list()` or `[]`. How to create an empty dictionary?

3. Say a dictionary`d = {"apple": 2, "banana": 3}`. Write me a one-line code that can print out the value associated with the key `banana`.

4. (Continue on Question 3) How about writing a one-line code that can add the new key-value pair: `"orange": 4` into the dictionary `d`.

5. Identify if it is legal to have each of the following dictionary key-value types.
5.1 `dict[str, int]`
5.2 `dict[dict[str, int], int]`
5.3 `dict[str, dict[str, int]]`
5.4 `dict[list[str], int]`
5.5 `dict[str, list[int]]`

6. Which of the following method(s) can successfully add a new key-value pair `"COMP": 110` into the dictionary `example`? (Choose all that apply)
A. example.append({"COMP":110})
B. example["COMP"] = 110
C. example.append({"COMP", 110})
D. example.add({"COMP":110})

7. (T/F)Is it Illegal to initiate the following dictionary:
dict1: dict[str, int] = {"COMP": 110, "COMP": 210, "COMP": 283}

8. So far we have learned two types of loops: `while-loop` and `for-in loop`, can we use both of them to iterate the dictionary? Why or why not?

9. (Continue on Q8) If both loops are applicable, pick one of them and iterate through the following dictionary `score`. Or, pick the one that is applicable to iterate through:
~~~
score: dict[str, int] = {"DUKE": 0, "UNC":100, "NYU":50}
~~~

10. (For elaboration) You are iterating over a dictionary in a for loop to check and possibly remove items based on a condition. Halfway through, you decide to remove an item from the dictionary. Why will that cause an error?

11. Consider the dictionary `grades = {'Vincent': 90, 'Mike': 85}.` You used grades['Charlie'] to access the grade of a student called `Charlie`. What specific error does this produce?

<br>

### Unit Test
1. Explain what unit testing is and why it is important in software development.

2. What module in Python is used for unit testing, and how do you import it into your test script?

3. What assert method would you use to check if two values are equal in a unit test? Can you also write the syntax of that assert statement?

4. What is the naming convention when you create a unit test file? What about each individual test inside that file?


# Solutions

### Dictionary
1. Expected Answer: A dictionary is a collection of `key-value pairs`. Each key is unique and is used to store and access its corresponding value.

2. `dict()` or `{}`

3. print(d["banana"])

4. d["orange"] = 4

5. As long as the key is immutable, it will be a legal data type
5.1 Legal
5.2 Illegal
5.3 Legal
5.4 Illegal
5.5 Legal

6. B

7. True

8. Although both types of the loop are applicable to iterate through the dictionary, it is preferable to use the for-in loop as it is definitely more straightforward.

9. 
~~~
for school in score:
    print(f"{school} scored {score[school]} points")
~~~
or 
~~~
keys = list(score.keys()) //May beyond our scope of COMP110
i = 0
while i < len(keys):
    key = keys[i]
    print(f"{key} scored {score[key]} points")
    i += 1
~~~

10. Think of last week's question that we are trying to mutate the value using a for-in loop, it will cause a Runtime Error since the iteration target's size gets changed. It is encouraged to generate a copy and keep the original variable immutable during the iteration.

11. KeyError, meaning that this key is not within the dictionary.

### Unit Test
1. Unit testing involves testing individual components or functions in isolation from the rest of the application. Lay the foundation for the following integrated test. Catch the bugs or errors earlier.

2. Python uses the `unittest` module for unit testing. `import unittest`

3. `assertEqual()` & `self.assertEqual(expected_value, actual_value)`

4. Naming Convention:  Reflects the module it tests with a `test_ prefix`, such as `test_module.py` for a module named `module.py`






