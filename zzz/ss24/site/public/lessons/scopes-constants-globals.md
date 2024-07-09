---
title: Scopes, Constants, and Global Variables
author:
- Kris Jordan
page: lessons
template: overview
---

## Scopes

When there can be many _people_, or more broadly _things_, which share the same name, the meaning of the name depends on the _context_ it is being referenced from. Let us consider a hypothetical, real-world scenario.

Imagine you just heard some amazingly positive news about your friend Lauren winning the lottery while on a road trip. You're so blown away you ask a gas station attendant, _"Wow, can you believe the news about Lauren?!"_ They look at you puzzled, "sorry, I don't know a Lauren." Slightly annoyed, you walk back out to the gas pumps and ask a stranger pumping gas the same question. With a look of suspicion the stranger responds, "you know my horse?" Now _you_ look puzzled and say, "neigh, sorry, different Laurens."

In _your_ head, the name Lauren is your close friend. In the gas station attendant's, the name Lauren is not associated with anyone. In the stranger's head, Lauren is associated with their horse friend. While this ambiguity can lead to confusion, it makes complete sense, right? The world would be overwhelming if every _thing_ had a unique name.

In the evaluation of a single program, the same name can exist in _different contexts_ and be bound to many different values, all at the same time. Each function call _has its own context for names_. This is why, when diagramming with an _environment diagram_, we setup a new _frame_ for a function call. The rules of a language's _name resolution_ process decide what name you're referring to in a given context.

The _scope_ of an _identifier_, which includes variable _names_, function _names_, and _names_ of a few other concepts you'll learn in time, refers to _where you can access a specific definition of the identifier from_ in a program. Unpleasant surprises occur when you attempt to _access_ an _identifier_ outside its scope. For example, if an identifier is yet to be defined, or its definition is in a context _name resolution_ will not check, then you will be faced with a `NameError`.

Try the following example in your Python REPL:

~~~plaintext
>>> print(lauren)
NameError: name 'lauren' is not defined
>>> lauren: str = "a friend"
>>> def stranger() -> None:
...   lauren: str = "a horse"
...   print(lauren)
...
>>> print(lauren)
a friend
>>> stranger()
a horse
>>> print(lauren)
a friend
~~~

Let us walk through each of the steps above. First, an error occurs when attempting to access an identifier, or "read a variable", such as `lauren`, before it is defined.

The name `lauren` was first defined outside of any function and bound to the string `"a friend"`. Note the identifier `lauren` would now be _bound_ in the `Globals` frame of your diagram.

Next, a function is defined and its definition would be bound to the name `stranger` in the globals frame.

When `lauren` is printed, the current frame of execution is `Globals`, therefore the string `"a friend"` is bound to it.

Next, a function call to the `stranger` function is evaluated. This function call establishes a new frame on the stack, which becomes the current frame of execution while the function is evaluating. Inside the function definition, notice that a new variable, coincidentally named `lauren`, is is established in this frame. Now there are two identifiers on the call stack with the _name_ of `lauren`. One is in globals, the other is the one we just evaluated in `stranger`, and is bound to the string `"a horse"`. Thus, when `print(lauren)` is evaluated in the context of the call to `stranger`, it results in `a horse` being printed. The end of the _procedure_ function body is reached, so `None` is implicitly returned. The current execution context returns to `Globals`.

Finally, when we access `lauren` once last time from the `Globals` context, it is still bound to `"a friend"`, just the same as it was before calling `stranger`. 

## Accessing Global Names

_Global names_ are those defined in the globals frame, outside of any other context, such as a function definition.

In the Python programming language, global variables are technically _module variables_. They are only "global" within a module, meaning within a single Python file. The concept of _global variables_ and _global scope_ is more widely applicable in other programming languages than _module variables_, though, so we will choose the more universal terminology. Notice the meta in this description. Sometimes you intentionally want to refer to names whose definitions are beyond your local concerns.

In the preceding section's REPL example, the name `lauren` was initially defined as a _global variable_. In the following example, we will define a function that accesses this global variable.

~~~plaintext
>>> lauren: str = "a friend"
>>> def global_access() -> None:
...   print(lauren)
...
>>> global_access()
"a friend"
~~~

Notice a key distinction between the `global_access` function and the `stranger` function: `lauren` was redefined and bound to have a different, local meaning in `stranger`.

_Name resolution_ rules inform why the `global_access` function was able to read from `lauren` rather than result in a `NameError`. When a name is not found in the current scope, which in a function call is the current frame of execution, then the Globals frame is checked. This is how the `main` function is able to _call_ other functions whose identifiers are found in `Globals` and bound to their definitions.

## Named Constants and Magic Numbers

The most valuable, and acceptable, use of _globally scoped_ variables are to put names on _constant values_ used throughout your program. Consider the following code listing:

~~~plaintext
def compound(current: float) -> float:
    return current + (current * 0.009)
~~~

