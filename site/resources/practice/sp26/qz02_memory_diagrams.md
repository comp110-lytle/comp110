---
title: Quiz 02 Memory Diagram Practice
author:
- Alyssa Lytle
- Kris Jordan
- Navya Katraju
- Olivia Xiao
- Viktorya Hunanyan
- Coralee Rogers
- Benjamin Eldridge
page: lessons
template: overview
---

# Lists and `while` loops

1. Create a memory diagram for the following code listing.

```py
    """Practice diagram."""

    def check_quiz(responses: list[bool]) -> int:
        answer_key: list[bool] = [True, True, False]
        correct: int = 0
        idx: int = 0
        while idx < len(responses):
            if responses[idx] == answer_key[idx]:
                correct += 1
                idx += 1
            else:
                idx += 1
        return correct

    def main() -> None:
        my_quiz: list[bool] = [True, True, True]
        grade: int = check_quiz(my_quiz)
        print(f"{grade} out of 3 questions correct.")


    main()
```

2. Create a memory diagram for the following code listing.

```py
    """Practice diagram."""

    def create() -> list[int]:
        """An obnoxious way to make a list."""
        list_1: list[int] = []
        i: int = 0
        while i < 3:
            list_1.append(i)
            i += 1
        return list_1


    def increase(a_list: list[int], x: int) -> None:
        """Lets pump it up!"""
        i: int = 0
        while i < len(a_list):
            a_list[i] += x
            i += 1
        return None


    def main() -> None:
        """Entrypoint of the program."""
        list_1: list[int] = create()
        list_2: list[int] = list_1
        list_1 = create()
        increase(list_1, 2)
        print(list_1)
        print(list_2)


    main()
```


3. Create a memory diagram for the following code listing.

```py
    """Practice diagram."""
 
    def change_and_check(x: int, nums: list[int]) -> int:
        """Let's see what happens!"""
        if x < 0:
            return 0
        i: int = 0
        while i < len(nums):
            nums[i] += x
            i += 1
        i = 0
        while i < len(nums):
            if nums[i] == x:
                return 0
            i += 1
        return x - 1


    def main() -> None:
        """The entrypoint of this program."""
        num_1: int = 0
        list_1: list[int] = [1, 2, num_1]
        list_1.append(change_and_check(2, list_1))
        list_1.append(change_and_check(3, list_1))

    main()
```

<details>
<summary>SHOW SOLUTIONS</summary>

