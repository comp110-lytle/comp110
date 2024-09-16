---
title: Practice Memory Diagram
author:
- Created by Viktorya Hunanyan
- Solution by Lizzie Coats
page: lessons
template: overview
---

# Snippet

```python
    def count_digits(text: str) -> int:
        """Count the number of digits in a given text string."""
        index: int = 0
        digit_count: int = 0
        digits: str = "0123456789"
        
        while index < len(text):
            char: str = text[index]
            is_digit: bool = False
            
            digit_index: int = 0
            while digit_index < len(digits):
                if char == digits[digit_index]:
                    is_digit = True
                digit_index += 1
            
            if is_digit:
                digit_count += 1
            
            index += 1
        
        return digit_count

    def main() -> None: 
        """Main entry point of the program."""
        text: str = "abc123"
        result: int = count_digits(text)
        print(result)

    main()
```

# Solution

<img class="img-fluid" src="/static/practice-mem-diagrams/num_count.jpg" alt="Image Description Here"  />

## Video
*(Video Coming Soon)*

## Image Description
*(Coming Soon)*