---
title: Unicode, Emoji, Escape Sequences, and f-Strings
author:
- Kris Jordan
page: lessons
template: overview
---

As you now understand, strings are a data type for representing textual data.

So far, you have learned how to:

1. Write `str` literals, such as `"hello, world"`
2. Convert other types of values _into_ to `str` values, `str(110)` evaluates to `"110"`
3. Build strings through concatenation `"COMP" + str(110)`, which evaluates to `"COMP110"`

But what, _really_, are strings?

In this lesson, we will deepen on our understanding of strings. We will zoom in on strings, narrowing in on _individual characters_ and ask what _really_ is a character?

## Characters

Textual data is made up of a sequence of **characters**. For example, the `str` `"hello"` comprises the characters `'h'`, `'e'`, `'l'`, `'l'`, `'o'`. For the computer to _represent_ a string, it must also be able to work with _characters_. 

The distinction between _characters_ and _letters_ is noteworthy. Textual data is more than _letters_! There are numbers, spaces, tabs, new lines, many lettering sets 爱, and even emoji 🤠. Each is a _character_. Strings are _sequences_ of **characters**. So, what are _characters_?

Like an onion, every _abstraction_ has _layers_. If you cut too many layers into this onion you will leave the realm of computer science and enter the fields of physics and philosophy. You might also cry. So let's peel back only one more layer.

What a _character_ is depends on how it is represented. On your screen, most characters present visually as a shape or space, but some do not. A _single character of data_ can be represented in many different visual forms by changing fonts and you can accept that it's still the _same, single character of data_ just viewed in a different way. [Icon fonts such as wingdings](https://en.wikipedia.org/wiki/Wingdings) intentionally present characters, even letters, as icons very different from their traditional form. Changing the font back and forth between an icon font and a traditional one doesn't change the underlying character data, only how we see it and interpret it.

Inside a computer's digital systems, chracters are represented as coded patterns of 0s and 1s, or binary. There is a generally agreed upon "encoding" of character data in computing systems called the [American Standard Code for Information Interchange abbreviated to ASCII](https://en.wikipedia.org/wiki/ASCII) that was _designed_ by humans, and agreed upon, in the 1960s. As you learned, the character `A` has the binary code `01000001`. Numerical data, such as `int` values, can also be represented in binary system. It so happens that the _same_ binary pattern `01000001` can be interpretted as the `int` value `65`. Since binary is outside our concern, the main takeaway here is every character has a corresponding `int` value.

### Use the `ord` function to find a character's `int` code

Python's built-in function `ord`, short for "ordinal" which is the order in which characters are defined, takes a single-character string as an input parameter and returns the `int` representation of the character's binary code.

~~~plaintext
>>> ord("A")
65
>>> ord("B")
66
>>> ord("Z")
90
>>> ord("a")
97
>>> ord("b")
98
>>> ord("z")
122
~~~

There are a few important observations to make in the example above. 

First, notice that the codes for letters _relative to one another_ is logical. In the English alphabet, A is followed directly by B, just as in integers 1 is followed by 2. Similarly, A's integer ASCII code is 65 and B's is 66. The specific numbers of either are not important, but their relationship to one another is.

~~~plaintext
>>> "Duke" < "UNC"
True
>>> "unc" > "duke"
True
>>> "duke" > "UNC"
True
~~~

