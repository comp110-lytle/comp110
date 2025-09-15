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
1     """Recursion practice with palindromes."""
2 
3     def is_palindrome(word: str, index: int = 0) -> bool:
4         """Returns True if word is a palindrome and False otherwise."""
5         if index >= int(len(word) / 2):
6             return True
7         elif word[index] == word[len(word) - (index + 1)]:
8             return is_palindrome(word=word, index=index + 1)
9         else:
10            return False
11
12    def main() -> None:
13        """The main function."""
14        print(is_palindrome(word="noon"))
15        print(is_palindrome(word="110"))
16
17    main()
```

# Solution

The base cases occur on lines 5-6 and 9-10. If you reach the base case on lines 5-6, that means you made it through the whole `word` without finding any differences between letters that should be the same, so you can return `True` as the final result. If you make it to lines 9-10, that means a difference was found between letters that should be the same, so `word` is not a palindrome. The recursive case is on lines 7-8.

<img class="img-fluid" src="/static/practice-mem-diagrams/palindrome.png" alt="Memory diagram for palindrome example."  />

## Image Description 
*(Coming Soon)*
