---
title: String algos
author:
- Kris Jordan
page: lessons
template: overview
---

The Python programming language, along with _many_ other languages, have a special notation when accessing an individual _item_ in a sequence called _subscript notation_. This notation gives you the ability to ask a sequence for its "item at position _int index_". The _int index_ begins counting from `0`, such that the item at index `0` is the first item, the item at index `1` is the second item, and so on.

### Subscript Notation

_Subscript notation_ uses square brackets `[` `]` to surround an `int` _index_ expression. This notation follows a `str` expression. For example, `"abcd"[0]` evaluates to the character `'a'` and `"abcd"[1]` evaluates to the character `'b'`. Typically, you will subscript off of a variable storing a `str` and not a _string literal_. As an example, try the following in a Python REPL:

~~~text
>>> a_str = "abcd"
>>> print(a_str[0])
a
>>> print(a_str[3])
d
>>> print(a_str[4])
IndexError: string index out of range
~~~

Notice in the example above, if you ask for an index _beyond_ its maximum index it will lead to an `IndexError`.

### Use `len` to find a `str`'s length 

It's helpful to know _how many characters_ are in a `str`, to avoid writing code that leads to an `IndexError`. Python has a built-in `len` function that will tell you the "length" of any `str`.

~~~
>>> print(len("abcd"))
4
>>> message = "a b c"
>>> print(len(message))
5
>>> print(message[len(message) - 1])
'c'
~~~

Notice in the second example of `len` above the length of `str` `"a b c"` is `5`. Remember, our emphasis is on _characters_ and spaces are characters.

Also notice, since sequences begin indexing at `0`, the _last character's index_ is always one less than the length of the sequence.

As a bit of foreshadowing, both the _subscript notation_ and `len` will be used to work with many other sequences and collections of data beyond just strings.

### Using `int` Expressions in Subscript Notation

It was mentioned in passing above, but must be addressed with emphasis now, the index number **is an `int` expression**. Beyond simple `int` literal values, you can form any expression you'd like as long as it evaluates to an `int`. **This is a SUPER POWER!**

This means you can subscript with `int` _variables_, which is very common, but also `int` arithmetic _and_ function calls to functions that return an `int`. Let's focus on the former with an example:

~~~
>>> s = "asdf"
>>> i = 0
>>> print(s[i])
a
>>> i += 1
>>> print(s[i])
s
>>> i += 1
>>> print(s[i])
d
>>> i += 1
>>> print(s[i])
f
>>> i += 1
>>> print(s[i])
IndexError: string index out of range
~~~

Notice, since `i` is an `int` variable we can _access_ it from within the subscript notation of `s[i]`. Since we can _reassign_ new values to `i` while the program is running, that means we can control which index the expression `s[i]` refers to at runtime.

Also notice the same two statements are repeated and the effect was to move index-by-index through the characters of the string. When you find yourself writing repeating statements it is a strong indicator you can use a loop to achieve your goal. As you know, though, loops have a _test condition_ that ends the looping behavior. To loop over all items in a str, you can use its `len` as part of the loop condition.

~~~
>>> s = "hiya!"
>>> i = 0
>>> while i < len(s):
...     print(s[i])
...     i += 1
...
h
i
y
a
!
~~~

With this capability, you can write _algorithms_ that are guided by the individual _characters_ it is made of. For example, when a website checks your password to be sure it meets some criteria such as a minimum length and contains certain special characters, numbers, and letters... _you could now write that function_!

These same concepts of working with items in a sequence using subscript notation are applicable _far beyond_ just string data. In the near future we will learn about _lists_ which give you the ability to form sequences of items of _any type_ not just characters. The same syntax, concepts, and general patterns for thinking apply there, too.