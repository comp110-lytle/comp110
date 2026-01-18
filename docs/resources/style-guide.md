---
title: Style, Linting and Autograder Guide
author:
- Ezri White
page: resource
template: overview
---

## General Layout Guidelines

1. Make sure to include a file __Docstring__ and __author variable__.
    - A __Docstring__ should be surrounded by triple quotes, have no spaces on at the beginning and end, and end in punctuation.
    - An __author variable__ should have two underscores (a dunderscore) on either side of author and be equal to your PID in __String__ format.
2. __Named constants__ follow the Docstring and author variable. They should be all capitalized and already initialized. 
3. Every function and class should have it's own __Docstring__ as the first line. There should also be two newlines of space in between each function or class.
    - Every function must be declared with a unique name, it's parameters and a return type.
    - Note that `add_one` returns an `int` and therefore must have a return statment. However `print_word` returns `None` and therefore a return statement is not required.

~~~ {.python .numberLines startFrom="1"}
"""This is a Docstring."""

__author__ = "123456789"

NAMED_CONSTANT: int = 1


def add_one(num: int) -> int:
    """Adds one to a given number."""
    return num + NAMED_CONSTANT


def print_word(word: str) -> None:
    """Prints out a given word."""
    print(word)
~~~


## How to Read the Autograder

If you don't recieve full credit when submitting to the autograder, there will likely be error messages outputted. Understanding how to read these messages can be key to figuring out what is wrong with your code.

#### Basic Failed Test

Below is an example of a possible autograder error message if your code did not pass a functionality test.

![](../../static/assets/autograder-fail.png)

- `graders/exercises/ex02/cipher_test.py:38` tells you which line of the grader found the missing functionality in your code. Since you cannot see the grader, you can ignore this part.
- `AssertionError: assert 'n' == 'njml'` tells you that your code outputted `'n'` but the autograder was expecting `'njml'`.
- ` - njml,  + n` tells you the same thing, `njml` was missing from your output but `n` was present.


#### Code Style and Linting Errors

Below is an example of a possible autograder error message for a style issue.

![](../../static/assets/autograder-lintfail.png)

- `exercises/ex02/cipher.py` tells you that it was the `cipher.py` file that threw the error and that the file is located in `exercises/ex02`.
- `10` tells you that this error originated from line 10 of the given file.
- `43` tells you how far (how many characters) into the line the error occured.
- `E225` is a __flake8 linter__ error. Linting helps identify formatting issues in your code. You can view these error codes <a href="https://www.flake8rules.com/" target="_blank" rel="noopener noreferrer">here</a>.
- `missing whitespace around operator` gives you a brief summary of your formatting issue.

Most autograder errors will follow this general pattern. You should familiarize yourself with reading autograder errors to help you get full points on exercises, projects and quizzes. 


## Specific Autograder Errors

This section contains errors unrelated to linting and styling and some possible fixes to try.

- The file won't upload, or when it uploads the autograder doesn't seem to recognize the files.
    - Delete all your old submission zips, then create a new submission zip making sure to check for punctuation or spelling errors in the command.

- No tests or only `Lint - Code style, documentation, formatting` is showing up.
    - Check that your file is in the correct location.
    - Make sure your folder and files are named correctly.
    - Confirm all functions are properly named and declared.
    - Check for any unclosed parenthesis, quotation marks or other small syntax errors.


- `module <_file_path_> has no attribute '__author__'`
    - Make sure your `__author__` variable has __TWO__ underscores on either side.
    - Make sure your `__author__` variable is a string.