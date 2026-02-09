---
title: Quiz 01 Memory Diagrams
author:
- Alyssa Lytle
- Benjamin Eldridge
page: lessons
template: overview
---

# Memory Diagram Practice

## Conditionals

1. Trace a memory diagram of the following code listing.

```py
    def count(x: str) -> str:
        """Practice conditionals."""
        y: int = len(x)
        if y % 4 == 1:
            y = y * 2
        y = y - 6
        print(y)
        return(x[y])
        print(x[y])

    count(x="Hello")
```

<details>
<summary>SHOW SOLUTION</summary>

<!-- [Video](https://youtu.be/o73Rk9ni5Rc)

<img class="img-fluid" src="/static/assets/f23/conditionals-00-sol.png" alt="The memory diagram includes a column on the left titled Stack and a column on the right titled Output."  />  -->



</details>

2. Trace a memory diagram of the following code listing.

```py
    def xyz(x: int, y: str) -> str:
        """Practice conditionals."""
        z: str = str(x)
        if len(y) > 1:
            y = y * x
        else:
            y = "no"
        if x > 0:
            print(z)
        return y

    xyz(x=2, y="yo")  
```

<details>
<summary>SHOW SOLUTION</summary>

<!-- <img class="img-fluid" src="/static/assets/sp24/conditionals-01-sol.png" alt="The memory diagram includes a column on the left titled Stack and a column on the right titled Output."  />  -->



<!-- In the Stack section, under the label Globals, there are three variables displayed:
* Variable x with the value 2.
* Variable y with the original value "yo" crossed out and updated to "yoyo".
* Variable z with the value "1".

In the Output section, the following are displayed in a vertical sequence:
* The number 2.
* The string "yoyo" -->

</details>

3. Trace a memory diagram of the following code listing.

```py
    def g(a: int, b: int) -> None:
        """Practice conditionals."""
        if a > b:
            print(a-b)
        elif b < 10:
            print(b/a)
        else:
            print(a+b)
        print(b)

    g(a=2,b=6)
```


<details>
<summary>SHOW SOLUTION</summary>

<!-- <img class="img-fluid" src="/static/assets/f23/elif-00-sol.png" alt="The memory diagram"  />

*Image Description:*
The memory diagram is divided into two sections: Stack and Output.

In the Stack section, under the label Globals, there are two variables:
* Variable a with the value 2.
* Variable b with the value 6.

In the Output section, two values are shown in a vertical sequence:
* The string "3.0".
* The string "6", which is the value of variable b. -->

</details>


## Recursion

Note: The following questions are more challenging than what will be on the quiz, especially the second one, in order to help you be very well prepared to tackle similar questions in a quiz environment. Attempting the first question is highly recommended, but the second question should be treated as optional additional practice.

1. Create a memory diagram for the following code snippet. Additionally, identify the lines where the edge case, base case, and recursive case occur (this will generally consist of a conditional statement, a return statement, and possibly more lines of code in between).

```py
    """Recursion practice!"""

    def factorial(num: int) -> int:
        """Calculate the factorial of num."""
        if num <= 0:
            return 1
        elif num == 1:
            return 1
        else:
            return num * factorial(num=num - 1)

    def main() -> None:
        """The main function."""
        print(factorial(num=3))

    main()
```

<details>
<summary>SHOW SOLUTION</summary>

The edge case occurs on lines 5-6, the base case occurs on lines 7-8, and the recursive case on lines 9-10.

  <img class="img-fluid" src="/static/practice-mem-diagrams/factorial.png" alt="Memory diagram of code listing with factorial and main functions"  />

</details>

2. **Challenge Question:** Create a memory diagram for the following code snippet. Identify which lines that base case(s) or recursive case(s) occur on.

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

<details>
<summary>SHOW SOLUTION</summary>

The base cases occur on lines 5-6 and 9-10. If you reach the base case on lines 5-6 that means you made it through the whole `word` without finding any differences between letters that should be the same, so you can return `True` as the final result. If you make it to lines 9-10, that means a difference was found between letters that should be the same, so `word` is not a palindrome. The recursive case is on lines 7-8.

  <img class="img-fluid" src="/static/practice-mem-diagrams/palindrome.png" alt="Memory diagram of code listing with palindrome function"  />
  
</details>