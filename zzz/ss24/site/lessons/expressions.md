---
title: Expressions
author:
- Kris Jordan
page: lessons
template: overview
---

## Expressions Enable Creativity in Solutions

*Expressions* are a fundamental building block in programs. Much like clauses in English, the artful use of expressions gives you the freedom to compose and _express_ precise ideas and computations.

There are two **big ideas** behind expressions:

1. Every expression *evaluates* to a *typed* value at runtime
   * Every expression evaluates to a specific, concrete type
   * The evaluation of an expression only occurs when the program is running or when you ask the interactive Python interpreter to evaluate it
2. Anywhere you can write an expression, you can substitute _any other expression of the same type_ and still have a validly _typed_ program (though it may have bugs!)

Expressions operate on objects and the types of objects inform the kinds of expressions you can write to operate on them or with them. An object's _type_ tells you what you can do with it. An expression is an intent to do something.

## Literal Expressions

Good news, you already learned these! When a literal expression is *evaluated*, it results in an *object* guided by what was *literally* written in code. Notice there is an *evaluation* taking place to convert a literal such as `"hello"` to the `str` whose character contents are `hello`, in that the quotation marks are not a part of the constructed `str` value. Literals are the simplest form of an expression because their *evaluation* is straightforward.

## Operator Expressions

To accelerate your understanding operators, let's apply your prior experience with mathematical operators. They do not work exactly the same in all cases, but the same intuitions generally apply. Consider mathematical expression such as:

$1 + 2$

You know this expression isn't _fully evaluated_ or "simplified". To _evaluate_ it, you take the value on each side of the **addition operator** and combine their values. This expression _evaluates to_ 3. 

You can _compose_ a more complex expression by adding an additional operator to it:

$1 + 2 \times 3$

Does this expression evaluate to `9` or `7`? Be careful of your algebraic precedence rules! In the absence of parentheses, the **multiplication operator** takes a higher precedence than addition. Thus the expression first simplifies to $1 + 6$, and then to $7$. _Note: the multiplication operator in Python, and most programming languages, is the asterisk `*`._

When a programming expression is evaluated, precedence and orders of operation also apply. The computer will evaluate each expression in your program one step at a time. For the purposes of numerical expressions, typical precedence rules apply. Parentheses allow you to control precedence outside of any implicit rules, exponents follow, multiplication and division are at the same level of precedence and evaluate left to right, followed by addition and subtraction, and so on. There are other operators you'll encounter, too, and we'll discuss their precedence as needed.

### Numerical Operators

In the examples above you saw two arithmetic operators: addition and multiplication. In an interactive Python session, try exploring some additional numerical computations including some of these below. See if you can figure out what the mysterious ones are doing!

~~~ {.plaintext}
>>> 4 / 2
2.0

>>> 4.0 / 2.0
2.0

>>> 4 / 3
1.3333333333333333

>>> 2 ** 3
8

>>> 2 ** 64
18446744073709551616

>>> 3 % 5
3

>>> 5 % 5
0

>>> 6 % 5
1

>>> 7 % 5
2

>>> 7 // 5
1

>>> 6 // 5
1

>>> 4 // 5
0

>>> -(1 + 1)
-2
~~~

### Table of Numerical Operators

|  Symbol    | Operator Name      | Example                       |
|:----------:|:-------------------|:------------------------------|
| `**`       | Exponentiation     | `2 ** 8` equivalent to $2^8$  |
| `*`        | Multiplication     | `10 * 3`                      |
| `/`        | Division           | `7 / 5` result is `1.4`       |
| `//`       | Integer Division   | `7 // 5` result is `1`        |
| `%`        | Remainder "modulo" | `7 % 5` result is `2`         |
| `+`        | Addition           | `1 + 1`                       |
| `-`        | Subtraction        | `111 - 1`                     |
| `-`        | Negation           | `-(1 + 1)` result is `-2`     |

In general, when you apply a numerical operator between two of values of the same type, whether `int` or `float`, you will get back a value of the same type. However, an expression formed with the standard division operator will always evaluate to a `float`, even if both sides of the operator are an `int`. If you attempt to form an expression between an `int` and a `float`, the `int` will first be converted to the a `float` and then the expression will be evaluated.

For integer division, like you learned in elementary school, the `//` operator will return an `int` and will always truncate, or remove, any remainder. The `%` operator will compute the remainder. You will be surprised at how frequently the remainder operator is useful in programming!

