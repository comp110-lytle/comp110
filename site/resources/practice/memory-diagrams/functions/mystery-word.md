---
title: Practice Memory Diagram
author:
- Created by Viktorya Hunanyan
page: lessons
template: overview
---

# Snippet

<pre>
<code class="python">   def get_starting_point(word: str) -> int:
    return int(len(word) / 3)

def shift_position(index: int) -> int:
    return index - 1

def extract_character(word: str, index: int) -> str:
    return word[index]

def main(word: str) -> None:
    print("The hidden character is: " + extract_character(word, shift_position(get_starting_point(word))))

main(word="mystery")
</code></pre>

# Solution

*(Coming soon)*