The first two examples are reasonable, but the third comes as a surprise! How is "duke" greater than "UNC"? When `str` values are compared in Python, and most programming languages, the `ord` values are compared relative to one another. The `ord` of lowercase letters is higher than uppercase letters in ASCII. Just as when you order information alphabetically, the first letter is compared and, if the same, the following character, and so on. (This is an algorithm!) String comparisons are case-sensitive. (For case-insensitive comparisons, you would first use `str`'s [`casefold` method](https://docs.python.org/3/library/stdtypes.html#str.casefold).)

### Use the `chr` function to convert an `int` to a character

Since characters and their integer codes are two sides of the same coin, you can freely go back and forth:

~~~plaintext
>>> chr(65)
'A'
>>> chr(122)
'Z'
>>> chr(ord('A'))
'A'
>>> ord(chr(65))
65
~~~

The `chr` function is built-in to Python, takes an `int` parameter, and returns the single character representation as a string.

### What about foreign languages and emoji?

When ASCII was decided in the 60s, it was a technical achievement to include _both_ lower and uppercase letters in the standard. Emoji, and much more importantly large alphabet languages such as Chinese, were not possible until later. As additional characters were added to international standards, the set of total characters possible expanded well beyond ASCII's initial 127 character specification.

For example, try the following in the REPL:

~~~plaintext
>>> chr(129312)
~~~

Hold on to your saddles, because we're about to go on a little adventure. This is a bit outside of the scope of your concerns in COMP110, but to make use of Emoji in our programs (which is of utmost importance) there's just a little more to the story to reveal.

### Putting a `hex` on large integers

The decimal system is base-10, meaning we have 10 digits ranging from 0 through 9. Notice you grew comfortable with a 0-indexing numbering scheme in elementary school! Consider the base-10 value `90`. It can be interpretted in a binary, a base-2 numeral system as `01011010`. Binary is _base 2_ and has only 2 digits: 0 and 1. It can also be represented in a hexademical, a base-16 numeral system, with `5A`. Hexadecimal is _base 16_ and has 16 digits, 0-9 followed by A-F which correspond to the decimal values of 10-15. Computer scientists love hexadecimal because each single digit corresponds to four binary digits. Notice that in the example: `01011010`, which is 8 binary digits, is equivalent to `5A`.

Python has a built-in `hex` function for converting to its representation. The `0x` in front of the hexadecimal notation can be ignored and is case insensitive.

~~~plaintext
>>> hex(90)
0x5a
~~~

When looking up the codes for emoji or characters in other languages, they will tend to be presented to you in a _hex_ format, such as [on this web site](https://unicode.org/emoji/charts/full-emoji-list.html). You will notice in the _code_ column, there is a format of `U+1F920`. The `U+` tells you this is Unicode, a more modern international character encoding standard than ASCII. The `1F920` is a hexadecimal representation of the code for the cowboy emoji. In Python, you can use such a Unicode character in your strings as follows:

~~~plaintext
>>> print("The \U0001F920 rides a \U0001F40E!")
The 🤠 rides a 🐎!
~~~

The leading backslash begins an escape sequence, which will be discussed in depth shortly. The `U` is an indication that what will follow is an 8-digit hex representation of a unicode character. Then, to encode `1F920`, we must add three leading `0`s for padding because 8 hex digits are expected.

It is worth taking a moment to appreciate that Python is doing a proper job of treating those emoji each as an individual item in our sequence of characters.

~~~plaintext
>>> emoji: str = "\U0001F920\U0001F40E"
>>> print(emoji)
🤠🐎
>>> len(emoji)
2
>>> emoji[0]
🤠
~~~

## String Escape Sequences

In the previous example, the backslashes in the string `"\U0001F920\U0001F40E"` are signalling something special is about to follow the backslash. In this case, what follows is a `U` which hints "8 hexidecimal digits encoding a single unicode character" will follow the `\U` "escape sequence".

There are other _escape sequences_, as well. Here are some common ones:

| Escape Sequence | Meaning                  |
|-----------------|--------------------------|
| `\"`            | Double quote (`"`)       |
| `\'`            | Single quote (`'`)       |
| `\t`            | Tab                      |
| `\n`            | New Line                 |
| `\Uxxxxxxxx`    | 32-bit unicode character |
| `\\`            | Backslash (`\`)          |

Escape sequences in string literals begin with a backslash. 

How can you _use_ a double quote character in a string surrounded in double quotes? With the first escape sequence above! For example, the string literal `"The computer said, \"Hello, world.\""` will evaluate to the characters `The computer said, "Hello, world."` The `\"` escape sequence, when evaluated, results in a single backslash character.

The last entry in the table is also interesting. If backslashes are how we begin writing an escape sequence in a string literal in Python... _how do we write a single backslash?_ By writing two backslashes back-to-back, of course! The first backslash begins an escape sequence, the second backslash causes the sequence to evaluate to a single backslash.

## f-Strings "Format" Strings

Zooming back out to thinking of strings at a high-level, by now you have used concatenation enough to recognize that concatenating strings can be a lot of work! Especially if you are concatenating non-string values in the middle of a larger string. Modern Python has a special string literal called a _format string_ or _f-string_ for short, that makes this much easier. Consider the following examples:

~~~plaintext
>>> course: int = 110
>>> print("I am in COMP" + str(course) + " right now!")
I am in COMP110 right now!
>>> print(f"I am in COMP{ course } right now!")
I am in COMP110 right now!
~~~

A key distinction between a regular string and an f-string is that it begins with the letter `f` preceeding its quotes. Notice the difference of `f"Hi"` and `"Hi"`, where the former is an `f` string.

Inside of an f-string you can write an _expression_ inside of curly braces and it will get substituted with the expression's value when the string literal is evaluated. Spaces inside of the curly braces are ignored. This is especially handy if you are building a string with multiple variables being concatenated together. Consider the difference of:

~~~plaintext
>>> name: str = "Lauren"
>>> age_turning: int = 21
>>> print("Hello " + name + ", you're almost " + str(age_turning) + "!")
Hello Lauren, you're almost 21!
>>> print(f"Hello {name}, you're almost {age_turning}!")
Hello Lauren, you're almost 21!
~~~

There are other powerful things format strings can do, too, but they are outside the scope of this course. If you'd like to learn more [this guide](https://realpython.com/python-f-strings/) covers many useful cases. Other modern programming languages are adopting variations of this same concept which you may also hear referred to as _string interpolation_.