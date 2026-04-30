---
title: Practice Problems
author:
- Alyssa Lytle
- Team 110
- Izzi Hinks
- Benjamin Eldridge
- Viktorya Hunanyan
- Kaleb White
- Rosey Anim
- Lynn Lee
- Olivia Xiao
page: lessons
template: overview
---

There are a lot of questions here, and if it feels like an overwhelming number, start with just a couple from each section that you think would help fill in any knowledge gaps you have.

If you find yourself feeling lost, please ask for help in [office hours or tutoring](/support).

# Quiz 00 General Practice

1. Trace a memory diagram of the following code listing and answer the following subquestions.

    ```python
        def total_price(calzones: int, strombolis: int) -> int:
            """Returns the total price for the order of food, including a service fee of $3."""
            return calzones_price(calzones=calzones) + strombolis_price(strombolis=strombolis) + 3
    
        def calzones_price(calzones: int) -> int:
            """Returns the price of the given number of calzones."""
            return 7 * calzones
        
        def strombolis_price(strombolis: int) -> int:
            """Returns the price of the given number of strombolis."""
            return 8 * strombolis
    
        print(total_price(calzones=4, strombolis=2))
    ```

    1.1. What line(s) do *function definition signatures* appear on?

    1.2. What line(s) do *docstrings* appear on?

    1.3. What line(s) do *expressions* appear on?

    1.4. What line(s) do *function calls* appear on?

    1.5. Write a function call to `calzones_price` that would evaluate to `28`.

<details>
  <summary><b>SHOW SOLUTION</b></summary>

  <img class="img-fluid" src="/static/practice-mem-diagrams/calzones_mem_diag.jpg" alt="Memory diagram of calzones and strombolis"/>
  
  The correct answers are:

    1.1. Lines 1, 5, and 9.

    1.2. Lines 2, 6, and 10.

    1.3. Lines 3, 7, 11, 13. Line 13 is a tricky one but it is a function call expression, thus an expression. The following explanation is intended for the curious, but is not required knowledge for the quiz: 
    
    You may not immediately think of a call to `print()` as being an expression because you may not know what it evaluates to (since all expressions must evaluate to a value). This is normal since that's not really how we use `print`, but a function call expression to `print()` such as `print("Hello!")` evaluates to `None`. You can test this for yourself by going to your REPL and running the line `print(print("Hello!"))`. This will result in two lines, first the inner `print` function call runs and `Hello!` will be printed out on the first line (with no quotation marks), then the outer `print` function call runs and prints the result of the function call expression `print("Hello")`, which is `None`, on the second line. Funky stuff!

    1.4. Lines 3 and 13.

    1.5. `calzones_price(calzones=4)`

</details>

&nbsp;

2. Trace a memory diagram of the following code listing and answer the following subquestions.

    ```python
        """Functions of a circle..."""
        
        
        def main() -> None:
            """Entrypoint of Program"""
            print(circumference(radius=1.0))
            print(area(radius=1.0))
            return None
        
        
        def area(radius: float) -> float:
            """Calculate area of a circle"""
            return 3.14 * radius ** 2
        
        
        def circumference(radius: float) -> float:
            """Calculate circumference"""
            return 2 * 3.14 * radius
        
        
        main()
    ```

    2.1. What line(s) do *function definition signatures* appear on?

    2.2. What line(s) do *docstrings* appear on?

    2.3. What line(s) do *expressions* appear on?

    2.4. What line(s) do *function calls* appear on?

    2.5. What is the return type of `area`? What is the return type of `main`?

<details>
  <summary><b>SHOW SOLUTION</b></summary>

  <img class="img-fluid" src=" /static/practice-mem-diagrams/circumference_area_mem_diag.jpg" alt="Memory diagram of circumference and area"  />
  
  The correct answers are:

    2.1. Lines 4, 11, and 16.

    2.2. Lines 1, 5, 12, and 17.

    2.3. Lines 6, 7, 13, 18, and 21.

    2.4. Lines 6, 7, and 21.

    2.5. `area` has a return type of `float` and `main` has a return type of `None`.

</details>

&nbsp;

3. Trace a memory diagram of the following code listing.

```py
    def big_func(a: int) -> int:
        return a + 2

    def bigger_func(b: int) -> int:
        return big_func(a=b) * 2

    def biggest_func(num: int) -> int:
        return bigger_func(b=num) ** 2

    def main() -> None:
        print(str(biggest_func(num=110)) + " is a big number!")

    main()
```

<details>
  <summary><b>SHOW SOLUTION</b></summary>

[Video](https://youtu.be/vpPrAIKvMPk)

<img class="img-fluid" src="/static/practice-mem-diagrams/big_func.jpg" alt="Image Description Here"  />


</details>

&nbsp;

4. Trace a memory diagram of the following code listing.

```py
    def division(x: int, y: int) -> float: 
        return y / x
        print(y % x)

    print(division(y=64, x=16))

    print(int(64/16))
```

<details>
  <summary><b>SHOW SOLUTION</b></summary>

[Video](https://youtu.be/pG0CCElC0Tw)

<img class="img-fluid" src="/static/practice-mem-diagrams/division.jpg" alt="Image Description Here"  />

</details>

&nbsp;

5. Trace a memory diagram of the following code listing.

```py
    def start_end(word: str) -> str:
        return word[0] + word[len(word)-1]

    start_end(word="kitkat")
    print(start_end(word="skittles"))
```

<details>
  <summary><b>SHOW SOLUTION</b></summary>

<img class="img-fluid" src="/static/practice-mem-diagrams/start-end.jpg" alt="Image Description Here"  />

</details>

&nbsp;

6. Trace a memory diagram of the following code listing.

```py
    def give_cookies(total_cookies: int, num_students: int) -> int:
        print("Extra cookies: " + str(total_cookies % num_students))
        return int((total_cookies - (total_cookies % num_students))/2)

    print("Each student gets " + str(give_cookies(total_cookies=11, num_students=2)) + "cookies")
```

<details>
  <summary><b>SHOW SOLUTION</b></summary>

<img class="img-fluid" src="/static/practice-mem-diagrams/cookies.png" alt="Image Description Here"  />

</details>

&nbsp;

7. Trace a memory diagram of the following code listing.

```py
    def get_starting_point(word: str) -> int:
        return int(len(word) / 3)

    def shift_position(index: int) -> int:
        return index - 1

    def extract_character(word: str, index: int) -> str:
        return word[index]

    def main(word: str) -> None:
        print("The hidden character is: " + extract_character(word=word, index=shift_position(index=get_starting_point(word=word))))

    main(word="mystery")
```

<details>
  <summary><b>SHOW SOLUTION</b></summary>

<img class="img-fluid" src="/static/practice-mem-diagrams/mystery_word.jpg" alt="Image Description Here"  />

</details>