### Relational Operators

Programs commonly need to relate two values with one another to make decisions. For example, if you visit a website regarding alcoholic beverages, you will be asked for your date of birth. The website needs to compare your age with 21 in order to determine whether to let you into the website, or not. This kind of _comparison_ tests a relationship, "true or false: 18 is greater than or equal to 21?" `False`!

~~~ {.plaintext}
>>> 18 >= 21
False

>>> 21 >= 21
True

>>> 22 >= 21
True

>>> 110 == 110
True

>>> 110 != 110
False
~~~

### Table of Relational Operators

| Operator Symbol | Verbalization | `True` Example      | `False` Example |
|:----------:|:-------------------|:--------------------|-----------------|
| `==`       | Is equal to?       | `1 == 1`            | `1 == 2`        |
| `!=`       | Is NOT equal to?   | `1 != 2`            | `1 != 1`        |
| `>`        | Is greater than?   | `1 > 0`             | `0 > 1`         |
| `>=`       | Is at least?       | `1 >= 0` or `1 >= 1`| `0 >= 1`        |
| `<`        | Is less than?      | `0 < 1`             | `1 < 0`         |
| `<=`       | Is at most?        | `0 <= 1` or `1 <= 1`| `1 <= 0`        |

The evaluation of relational operators always results in a `bool` value.

It is important to pause and note the _equality_ of two values is tested with the `==` operator comprised of two equals symbols side-by-side. The "is NOT equal" operator has a surprising symbol in it, the exclamation point! The `!` symbol is commonly used in programming languages to represent the word "not".

For each of these operators with two different characters, such as `!=`, `>=`, and `<=`, the order of the characters matters. You could not write `=!`, `=>`, nor `=<`. Additionally, you cannot place any spaces between the two characters.

Comparing two numerical values works as you would expect. Comparing two `str` values using relational operators can be surprising. The comparison uses each character of the string's ASCII values, in order, and is thus case-sensitive in a surprising way.

~~~ {.plaintext}
>>> "UNC" > "Duke"
True
>>> "UNC" > "duke"
False
~~~

If the above result is perplexing to you, recall from the previous lesson that every character has a numerical value associated with it. Lowercase characters have higher numerical representation than uppercase characters, which leads to this result. Generally, when comparing strings for alphabetization purposes, it makes sense to first convert each string to all lower or uppercase letters, which you will learn how to do in due time. This is beyond our concern for now, just recognize comparing two `str` values with relational operators can lead to surprising results.

### Operators on Other Types

You will encounter and learn additional operators in the coming weeks. For example, equality and inequality operators for comparing two objects with one another, logical operators for forming complex logical expressions, and more.

Operators have specialized syntax, the symbols such as `+`, `**`, and so on, and an object's _type_ decides whether that operator is defined for that type and what the meaning of it is. We started with numerical operators because you have years of experience with their inspiration. When you later get to _invent your own types_, _you_ can decide whether to define meaning for these operators or not.

## Variable Access

A variable is a names you associate with a block of memory that refers to an object. Variables are so important they will have a special lesson on their own just after this one. They are worth demonstrating briefly, though, in conjunction with the operators shown above.

Follow along with this example where you establish an `int` variable named `x`, initially bind it to a value of `110`, and then later rebind it to a different value. In between, you can use the name `x` in expressions, called **variable access expressions**. A variable access will evaluate to the _last value bound to the variable's name_.

~~~ {.plaintext}
>>> x: int = 110

>>> x
110

>>> x * 2
220

>>> x * x
12100

>>> x = 3

>>> x
3

>>> x * 2
6

>>> x * x
9
~~~

Notice the single `=` symbol does not mean the same as what it does in mathematics! It can be read as _"is bound to a value of"_. The full details of variables will be explored in the next lesson!

## Constructor Expressions for Type Conversions

For types of data that do not have built-in literal syntax, meaning types other than `str`, `int`, and so on, you need a way to _construct_ a new object of that type. Each _type_ is defined by a _class_ that has a _constructor_. By convention, the name of the _constructor_ is the same as the _class_.

Although types such as `str` and `int` have literal syntax, they also have constructor functions. Each of the primitive types' constructor functions can be used to convert a value from another type to it. This is best explored through following along:

~~~ {.plaintext}
>>> str
<class 'str'>

