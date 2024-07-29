---
title: Objects and Data Types
author:
- Kris Jordan
page: lessons
template: overview
site-branch: public
---

The term **object** has many meanings in programming, just as it does in real-life. The first and most fundamental definition is **an object is a typed unit of data in memory**. 

**Memory is your canvas and objects are your paint.** Understanding the fundamental types of data you can work with, and their capabilities, is the first step on your journey toward programming!

Let's zoom in a bit to explore memory more closely, before zooming our way out toward thinking in terms of _objects_ in memory.

## Bits and Bit Patterns

Your computer's memory is comprised of billions of electronic cells. These cells, called _transistors_ are now the most frequently manufactured device in history, with over 13 sextillion produced[^mosfet]! Each transistor has two states, _off_ or _on_. This is represented numerically as a **bit** whose value is either `0` or `1`. Despite `1` being the maximal value of a bit, notice there are _two_ possible values thanks to `0`. Unlike humans, **bits are binary**.

[^mosfet]: That's 13,000,000,000,000,000,000,000 transistors produced! <https://en.wikipedia.org/wiki/MOSFET>

You can form many unique patterns by _stringing_ bits together. For example, with two bits strung together, you can form four different **bit patterns**: `00`, `01`, `10`, and `11`. With three bits strung together, you can form eight different combinations: `000`, `001`, `010`, `011`, `100`, `101`, `110`, `111`. How many **bit patterns** can you form with four bits?

Each time you extend a bit pattern by another bit, you double the number of possible patterns. Thus, given any number of bits, you can calculate the possible unique patterns with the mathematical expression $2^{bits}$. With 8 bits, called a **byte** there are $2^8$, which _evaluates to_ 256, different patterns. Exponential growth is a powerful force! With only 64 bits, there are $2^{64}$ patterns, which _evaluates to_ 18,446,744,073,709,551,616 possibilities.

Humanity has settled on the decimal system as its defacto numbering system. Languages have their own alphabets for  textual data. There is an emergent universal _character set_ in emoji 🤠. As all of memory is the binary system of `0`s and `1`s, how can computers process these widely different _**types** of data_?

## Classification and Representation

A symbol will follow this question, what does the symbol mean? `V`

If you classify it as an English character, it _represents_ the letter "vee". Classified as a Roman Numeral, though, it _represents_ the number five. If you read it in the phrase, "I'm V excited!" it's an abbreviation of the word "very". Choosing to classify, and _interpret_, the simple symbol `V` as different types of data allows for _the same symbol_ to **represent** very different ideas.

Programmers decide to _classify_ each block of memory they use, or each _object_, as a specific **type** of data: numerical data, textual data, sequences of data, compound groupings of many types of data, and so on. In doing so, the same underlying bit patterns are interpretted to **represent** different ideas.

|  Binary Bit Pattern    | Number (Integer)   | Text (Character)              |
|-----------------------:|-------------------:|:------------------------------|
|             `00000000` | `0`                | `NULL (invisible)`            |
|             `00000001` | `1`                | `Start of Heading (invisible)`|
|             `00000010` | `2`                | `Start of Text (invisible)`   |
|             `00110000` | `48`               | `0`                           |
|             `00110001` | `49`               | `1`                           |
|             `00110010` | `50`               | `2`                           |
|             `01000001` | `65`               | `A`                           |
|             `01000010` | `66`               | `B`                           |
|             `01000011` | `67`               | `C`                           |
|             `01100001` | `97`               | `a`                           |
|             `01100010` | `98`               | `b`                           |
|             `01100011` | `99`               | `c`                           |

You can poke at this concept directly in an interactive Python session. To follow along, **open a new terminal session** and run the `python` program by typing it in and pressing enter. Each of the lines beginning with `>>>` is one where you will type in an expression and press enter for the Python interpreter to **evaluate**.

~~~ {.plaintext}
>>> int(0b01000001)
65

>>> chr(0b01000001)
'A'

>>> int(0b01000010)
66

>>> chr(0b01000010)
'B'

>>> int(0b01000011)
67

>>> chr(0b01000011)
'C'
~~~

You are encouraged to try other bit patterns! When you are done, evaluate the function call expression `quit()` in the interactive Python program.

