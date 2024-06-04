---
title: Chapter 3 - The Library
author:
- Ezri White
- Marc Lewis
page: logistics
template: overview
---

<script>
    document.body.classList.add('halloween-mode'); 
    document.getElementById("mode-switch").classList.add('hidden')
</script>



<p style="font-size: xx-large; color: rgba(255, 132, 32, 0.909);">🎃 Congratulations you have discoved a clue! 🎃</p>

> Take a picture at this location with your fellow detectives and fill out <a href="https://airtable.com/shrzczOIak59I0cyx" target="blank">THIS FORM</a> to get onto the leaderboard! Make sure to do this immediately and for every new chapter you discover!

<p style="color: rgba(255, 132, 32, 0.909);">Lily is really upset and hungry.</p>

## The CLUE 🔎

~~~ {.python }
 EMOJI_CIPHER = {'👽': 'a', '🔍': 'b', '🍁': 'c', '🎃': 'd', '💀': 'e', '😱': 'f',
                 '🥸': 'g', '🦄': 'h', '🌲': 'i', '🌵': 'j', '🌈': 'k', '⛸': 'l',
                 '👻': 'm', '💅': 'n', '🍭': 'o', '⛄': 'p', '🐟': 'q', '🕸': 'r',
                 '🍰': 's', '🐓': 't', '🌽': 'u', '🍂': 'v', '🔥': 'w', '🌺': 'x',
                 '💻': 'y', '🔦': 'z'}
~~~    

## The TASK 🕵️

### 0. Random Ciphers
Another common type of cipher is where letters are randomly chosen to represent other letters instead of evenly shifted like in a caesar cipher. This makes for a much tougher code to crack as there is no concrete pattern. 

Without a pattern, there must be a record of the encoded version of every letter in order to decode a given message. For our purposes a `dict` is the perfect structure to represent this. Below is an example of a random cipher represented with a dictionary:

~~~ {.python }
 RANDOM_CIPHER = {'s': 'a', 'v': 'b', 'd': 'c', 'c': 'd', 'l': 'e', 'w': 'f', 'p': 'g',
                  'e': 'h', 'k': 'i', 'b': 'j', 't': 'k', 'r': 'l', 'q': 'm', 'z': 'n',
                  'x': 'o', 'g': 'p', 'o': 'q', 'j': 'r', 'y': 's', 'n': 't', 'a': 'u',
                  'u': 'v', 'f': 'w', 'i': 'x', 'h': 'y', 'm': 'z'}
~~~    

An example of a message decoded using the above cipher is as follows:

~~~ {.plaintext}
elrrx fxjrc -> hello world
~~~

Note: In this representation, for each key-value pair in the dictionary, the key represents the encoded letter and the value is the decoded letter.

A random cipher is typically created by just randomizing which letter represents which, but we could also create a random cipher by assigning any type of data where there was at least 26 unique options to each letter. One type of string data that fits these requirements are emojis. The dictionary at the top of this page displays a random cipher made with emojis.

### 1. `decode_random_cipher` function

While you could attempt to hand decode a random cipher messager it becomes tedious after a few words. Instead we will write a generic function that can take a given random cipher that pairs a `str` to each letter and use it to decode a given piece of encoded text.

#### Functional Requirements -- `decode_random_cipher`

1. Have a function with the following signature:
   1. Name: `decode_random_cipher`
   2. Arguments: a `dict[str, str]` that represents the random cipher and a `str` that is the text to be decoded
   3. Returns: a decoded `str` 
2. The new `str` should be the `str` parameter decoded using the given dictionary 
3. If a character in the encoded string is not a key in the dictionary leave it unchanged
4. You do not need to worry about uppercase versus lowercase letters in this function

### 2. Testing and using your program

To check that your functions work as expected, you can load your `random_cipher` file into a REPL by opening up a new `REPL`, and then running `from projects.mystery.random_cipher import decode_random_cipher`. From here you can practice calling your functions and seeing if the results match what you expected.

Remember that your function should be able to handle a normal random cipher or the emoji variation of it since they both use `str` data for the key. Here are some examples using both dictionaries as inputs:

~~~
decode_random_cipher(RANDOM_CIPHER, "azd") --> returns "unc"
decode_random_cipher(RANDOM_CIPHER, "elrrx fxjrc") --> returns "hello world"
~~~

~~~
decode_random_cipher(EMOJI_CIPHER, "🌽💅🍁") --> returns "unc"
decode_random_cipher(EMOJI_CIPHER, "🦄💀⛸⛸🍭 🔥🍭🕸⛸🎃") --> returns "hello world"
~~~

> HINT: Where have you recently seen a lot of emojis in an unexpected place?

### 3. Make a Backup Checkpoint "Commit"

Follow the instructions on the project introduction page to make a backup commit.