---
title: Recursive Structures Questions
author:
- Benjamin Eldridge
page: lessons
template: overview
---

Any questions that reference the `Node` class are referring to a class defined in the following way:

```py
    from __future__ import annotations

    class Node:
        value: int
        next: Node | None

        def __init__(self, val: int, next: Node | None):
            self.value = val
            self.next = next

        def __str__(self) -> str:
            rest: str
            if self.next is None:
                rest = "None"
            else:
                rest = str(self.next)
            return f"{self.value} -> {rest}"
```

## Multiple Choice

1. (Select all that apply) Which of the following properties of a recursive function will ensure that it *does not* have an infinite loop?

    a. The function calls itself in the recursive case.

    b. The recursive case progresses towards the base case.

    c. The base case returns a result directly (it does not call the function again).

    d. The base case is always reached.

    e. None of the above

2. (Fill in the blank) A linked list in python consists of one or more instances of the _____ class.

    a. `list`

    b. `int`

    c. `Node`

    d. `None`

    e. None of the above

3. (True/False) Attempting to access the `value` or `next` attribute of `None` will result in an error.

4. (True/False) There is no way to traverse to the start of a linked list that has multiple Nodes given only a reference to the last `Node`.

<details>
<summary>SOLUTIONS</summary>

1. B, C, and D. A is true of all recursive functions, but does not guarantee that there won't be an infinite loop.

2. C

3. True, attempting to access any attributes of `None` will result in an error since it has no attributes.

4. True, Nodes only know about the `Node` "in front" of them, or the next `Node`, so you cannot move backwards in a linked list.

</details>

## Code Writing

1. Write a recursive function (not a method of the `Node` class) named `recursive_range` with `start` and `end` `int` parameters that will create a linked list with the Nodes having values counting from `start` to `end`, not including `end`, either counting down (decrementing) or up (incrementing) depending on what `start` and `end` are. The function signature is below to get you started.

    `def recursive_range(start: int, end: int) -> Node | None:`

2. Write a recursive method of the `Node` class named `append` that has parameters `self` and `new_val` which is of type `int`, and this method should create a new `Node` at the end of the linked list and return `None`. In other words, the last `Node` object before this method is called will have a `next` attribute of `None`, but after this method is called, it should have a `next` attribute equal to a `Node` object with value `new_val` and `next` attribute being `None` (since that new node is now the last `Node` in the linked list).

3. Write a recursive method of the `Node` class named `get_length` that has parameters `self` and `count` which is of type `int`, which if you were to call with a `count` argument of 0, would return the length of the linked list starting with `self` (not including `None`). Hint: Use `count` to keep track of a `Node` count between function calls. How would you write this method as an *iterative* function (with no `count` parameter)?

<details>
<summary>SOLUTIONS</summary>

1. Recursive range has two base cases, and the one that is used depends on if `start` is greater than or less than `end`.

    ```py
        def recursive_range(start: int, end: int) -> Node | None:
            if start == end:
                return None
            elif start < end:
                return Node(start, recursive_range(start + 1, end))
            else:
                return Node(start, recursive_range(start - 1, end))
    ```

2. Here is one way to make the `append` method:

    ```py
        def append(self, new_val: int) -> None:
            if self.next is None:
                self.next = Node(new_val, None)
            else:
                self.next.append(new_val)
    ```

3. Here are two possibilities:

```py
    def get_length(self, count: int) -> int:
        if self.next is None:
            return count + 1
        else:
            return self.next.get_length(count + 1)
```

```py
    def get_length(self, count: int) -> int:
        count += 1
        if self.next is None:
            return count
        else:
            return self.next.get_length(count)
```

</details>

## Short Answer

1. Based on the following code snippet, what would be the output of the following lines of code given in parts 1.1-1.4?

    ```py
        from __future__ import annotations

        # Node class definition included for reference!
        class Node:
            value: int
            next: Node | None

            def __init__(self, val: int, next: Node | None):
                self.value = val
                self.next = next

            def __str__(self) -> str:
                rest: str
                if self.next is None:
                    rest = "None"
                else:
                    rest = str(self.next)
                return f"{self.value} -> {rest}"

        x: Node = Node(4, None)
        y: Node = Node(8, None)
        
        x.next = y

        z: Node = Node(16, None)

        z.next = x

        x = Node(32, None)
    ```

    1.1. `print(z.next.next.value)`

    1.2. `print(y.next)`

    1.3. `print(x)`

    1.4. `print(z)`


<details>
<summary>SOLUTIONS</summary>

1. Question 1 answers:

    1.1. `8`

    1.2. `None`

    1.3. `32 -> None`

    1.4. `16 -> 4 -> 8 -> None`

</details>