Each line had its own _function call **expression**_. A _function call_ starts with a function's name, in these examples there were two functions used, both `int` and `chr`. The word `int` is short for _integer_ and `chr` short for _character_, which includes letters, numbers, punctuations, and other textual symbols. Following the function name are a pair of parentheses and inside the parenthesis are any pieces of input data the function needs, called _arguments_. In these examples, a single argument was given to the function calls, and each of the arguments was a bit pattern. In Python, and many other languages, bit patterns are denoted with a prefix of `0b` followed by the pattern of 0s and 1s. Each expression you wrote was **evaluated** by the Python interpreter and its resulting value was printed to the screen.

> Note: When working in an interactive Python interpreter, the evaluation of each expression is displayed, or "printed", back to you automatically. This is _great_ for messing around! This **will not** be the case when writing stored programs. There you would need to surround any expression you want displayed in a `print` function call, for example `print(chr(0b01000011))`.

**What an object's _bit pattern_ means or _represents_ is decided entirely by the _type_ of data you decide to _classify_ it as.** Thus, when programming in a high level language like Python, it is more important to understand the types of data you are working with than exactly how they are represented as bit patterns. This is one of the most important examples of data _abstraction_ in computer science: we will not need to concern ourselves with the details of these lower, bit-level concerns for quite some time[^systems-programming]!

[^systems-programming]: In later computer science courses you will encounter systems programming languages, as you work closer to the actual machine, and will learn in much more depth the various binary systems behind integer, floating point, ASCII/UTF-8 data, and more.

## Built-in Types

Programming languages offer many built-in data types for you to work with, typically including:

* numerical
    * integers
    * decimal numbers
    * complex numbers
* textual
* logical
* collections of many objects
    * sequences
    * sets
    * dictionaries

The names programming languages choose for these common data types, thier capabilities, and their limitations, are usually very similar. However, there will be subtle differences specific to each language. **When learning a new programming language, start by spending time understanding and exploring its built-in data types and their capabilities.**

## Primitive Data Types

Let's explore these common data types in the context of Python, starting with _primitive_ types which are some of the simplest available to you in a programming language.

### Literal Expressions and `type` inspection

How do you express the integer number one hundred ten in Python?  Quite _literally_! `110`

What about fifty percent represented as a decimal? Quite _literally_! `0.50`

What about the textual word _programming_? Quite _literally_! `"programming"`

The built-in, _primitive_ types of a programming language often have _literal_ syntax for constructing and representing objects directly in your programs. _(Notice: none of these examples involve any binary! Though, previously, you wrote a binary literal without knowing it. Abstraction for the win!)_ These are examples of **literal expressions**.

To learn the type _classification_ of any object in Python, you can use the built-in `type` function. Try it by starting `python` in a terminal, if you don't already have one running, and following along:

~~~ {.plaintext}
>>> 110
110

>>> type(110)
<class 'int'>

>>> type(211)
<class 'int'>

>>> 0.5
0.5

>>> type(0.5)
<class 'float'>

>>> "programming"
'programming'

>>> type("programming")
<class 'str'>
~~~

Each literal expression evaluates to _literally_ itself. There is no further evaluation necessary or possible in these expressions. You also certainly noticed the classifications of each object's type have peculiar names such as `int`, `float`, `str`, and `bool`. Let's address each individually.


### `int` - Integers

The built-in type `int` is short for _integer_. Integers are useful for counting and programs count more things than you'd expect! For example, the number of likes on your last social media post, the number of words in your paper, the number of walking steps in your activity tracker, the number of points scored in games, and so on.

In Python, an `int` literal is either a zero _or_ a nonzero digit followed by zero or more digits. So, `0`, `1`, `987654321`, and `2020` are all example `int` literals, but `0110` is not. For large numbers you cannot use commas to denote places, such as in _1,000_, but you can use underscores which are completely ignored. Thus, `1_000_000` is the same `int` value as `1000000`.

We'll explore the kinds of _capabilities_ an `int` object has shortly, but to connect them with your understanding of calculations, try asking the Python interpreter to _evaluate_ some _integer arithmetic expressions_:

~~~ {.plaintext}
>>> 110 * 2
220

>>> 1 + 2 * 3
7

>>> (1 + 2) * 3
9

>>> 1_234 + 1
1235
~~~

### `float` - Floating-point "Decimal" Numbers