1. [Video](https://youtu.be/ZAH1mpf6GKc?si=8BgFglBAlJ4QJJQS)

    <img class="img-fluid" src="/static/practice-mem-diagrams/lists-01-sol.png" alt=""/>


    *Image Description*

    The Memory Diagram includes one box titled Output and below that box two columns, the left one titled Stack and the right one titled Heap.

    The Stack includes 3 frames in the following order from top to bottom including Globals, main, and check_quiz.

    The Globals frame has 2 variables including check_quiz and main.
    - check_quiz has id 0, it is a function on the Heap (lines 1-11).
    - main points id 1, it is a function on the Heap (lines 14-17).

    The main frame has 4 items including the RA and RV, and variables named my_quiz and grade.
    - The RA is defined at line 19.
    - The RV is None.
    - my_quiz has id 2, it is a list[bool] on the Heap.
        - Indexes 0, 1, 2 and values True, True, True respectively.
    - grade is 2.

    The check_quiz frame has 6 items including the RA and RV, and variables named responses, answer_key, correct, and idx.
    - The RA is defined at line 15.
    - The RV is 2.
    - responses has id 2.
    - answer_key has id 3, it is a list[bool] on the Heap.
        - Indexes 0, 1, 2 and values True, True, False respectively.
    - correct is 2.
        - Previous values of correct include 0 and 1, which are now crossed out.
    - idx is 3.
        - Previous values of idx include 0, 1, and 2, which are now crossed out.

    The Heap includes 2 function objects, and 2 list[bool] objects.

    Output includes the phrase: “2 out of 3 questions correct.” 

2. [Video](https://youtu.be/WxRQAmKlESU?si=G-i5_TWdt_Uc9n9n)

    <img class="img-fluid" src="/static/practice-mem-diagrams/refs.png" alt=""/>

3. <img class="img-fluid" src="/static/practice-mem-diagrams/change-and-check.png" alt="Image Description Here"  />

</details>

# Dictionaries and `for` loops

1. Create a memory diagram for the following code listing.

```py
    """Practice diagram."""
 
    def count(xs: list[int]) -> dict[int, int]:
        counts: dict[int, int] = {}
        for x in xs:
            if x in counts:
                counts[x] += 1
            else:
                counts[x] = 1
        return counts


    numbers: list[int] = [1, 1, 0]
    print(count(numbers))
```

2. Create a memory diagram for the following code listing.

```py
    """Practice diagram."""

    def artist_counts(playlist: dict[str, str]) -> dict[str, int]:
        artists: dict[str, int] = dict()
        for track in playlist:
            art: str = playlist[track]
            if playlist[track] not in artists:
                artists[art] = 1
            else:
                artists[art] += 1
        return artists

    songs: dict[str, str] = {
        "B2b": "Charli",
        "Hello": "Erykah",
        "Fiat": "Butcher",
        "Woo": "Erykah"
    }

    print(artist_counts(songs))
```

3. Create a memory diagram for the following code listing.

```py
    """Practice diagram."""

    def f(x: dict[str,int]) -> int:
        for y in x:
            x[y] += 1
        return x[y]
 
    def g(x: dict[str,int]) -> dict[str,str]:
        new_dict: dict[str,str] = {}
        for z in x:
            new_dict[z] = str(z)
        return new_dict

    record: dict[str, int] = {"x": 20, "y": 40}
    print(f(record))
    print(g(record))
```

4. Create a memory diagram for the following code listing.

```py
    """Practice diagram."""

    def mystery(x: dict[str,float], y: str) -> str:
        if y in x:
            return str(x[y])
        else:
            return "not in dictionary"

    x = "y"
    y = "z"
    test: dict[str,float] = {"z": 3.14}
    print(mystery(test, y))
```

5. Create a memory diagram for the following code listing.

```py
    """Practice diagram."""

    starting = dict[str, list[str]] = {}
    starting["2017"] = ["Berry", "Meeks", "Jackson"]
    starting["2023"] = ["Love", "Bacot", "Black"]

    print(starting["2017"][2])
    print(starting["2023"])
    starting["2023"][2] = "Johnson"
    print(starting["2023"])
```


<details>
<summary>SHOW SOLUTIONS</summary>

1. <img class="img-fluid" src="/static/practice-mem-diagrams/count_memdiag.png" alt="Memory diagram of code listing with count function"  />

2. <img class="img-fluid" src="/static/practice-mem-diagrams/artistcounts_memdiag.png" alt="Memory diagram of code listing with artist_counts function"  />

3. [Video](https://youtu.be/pyl28ClXwfY?si=QwIDQdlgjupNA1R3)

    <img class="img-fluid" src="/static/practice-mem-diagrams/record-sol.png" alt=""  />

    *Image Description:*
    The memory diagram is divided into three segments: Output, Stack, and Heap.

    Under the stack, the Globals frame contains references to three objects:
    * Function f points to a function on the Heap defined from lines 1 to 4.
    * Function g points to a function on the Heap defined from lines 6 to 10.
    * The variable record points to a dictionary object on the Heap with string keys and integer values.

    The F frame has:
    * Return Address (RA) at line 13.
    * Return Value (RV) is the integer 41.
    * Variable x points to a the same dictionary object on the heap as record.
    * Variable y with a crossed-out value of “x” and updated to “y”.

    The G frame has:
    * Return Address (RA) at line 14.
    * Variable x points to the same dictionary object as record.
    * Variable new_dict to a second dictionary object on the Heap.
    * Variable z with a crossed-out value of “x” updated to “y”.

    The heap has two dictionary objects:
    * The first dictionary object is associated with the variable record in Globals frame and the variable x in the F and G frames. It contains two string keys, 'x' with the integer value 20 crossed out and updated to 21, and 'y' with the integer value 40 crossed out and updated to 41.
    * The second dictionary object is associated with the variable new_dict in the G frame, with string keys 'x' and 'y' and string values ‘x’ and ‘y’ respectively.

    Output:
    The output displays the integer 41 and a dictionary object with keys 'x' and 'y', each paired with their respective values 'x' and 'y' as strings.

4. [Video](https://youtu.be/SZrv9TT84Iw)

    <img class="img-fluid" src="/static/practice-mem-diagrams/mystery-dict-sol.png" alt=""  />

    *Image Description:*
    The memory diagram provided displays elements in the Output, Stack, and Heap sections.

    Stack:

    The Globals frame contains three variables and a function:
    * Function mystery points to a function definition on the Heap spanning lines 1 to 5.
    * Variable x with the string value "y".
    * Variable y with the string value "z".
    * Variable test points to a dictionary on the Heap.

    The mystery frame has:
    * Return Address (RA) at line 10.
    * Return Value (RV) is the string “3.14”.
    * Variable x points to the same dictionary object as test
    * Variable y has a value of “z”.

    Heap:
    * A dictionary object with string keys and a floating-point value is present. It contains a single entry where the key is the string "z" and the value is the floating-point number 3.14.

    Output:
    The output section shows the floating-point number 3.14.

5. [Video](https://youtu.be/KcP6rkkHrEs) 

<img class="img-fluid" src="/static/practice-mem-diagrams/lineup-sol.png" alt="Image Description Here"  />

*Image Description:*
The memory diagram provided contains three main components: Stack, Heap, and Output.

Stack:
* The Stack section contains a single frame labeled "Globals."
* Inside Globals, there is a variable named starting pointing to a list on the Heap.

Heap:
* The first part is a dictionary object with string keys and lists of strings for values. There are two keys: "2017" and "2023." Each key points to a different list.
* The second part consists of two lists of strings. Each list contains five elements with indices from 0 to 4.
* The first list contains the following strings: "Berry", "Meeks", "Jackson", "Pinson", and "Hicks".
* The second list contains the strings: "Love", "Bacot", "Black", "Johnson" (with “Nance” crossed-out), and "Davis".

The output section has three outputs:
* The string “Jackson”
* The list [“Love”, “Bacot”, “Black”, “Nance”, “Davis”]
* The list [“Love”, “Bacot”, “Black”, “Johnson”, “Davis”]


</details>