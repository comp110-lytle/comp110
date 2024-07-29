---
title: Chapter 0 - The Note
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

## Introduction

Last night a terrible crime was commited. Kaki was walking home from sitterson late at night and never made it home to her cat Lily. We know because Lily told us. She was last seen just outside of sitterson by her security class lab partner who found the following note when he left an hour later:

 > CFMMU PXFSX JOEPX

Having just learnt about caesar ciphers in security class, Kaki's lab parter had a sneaking suspician there was an encoded message in this odd set of letters. He gave us the following instructions for cracking the code: 

## The Caesar Cipher

We just learned about [Julius Caesar's cipher](https://en.wikipedia.org/wiki/Caesar_cipher#History_and_usage) and we can use it to _decode_ secret 5-letter strings. For example, the string `"HIPTU"` decodes to `"GHOST"`. The idea is each letter is replaced by a letter some offset away from it in the alphabet. For our purposes, we will assume an offset shift of 1. 

Thus, the mappings are:

~~~ {.plaintext}
A -> B
B -> C
C -> D
....
Y -> Z
Z -> A
~~~

Notice when `Z` is encoded it "wraps around" to `A`.

### ASCII Encoding and the `ord` function

Under the hood our computer uses numeric codes to represent characters, or `str`s of length one. The standard encoding is ASCII ("American Standard Code for Information Exchange") which uses 7 binary digits (0s and 1s) to reresent each character. You'll learn about this more in later classes, so no worries about the details here. The table of codes can be found here: <https://en.wikipedia.org/wiki/ASCII#Printable_characters>. In the table, the `Dec` column is the `int` value of each character and the `Glyph` column contains the character representation. Scroll down to `Dec` `65` to see the uppercase range.

For this exercise, you will make use of the built-in `ord`. The `ord` function is short for "ordinal" and it gives the numerical `int` ordering of a single-character `str` in ASCII. For example, the character `n` has corresponds to the `int` value `110` in ASCII per the table linked above. You can confirm this with the following demo code:

~~~ {.plaintext}
>>> character: str = "n"
>>> ascii_code: int = ord(character)
>>> print(ascii_code)
110
~~~

### Encoding a character and the `chr` function.

According to our cipher mapping, we want to encode each character with the letter following it in the alphabet. We can do this by  performing integer arithmetic on the `ascii_code`. 

Building on the previous example, we will encode the `character` variable, whose value is `n`, and store the result in `encoded_character`, whose value we expect to be `o`. 

The built-in `chr` function can be given an `int` ASCII code and return a `str` made of its corresponding character.

~~~ {.plaintext}
>>> character: str = "n"
>>> ascii_code: int = ord(character)
>>> encoded_ascii_code: int = ascii_code + 1
>>> encoded_character: str = chr(encoded_ascii_code)
>>> print(encoded_character)
o
~~~

Try running this code yourself in a REPL to make sure you are confident about what is going on!

What about if we have to wrap around? In the case of encoding `Z`, we can't just add 1 to get back to `A`. The character `Z`'s ASCII code is `90` while `A` is `65`.

Some clever arithmetic, in conjunction with our good friend the _remainder operator_ `%`, can help us achieve this! Since there are 26 uppercase letters, we can take the remainder of dividing _any number_ by 26 and are guaranteed for it to result in a value of `0` through `25`. This would be great if `A` was `0` and `Z` was `25`, because then `(25 + 1) % 26` would be `0` which is `A`! The problem is, uppercase ASCII codes begin at `65` with `A` and end at `90` with `Z`. For a fun challenge, pause here and see if you can figure out how we'll get around this conundrum.

Are you ready for the spoiler? Ok, here goes! An oft-used trick in situations like this, (this comes up in 3D graphics, too!), is we'll momentarily normalize our value so that `A` _is_ `0` and `Z` _is_ `25` by subtracting `A`'s ASCII value which is `65`. Then, we'll encode by adding 1 and performing the remainder operation, finally we'll denormalize by adding `A`'s ASCII value _back_ so that we once again have a number in the correct range for upper case letters. This modification still works for all letters in the alphabet, not just `Z`.

~~~ {.plaintext}
>>> character: str = "Z"
>>> ascii_code: int = ord(character)
>>> normalized_code: int = ascii_code - 65
>>> encoded_code: int = (normalized_code + 1) % 26 + 65
>>> encoded_character: str = chr(encoded_code)
>>> print(encoded_character)
'A'
~~~

Give it a try in a REPL to convice yourself these steps work for any uppercase `character`. No worries if this still seems a bit fuzzy or magical -- we are more worried about the function writing in the next two sections.

## 0. Pull the Skeleton ☠️ Code 

You will find the starter files needed by "pulling" from the course workspace repository. Before beginning, be sure to:

0. Be sure you are in your course workspace. Open the file explorer and you should see your work for the course. If you do not, open your course workspace through File > Open Recent.
1. Open the _Source Control View_ by clicking the 3-node (circles) graph (connected by lines) icon in your sidebar or opening the command palatte and searching for _Source Control_.
2. Click the Ellipses in the Source Control pane and select "Pull" from the drop-down menu. This will begin the pulling process from the course repository. It should silently succeed.
3. Return to the File Explorer pane and open the `projects` directory. You should see it now contains another directory named `mystery`. If you expand that directory, you should see the starter files for the Python programs in this exercise.


## 1. `decode_char` function


Now that we have learned how to encode a `str`, we want undo this operation and `decode` it. These next two functions will look *VERY* similar to the ones you wrote in Part 1. This is expected -- the main goal of this exercise is to get comfortable with the function writing process.

Define a function named `decode_char` that given a single-length `str` parameter returns the originial, unencoded version of that character.

Example function call:

~~~
decode_char("C") --> returns "B"
~~~

### Functional Requirements -- `decode_char`

1. Define a function with the following signature:
   1. Name: `decode_char`
   2. Arguments: a `str` that can be assumed to be single-length
   3. Returns: a single-length `str` 
2. The new `str` should be the parameter given shifted one letter to the left in the alphabet, per the mapping shown above.
3. Your function should make use of the `ord` and `chr` built-in functions.


## 2. `decode_str` function

We can now use our `decode_char` function to help us decode `str`s of length 5. Define a new function called `decode_str` that takes in a `str` parameter and returns the original, unencoded version of that `str`. 

Example function call:

~~~
decode_str("BCDEF") --> returns "ABCDE"
~~~

### Functional Requirements -- `decode_str`

1. Define another function with the following signature:
   1. Name: `decode_str`
   2. Arguments: a `str` that can be assumed to have a length of 5.
   3. Returns: a `str` of length 5.
2. The result of this function should be the parameter `str` with each letter shifted one to the left.
3. Call `decode_char` inside this function for each letter of the parameter.
4. Use `str` indexing to get the individual characters without looping. 

## 3. Testing and Decoding the Note

To check that your functions work as expected, you can load your `caesar_cipher` file into a REPL by opening up a new `REPL`, and then running `from projects.mystery.caesar_cipher import decode_char, decode_str`. From here you can practice calling your functions and seeing if the results match what you expected. Below are some function calls and their correct answers. 

~~~
decode_char("A") --> returns "Z"
decode_char("B") --> returns "A"
decode_char("O") --> returns "N"
~~~

~~~
decode_str("RVFFO") --> returns "QUEEN"
decode_str("UPQBA") --> returns "TOPAZ"
decode_str("XJUDI") --> returns "WITCH"
~~~

If you are convinced that your decoding functions are working, try decoding the note Kaki's Lab Partner has found. Perhaps it is a clue to where there may be more information.
 
 > CFMMU PXFSX JOEPX

## 4. Make a Backup Checkpoint "Commit"

As you make progress on this project, making backups is encouraged. Note that you do not have to make a backup in order to submit your work, though you are encouraged to before each submission so that you can revert back to a previous point in your project if you accidentally change something you did not intend to.

1. Open the Source Control panel (Command Palette: "Show SCM" or click the icon with three circles and lines on the activity panel).
2. Notice the files listed under Changes. These are files you've made modifications to since your last backup.
3. Move your mouse's cursor over the word _Changes_ and notice the + symbol that appears. Click that plus symbol to add all changes to the next backup. You will now see the files listed under "Staged Changes".
   - If you do not want to backup _all_ changed files, you can select them individually. For this course you're encouraged to back everything up.
4. In the Message box, give a brief description of what you've changed and are backing up. This will help you find a specific backup (called a "commit") if needed. In this case a message such as, "Progress on mystery project" will suffice.
5. Press the Check icon to make a _Commit_ (a version) of your work.
6. Finally, press the Ellipses icon (...), look for "Pull/Push" submenu, and select "Push to...", and in the dropdown select your backup repository.

## 6. Submission Instructions

To prepare your code for submission, be sure to add a docstring to your module (at the top of the file) and a global `__author__` variable set to a string which contains your 9-digit PID. 

Run `python -m tools.submission projects/mystery` to build your submission zip for upload to Gradescope. Don't forget to backup your work by creating a commit and pushing it to GitHub. For a reminder of this process, see the previous exercises.