The `float`-literal `0.009` is a _constant_ value in the program. It will not change. It is also kind of "magical" isn't it? Where did this number come from and what does it represent? Often the same constant like this is copied throughout a program. Programmers call literals like this a "magic number".

Magic numbers are a bad practice for two reasons:

1. Magic numbers make your program more difficult to understand. Someone else reading your code will not immediately know _why_ that number is chosen. Further, you yourself will become a stranger to your own code and will often forget why _you_ chose some specific number.
2. Magic numbers used throughout a program are more work to change and maintain. At best, you remember you have multiple places you need to update the magic number or search/replace all. At worst, you forget to update a few places and are accidentally relying on different values for what should have been consistent!

_Named constants_ are the preferred technique for avoiding magic numbers. A named constant is a global variable whose value is initialized and does not change at runtime.

_Named constants_ are conventionally named using all capital letters with underscores separating words. This convention makes it easy to distinguise a variable name from a globally named constant. Let's rewrite the previous example to use a named constant:

~~~plaintext
INTEREST_RATE: float = 0.009

def compound(current: float) -> float:
    return current + (current * INTEREST_RATE)
~~~

Convince yourself this change is both easier to understand to someone reading the code for the first time. If the same named constant were used in multiple places, notice how much easier this code is to update, as well: you only need to change the value of the named constant and all uses of it will be correct.

Moving forward, any time you use a "magic number" in your program you should catch yourself as quickly as possible and _refactor_, meaning rewrite in such a way the program has the same meaning but is better structured, your program to use a named constant instead.

Named constants are intended to remain... _constant_! Thus, you should never attempt to reassign a named constant. If you need a globally accessible value that changes as the program is running, the next section discusses how to go about it. Most programming languages will actively prevent you from accidentally reassigning a new value to a named constant because doing so can be a source of great confusion. Python does not enforce this rule, though, so be careful to avoid being bitten by this snake.

## Reassigning a Global Variable

You now know two _primary use cases_ for globally defined names:

1. Defining structural components of your programs such as _functions_ and, you will soon learn, _classes_.
2. Defining named constants.

There's another use of globally defined variables that is worth knowing, but with an important disclaimer. Global variables can be handy in small programs, but should generally be avoided as your programs grow in size and you learn techniques for avoiding their use. Global variables can make programs  more difficult to reason about and more error prone.

When you initialize a local variable in a function in Python, by default it binds the variable's name _locally_ within the context of the function. Subsequent references to the name from inside the context of the function will refer to its _local_ value. You saw this in the `stranger` example above.

But, what if you **want** to _reassign_ to a global variable in Python? You must specifically declare your intent to do so. Let's explore with an example:

~~~plaintext
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

There are a few important points to notice. First, `lauren` is defined as a global variable, outside of any function.

Second, notice the `global` keyword followed by the name `lauren` on the first line of `a_forceful_stranger`. The `global` statement indicates within the function call's frame all references to `lauren` will resolve to the _global variable_ `lauren`. Importantly, all _assignment statements_ will assign to the global variable `lauren`. Notice, unlike in the original example, after the function call evaluates, the global variable's value is changed!

When it comes to diagramming the call stack, when you evaluate the function `a_forceful_stranger`, you would not introduce the name `lauren` in its frame because of the `global` keyword. The `global` declaration prevents a new entry from being added locally.

These specific kinds of rules around name resolution, scope, variable access, and variable assignment are where different programming languages make different choices. Python's rules make it easy for you to access global variables but make you go out of your way to _reassign_ them. This is helpful! When you find yourself learning or writing other programming languages, comparing and contrasting these rules in Python to the other languages' rules will help you get up to speed quickly.

In Python, you should name global variables with standard, lowercase `snake_case_conventions`.

Where is it appropriate to use a global variable? Suppose you're writing a program in a single file and there's a variable many different functions in your program need to make use of. For example, maybe you're writing a little interactive game and ask the user for their `name` as the program begins. Rather than having to pass around their `name` as an argument to every function call, storing it in a global variable may make sense. Another example might be a single player game that keeps track of a `score`. Being able to access and modify the `score` from various functions is handy.

When in doubt, though, prefer local variables and named constants!

## Why are global variables generally discouraged?

These concerns are a bit outside yours at this point, but foreshadowing can help prepare you for later ideas.

Reading from and writing to _global variables_ are examples of _side-effects_ in our _fundamental pattern_. The formal inputs to a function are its parameters and its formal result is its return value. Yet, a function can also read from and write to global variables it has access to through its _environment_.

Using _global variables_ makes your programs more difficult to debug. Since _any function_ is able to modify a global variable, if your bug is impacted by the _global variable_ then you must check all of the possible places it is reassigned from. Not only that, but you must begin to consider _how_ they change the _global variable_ and reason through _what order_ those functions might be called in, and so on. This is _much, much_ more challenging than working with local variables whose scopes are confined within the context of a function call's frame.

Functions which do not have any side-effects, including not accessing or reassigning global variables, are called _pure_ functions and are the easiest kind of functions to work with because they come with no surprises. When in doubt, write _pure_ functions!