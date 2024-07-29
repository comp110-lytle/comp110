---
title: Chapter 1 - The Bell Tower
author:
- Ezri White
- Marc Lewis
- Kaki Ryan
page: logistics
template: overview
---

<script>
    document.body.classList.add('halloween-mode'); 
    document.getElementById("mode-switch").classList.add('hidden')
</script>

<p style="font-size: xx-large; color: rgba(255, 132, 32, 0.909);">🎃 Congratulations you have discoved a clue! 🎃</p>

> Take a picture at this location with your fellow detectives and fill out <a href="https://airtable.com/shrzczOIak59I0cyx" target="blank">THIS FORM</a> to get onto the leaderboard! Make sure to do this immediately and for every new chapter you discover!

<p style="color: rgba(255, 132, 32, 0.909);">You better find Kaki quickly! Review sessions have ground to a halt!</p>

## The CLUE 🔎

Dl tpnoa ullk av ylabyu av aol jyptl zjlul... Zpaalyzvu pazlsm. Mylk Iyvvrz pz hsdhfz dhajopun vcly aol ibpskpun... myvt aol ivaavt msvvy. Wlyohwz ol zhd zvtlaopun? Ahrl h svvr ilulhao opt huk zll pm ol slma bz huf jsblz.

## The TASK 🕵️

It seems that whoever left this clue wanted it to be hard to read, we will have to decode it again. And what is with the number next to the clue? Weird... sometimes caesar ciphers shift by more than one character, perhaps that is it. There also is both uppercase and lowercase letters in this clue. Our cipher decoder will have to handle that too:

### 0. Handling all characters

We want our new and improved Caesar Cipher to be able to handle both uppercase and lowercase letters. We also want our decoder to leave numbers, spaces and punctuation untouched. Lucky for us, python has several built-in `str` methods that can help us check the case of character and determine if a character is part of the alphabet or not.

#### `isupper` and `islower`

Python has a built-in `str` method, `isupper`, that returns `True` if every alphabetic character in the `str` is uppercase. Since we are only dealing with single-length `str`s in `encode_char` and `decode_char` this method will definitively tell us if we are looking at a capitalized letter or not. You can try the following code out in a REPL

~~~ {.plaintext}
>>> "c".isupper()
False
>>> "D".isupper()
True
~~~

Unsuprisingly, there is also an `islower` method that does just the opposite.

~~~ {.plaintext}
>>> "c".islower()
True
>>> "D".islower()
False
~~~

#### `isalpha` function

Python has a built-in `str` method, `isalpha`, that returns `True` if every character in a given `str` is alphabetic. Since we are only dealing with single-length `str`s in `encode_char` and `decode_char` this method will definitively tell us if we are looking at a letter or some other character such as a number or punctionation. You can try the following code out in a REPL

~~~ {.plaintext}
>>> "$".isalpha()
False
>>> "a".isalpha()
True
>>> " ".isalpha()
False
>>> "A".isalpha()
True
~~~


### 1. Refactoring `decode_char`

With the built-ins methods shown above and our knowledge of `if` statements, we have the tools under our belt to update our `_char` functions to handle any character A-Z or a-z and ignore non alphabetic characters. 
The only difference between encoding an uppercase vs. lowercase character is the `int` value used to normalize our single-length `str`. In the first part of the project we used `65` since that is the ASCII code for `A`. Now, we still want to use `65` for uppercase letters, but in the case of an lowercase character we want to use `97`. This might seem random but if we look up `a` here: <https://en.wikipedia.org/wiki/ASCII#Printable_characters> we see that its code is `97`.

1. Copy and Paste your original `decode_char` function and rename it to `decode_any_char`.
2. Change the implementation in your pasted code to handle both lower and uppercase letters.
3. Change the implementation to ignore non alphabetic characters.
3. You can check if it is working with the following function calls:

~~~
decode_any_char("A") --> returns "Z"
decode_any_char("B") --> returns "A"
decode_any_char("O") --> returns "N"
decode_any_char("a") --> returns "z"
decode_any_char("b") --> returns "a"
decode_any_char("o") --> returns "n"
decode_any_char(" ") --> returns " "
decode_any_char(",") --> returns ","
decode_any_char("&") --> returns "&"
~~~

Note: This version of the function will not be tested by itself but make sure to get this working before refactoring again in step 2.


### 2. `decode_char_by_shift` function

Our decoder also needs to be able to shift by any given number of letters to handle this message. Write a new function called `decode_char_by_shift` that takes an additional `int` argument to shift by. You should be able to copy most of the functionality from your `decode_any_char` function


#### Functional Requirements -- `decode_char_by_shift`

1. Have a function with the following signature:
   1. Name: `decode_char_by_shift`
   2. Arguments: a `str` that can be assumed to be single-length
   3. Returns: a single-length `str` 
2. The new `str` should be the parameter given shifted one letter to the left in the alphabet, per the mapping shown above.
3. Your function should make use of the `ord` and `chr` built-in functions.
4. Ensure your function has the expected behavior for both uppercase and lowercase characters.

### 3. `decode_str_by_shift` function

The last step is to update the `decode_str` function to handle `str`s of any length, any shift number and upper case or lowercase letters. After this, your Caesar Cipher decoder will be powerful enough to handle any word you give it!

To process a _sequence_ using a loop, consider that the _subscription notation_ expects an _integer expression_ within the square brackets. For example, the following snippet prints every character of a `str` on its own line:

~~~ {.plaintext}
letters: str = "abcdefghijklmnopqrstuvwxyz"
i: int = 0
while i < len(letters):
   letter: str = letters[i]
   print(letter)
   i = i + 1
~~~

Notice using the `len` function to determine the length of _any string_ allows this loop to process the `letters` `str` no matter its contents. You will need to make use of a similar strategy for decoding a `str`.

#### Functional Requirements -- `decode_str_by_shift`

1. Have another function with the following signature:
   1. Name: `decode_str_by_shift`
   2. Arguments: a `str` of any length and an `int` to shift by.
   3. Returns: a `str` with the same length as the argument.
2. The result of this function should be the parameter `str` with each letter shifted to the left by the given shift argument.
3. Call `decode_char_by_shift` inside this function for each letter of the parameter.
4. Use a `while` loop with a counter variable to complete this function.

### 4. Testing your program

To check that your functions work as expected, you can load your `caesar_cipher` file into a REPL by opening up a new `REPL`, and then running `from projects.mystery.caesar_cipher import decode_char_by_shift, decode_str_by_shift`. From here you can practice calling your functions and seeing if the results match what you expected.

~~~
decode_char_by_shift("c", 3) --> returns "z"
decode_char_by_shift("F", 14) --> returns "R"
decode_char_by_shift("z", 26) --> returns "a"
decode_char_by_shift("%", 1) --> returns "%"
~~~

~~~
decode_str_by_shift("Cqn Dwrenabrch xo Wxacq Ljaxurwj", 9) --> returns "The University of North Carolina"
decode_str_by_shift("FcBAtRobO!!", 13) --> returns "SpONgEboB!!"
~~~

If you are convinced that your decoding functions are working, try decoding the clue. Perhaps it is a clue to where there may be more information.

## 5. Make a Backup Checkpoint "Commit"

Follow the instructions on the project introduction page to make a backup commit.

