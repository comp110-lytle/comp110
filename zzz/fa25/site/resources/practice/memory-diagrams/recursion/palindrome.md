---
title: Practice Memory Diagram
author:
- Benjamin Eldridge
page: lessons
template: overview
---

# Snippet

Challenge Memory Diagram: Create a memory diagram for the following code snippet. Identify which lines that base case(s) or recursive case(s) occur on.

```py
"""Recursion practice with palindromes."""

def is_palindrome(word: str, index: int) -> bool:
    """Returns True if word is a palindrome and False otherwise."""
    if index >= int(len(word) / 2):
        return True
    elif word[index] == word[len(word) - (index + 1)]:
        return is_palindrome(word=word, index=index + 1)
    else:
        return False

def main() -> None:
    """The main function."""
    print(is_palindrome(word="noon", index=0))
    print(is_palindrome(word="110", index=0))

main()
```

# Solution

The base cases occur on lines 5-6 and 9-10. If you reach the base case on lines 5-6, that means you made it through the whole `word` without finding any differences between letters that should be the same, so you can return `True` as the final result. If you make it to lines 9-10, that means a difference was found between letters that should be the same, so `word` is not a palindrome. The recursive case is on lines 7-8.

<img class="img-fluid" src="/static/practice-mem-diagrams/palindrome.png" alt="Memory diagram for palindrome example."  />

## Image Description 
*(Coming Soon)*