Why not classify the _type_ of a decimal numbers, such as `0.25`, with a name like `dec` or `decimal`? Because they're not _exactly_ decimal numbers, if you need to be _very precise_ about it. The name `float` is short for _floating-point_.

Here's a perplexing, motivating example of _very subtle_ limitations of floating-point arithmetic versus true decimal arithmetic. Can you spot any _miniscule_ errors?

~~~ {.plaintext}
>>> 0.25 + 0.25
0.5

>>> 10.0 / 3.0
3.3333333333333335

>>> 0.1 + 0.2
0.30000000000000004
~~~

The exact reasons for these computations having a slight error, less than a trillionth, are beyond your concerns right now, but the intuition behind it, and for the name _floating-point_, is as follows. Let's imagine an elementary numbering system where you are given three digit placeholders to form a number with: 

${d.d} \times 10^{x}$

For the two $d$ digits, you can choose any digit between `0` and `9`. For the $x$ digit, you can also choose any digit between `0` and `9`, _and_ can choose for it to be positive or negative. _In reality, a `float` value has far more digits to work with than this, this is dramatically simplified for illustrative purposes._

What is the _largest_ number you can represent?

$9.9 \times 10^9$ which is 9,900,000,000!

What is the _smallest_ number you can represent?

$0.1 \times 10^{-9}$ which is 0.0000000001

That's a massive range of numbers considering you only needed 3 digits and a sign to represent each!

**What's the catch?** Try describing a limitation of this system on your own.

What is the second largest number you can represent?

The second largest number would be $9.8 \times 10^9$ or 9,800,000,000, that means there are 99,999,999 whole numbers between the largest and second largest that are impossible to represent using this system! More precisely, there are only 1,539 unique numbers this system can represent in the range between 0.0000000001 and 9,900,000,000! Your mathematics has taught you there are an infinite number of decimal numbers in this range!

The good news is modern floating-point precision numbers use 64-bits of precision and can thus represent $2^64$ different possible numbers. That's astronomically more precision (over 18 quintillion possible numbers!) than our toy system above, but it is not _infinite_ nor _arbitrary_ precision. The motivating examples demonstrated there are often very small round-off errors in floating-point arithmetic that can be ignored. However, if you find yourself writing software that has no room for small errors in precision (rockets, bank software, medical devices, and so on), you will want to invest more time in understanding the trade-offs of _floating-point_ numbers versus [slower, more specialized options available](https://docs.python.org/3/library/decimal.html) for handling precise, numerical data.

We will use `float` for numbers with decimal points without hesitation or concern moving forward. For our purposes in COMP110, and most purposes you will encounter in computing (apps, games, most data science applications) the exceedingly small amounts of "round-off error" pose no problems and will be ignored moving forward.

### `str` - Strings of Characters for "Textual" Data

The "textual" data type in Python is `str`, short for _**str**ing of characters_, which is common terminology across programming languages. Strings are used *all  the time* in modern programs! Every application you use makes use of string values. Anywhere you see a label, are able to type text in, and so on is made possible by strings.

Why not simply call it _text_? _Text_ often conveys a bias toward thinking in _words_ and _visible symbols_ like letters, whereas "characters" can be invisible (such as spaces, tabs, and new line breaks), non-"textual" (digits, code, special symbols, and so on), and from many different _character sets_ (Arabic, Chinese, English, Emoji, German, and so on).

There are a few different syntaxes for working with `str` literals, but we will default to choosing double quoted `str` literals, such as `"hello, world"`. The characters following the first double-quote character `"` begin the contents of the string value and the _matched pairing_ double quote ends the `str` value. You can also use single-quotes, such as `'hello, world'`, and the result is the same. Most programming languages use double-quoted strings, while some allow either or, so we'll settle on the syntax that's more generalizable.

If a `str` begins and ends with a double quote, how can you have a double quote within a string? To solve this thorny issue, programming languages have settled on a technique called _escaping_ which means placing a backslash character `\` before some character with special meaning. This is best demonstrated through tinkering in an interactive Python session:

~~~ {.plaintext}
>>> "The students rejoiced, \"we love programming!\""
'The students rejoiced, "we love programming!"`
~~~

Notice the backslashes disappeared! _Escape codes_ in `str` data only appear in the code you write and when that code is evaluated to become a true `str` object, the `\"` is interpreted as simply a `"`. Without the leading backslashes in this example, there would have been a syntactical error.