>>> type("110")
<class 'str'>

>>> int("110")
110

>>> type(int("110"))
<class 'int'>

>>> int
<class 'int'>

>>> type(110)
<class 'int'>

>>> str(110)
'110'

>>> type(str(110))
<class 'str'>
~~~

Notice the names, or **identifiers**, `int` and `str` are defined as classes which you can think of as classifications of a type of data. Each class has a constructor we can make use of as shown. In the example of `int("110")`, notice the `int` constructor function is able to take in a `str` and evaluate to an `int` object. Similarly with the `str` constructor, notice we gave it an integer and it evaluated to a `str`. Often you will have data in one type and need to convert it to another type for a different purpose and, in Python, this is how you can.

When a constructor call expression evaluates, it always evaluates to the type of the object it created (and thus it's name!). So `str(123)` evaluates to a `str` typed object.

Constructor call expressions are more commonly used to construct objects of types that do not have literal syntax. We'll encounter these soon in Python's vibrant world of types and in those we define ourselves! 

## Function Call Expressions

Programs tend to be broken down into smaller "subprograms" called functions. Some of these are built into the programming language itself, others you will write on your own! The name function is similar in spirit to its mathematical counterpart, but not quite the same. A function can often be thought of as a procedure, or a named algorithm, which you can use to carry out some complex operation more simply. Let's explore a few function examples and discuss their intuition:

~~~ {.plaintext}
>>> round(3.5)
4

>>> round(3.4)
3

>>> from random import randint

>>> randint(0, 100)
93

>>> randint(0, 100)
10

>>> from math import sqrt

>>> sqrt(2)
1.4142135623730951
~~~

In the first examples, the built in `round` function rounded a `float` up or down based on common rounding rules. 

Next we _imported_ a function named `randint` from the `random` package. The concepts of packages and importing will be discussed soon, but the short story is many functions and types are organized into their own packages to keep related concepts separate from unrelated concepts. In this case, the `randint` function took two inputs in the form of two `int` values, and when the `randint` function evaluated it returned a random `int` value between those two numbers. Try evaluating the same function call expression multiple times (press the up key and `Enter`) and notice random numbers are returned. We will have a lot of fun with random number generation in this course!

Lastly, as one more example, notice we imported the `sqrt` function, short for square root, from the `math` package, and used it to calculate the square root of two. Each if the lines you typed in, except for the import lines, were _function call expressions_.

In the weeks ahead, function call expressions and how you can define your own functions will be explored in full depth!

## Method Call Expressions

Some **types** of _objects_ have built-in capabilities called **methods**. Of the types we've seen, this is true of `str` objects. A **method** is a special function associated with an object. Exactly how method calls work is for later in the course, so we will not spend much time here, but since they're commonly used with `str` objects it's worth demonstrating briefly now.

~~~ {.plaintext}
>>> "hello, world".upper()
'HELLO, WORLD'

>>> msg: str = "hello, world"

>>> msg.capitalize()
'Hello, world'

>>> msg.startswith("help") 
False

>>> msg.startswith("hello") 
True

>>> msg
'hello, world'
~~~

Each of the expressions you wrote that involved a `str`, or variable access that evaluated to a `str`, followed by a `.` and then what looks similar to a _function call_ was a _method call expression_. As another foreshadowing, the use of a `str` variable named `msg` was included.

To read more about the `str` methods available in Python, you are encouraged to read through the [String methods](https://docs.python.org/3/library/stdtypes.html#string-methods) section of the official documentation.

## Objects, Types, and Expressions

This was a high-level, whirlwind tour of some of the different kinds of expressions you will encounter when programming. As the course continues, each will be covered in full depth so that you know not only how to recognize them, but also what is happening behind the scenes to make them possible.

The big take away idea of this lesson, in conjunction with the previous on types, is that _types_ are fundamentally important to the practice of programming. All of the data your programs will process, which you can think of as objects in your computer's memory, have a specific type. That type is important because it guides the kinds of expressions you can form and thus the steps of computation you can carry out. As you grow more comfortable programming you will gain confidence in knowing what kinds of expressions you need to make use of to achieve your creative vision.

In the next lessons you will learn more about variables, followed by information on logical data types, and how to write programs that respond differently based on user input. You'll be making fun, little text-driven games sooner than you expect! In the meantime, you are encouraged to explore and tinker within your interactive Python sessions to explore expressions and data types.