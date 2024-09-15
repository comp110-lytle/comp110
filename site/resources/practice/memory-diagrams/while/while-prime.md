---
title: Practice Memory Diagram
author:
- Created by Viktorya Hunanyan
- Review and Solution by Julia Guzzo
page: lessons
template: overview
---

# Snippet

```
    def check_number(num: int) -> str:
        """Returns prime status of the number."""
        if is_prime(num=num):
            return str(num) + " is a prime number"
        else:
            return str(num) + " is not a prime number"

    def is_prime(num: int) -> bool:
        """Checks whether or not a number is prime."""
        if num <= 1:
            return False
        divisor = 2
        while divisor <= num // 2:
            if num % divisor == 0:
                return False
            divisor += 1
        return True

    def main() -> None:
        """Main entrypoint into the program."""
        print(check_number(num=13))

    if __name__ == "__main__":
        main()
```

# Solution

<img class="img-fluid" src="/static/practice-mem-diagrams/while-prime-soln.jpg" alt="Image Description Here"  />

## Video
*(Video Coming Soon)*

## Image Description
*(Coming Soon)*