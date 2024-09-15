---
title: Practice Memory Diagram
author:
- Created by Viktorya Hunanyan
page: lessons
template: overview
---

# Snippet

```python
    def count_characters(s: str) -> int:
        """Count the number of non-space characters in the string."""
        index: int = 0
        counter: int = 0
        while index < len(s):
            if s[index] != ' ':
                counter += 1
            index += 1
        return counter

    def analyze_string(s: str) -> str:
        """Analyze the string length and return a message about the string."""
        char_count: int = count_characters(s)
        if char_count > 10:
            return "The string is long and has " + str(char_count) + " characters."
        else:
            return "The string is short and has " + str(char_count) + " characters."

    def main() -> None:
        """Main entry point of the program."""
        test_string: str = "Hello, how are you doing today?"
        result: str = analyze_string(test_string)
        print(result)

    main()
```

# Solution
*(Solution Coming Soon)*

<!-- <img class="img-fluid" src="/static/practice-mem-diagrams/while-prime-soln.jpg" alt="Image Description Here"  /> -->

## Video
*(Video Coming Soon)*

## Image Description
*(Coming Soon)*