---
title: Globals
author:
- Tori Hoffmann
page: resource
template: overview
---

### Global Variables

__Global variables__ are those defined in the globals frame, outside of any other context, such as a function definition.

- Reminder: In Python, you should name global variables with standard, lowercase snake_case_conventions.

Looking for a variable but you don't see it in the current scope? Check the globals frame! This is how the main function is able to call other functions whose identifiers are found in Globals and bound to their definitions.


### Named Constants and Magic Numbers
The most valuable, and acceptable, use of globally scoped variables are to put names on constant values used throughout your program. Consider the following code listing:

~~~ {.python }
    def compound(current: float) -> float:
        return current + (current * 0.009)
~~~

The float-literal 0.009 is a constant value in the program. It will not change. It is also kind of “magical” isn’t it? Where did this number come from and what does it represent? Often the same constant like this is copied throughout a program. Programmers call literals like this a __“magic number”__.

Magic numbers are a bad practice for two reasons:

(1) Magic numbers make your program more difficult to understand. Someone else reading your code will not immediately know why that number is chosen. Further, you yourself will become a stranger to your own code and will often forget why you chose some specific number.
(2) Magic numbers used throughout a program are more work to change and maintain. At best, you remember you have multiple places you need to update the magic number or search/replace all. At worst, you forget to update a few places and are accidentally relying on different values for what should have been consistent!

__Named constants__ are the preferred technique for avoiding magic numbers. A __named constant__ is a global variable whose value is initialized and does not change at runtime.

Named constants are conventionally named using all capital letters with underscores separating words. This convention makes it easy to distinguise a variable name from a globally named constant. Let’s rewrite the previous example to use a named constant:

~~~ {.python }
    INTEREST_RATE: float = 0.009

    def compound(current: float) -> float:
        return current + (current * INTEREST_RATE)
~~~

Any time you use a “magic number” in your program you should catch yourself as quickly as possible and refactor your program to use a named constant instead.

Remember: Named constants are intended to remain… constant! Thus, you should never attempt to reassign a named constant. 

### Reassigning A Global Variable

If you want to reassign a global variable in Python you must specifically declare your intent to do so. An example of what this may look like is shown below: 

~~~ {.python }
    >>> lauren: str = "a friend"
    >>> def a_forceful_stranger() -> None:
    ...   global lauren
    ...   lauren = "MY HORSE"
    ...   print(lauren)
    ...
    >>> print(lauren)
    a friend
    >>> a_forceful_stranger()
    MY HORSE
    >>> print(lauren)
    MY HORSE
~~~

Disclaimer: Global variables can be handy in small programs, but should generally be avoided as your programs grow in size and you learn techniques for avoiding their use. Global variables can make programs more difficult to reason about and more error prone. When in doubt, prefer local variables and named constants!