It is worth pausing to emphasize the characters of a string have no meaning in our program beyond simply being characters. For example, the string `"110"` may have only digit characters in it, but **it is not number** and you cannot do numerical computations with it. Try to and you will see some surprising results:

~~~ {.plaintext}
>>> "110" + "110"
'110110`
~~~

The add _operator_, when used with two `str` values, produces a third `str` value that is the first `str`'s characters immediately followed by the second's. The technical term for this operation is _concatenation_ which is a term that originates in the chemical concept of carbon atoms forming chained bonds with other carbon atoms. Here, characters are being "bonded" into a longer sequence.

#### A `str` is a _Sequence_ of Characters

Through your programming journey you will encounter many types of data that are considered **sequences** of simpler values. In fact, you already have! Notice a `str` is a sequence of characters. The ordering of these characters is important! There's a meaningful difference between "please" and "asleep", even though they share the exact same characters.

We will explore _sequences_ in much more depth soon, but while we are on the subject of `str` values, let's foreshadow a bit with some examples of how to access individual **items** in a sequence. In a `str` value, each item is a character.

~~~ {.plaintext}
>>> "str!"[0]
's'

>>> "str!"[1]
't'

>>> "str!"[2]
'r'

>>> len("str!")
4

>>> "str!"[len("str!") - 1]
'!'

>>> 110[0]
TypeError: 'int' object is not subscriptable
~~~

**Subscription** syntax is formed by pairs of square brackets following a compound value. The individual items in a sequence can be accessed by their _index_ inside of the square brackets. You can find the number of items in any sequence using the built-in `len` function. Notice the `str` value `"str!"` has a length of 4 because there are three letter characters followed by an exclamation point character. The quotes are not a part of the `str`'s contents once it is evaluated, they are simply how we denote `str` literals in our programs.

**Index numbering starts from 0**. This is true in Python, as well as in most general-purpose programming languages. It takes some comfort to get used to! The first _item_ in a sequence is always at index 0. In a sequence with 10 items, the last item's index is 9. Since the `len` function will return the number of items in a sequence, you can always find the last item's index by computing `len(sequence) - 1`.

Integers and floating-point values _are not sequences_, they are singular numerical values. Thus, you cannot subscript them like a `str`.

#### Docstrings are for documentation

A **docstring** is a special kind of string in Python used to document the programs you write. Typically you will write a _docstring_ at the top of every file describing its purpose. As we begin defining subprograms, or functions, you will also write _docstrings_ in them describing their purposes in plain English.

Docstrings are written for other humans to read, or for you to read in the future to help refresh the purpose of specific files and functions you authored. Rather than beginning and ending with a single double quote `"`, a docstring stands out because it begins and ends with **three** double quotes strung together. For example: `"""This is a docstring."""`

As your programs become more complex, using docstrings will become more important. For now, when working in a stored program, begin each file with a docstring describing its purpose.

### `bool` - Booleans

The built-in type `bool` is short for _Boolean_, named after its [inventor](https://en.wikipedia.org/wiki/George_Boole). Booleans are binary and must be one of two possible values: `False` or `True`. Notice there is a direct connection with the _binary_ digits `0` and `1`. When you are writing programs you will find `bool` values are **used when making logical decisions in code**. In the examples below, you see some examples of asking the Python interpreter to _evaluate_ two _boolean relationship expressions_ using the greater than `>` comparison operator. Relationship expressions allow you to form inquiries such as, "is one number greater than another?"

~~~ {.plaintext}
>>> True
True

>>> type(True)
<class 'bool'>

>>> type(False)
<class 'bool'>

>>> 110 > 101
True

>>> 110 < 101
False
~~~

Note that Python, like most programming languages, is _case-sensitive_. The words `true`, `tRuE`, and `TrUe` are **not** `bool` values. Only `True` and `False` are valid `bool` values in Python.


## An object is a typed unit of data in memory

In the opening of this lesson it was said, "an object is a typed unit of data in memory". There is a lot of information packed into that statement now that you know a bit more about memory and types! Types are important because they decide how data is interpreted and, as you will explore in the next lesson, inform how you can make use of the object and its capabilities. The operations you can perform on numbers, such as adding them or subtracting them, are different than the operations you can perform on strings. This is broadly true both in programming and the real world: when you have different types of objects you'll want to do different things with them.