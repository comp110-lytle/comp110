---
title: Practice Memory Diagram
author:
- Benjamin Eldridge
page: lessons
template: overview
---

## Snippet

Diagram the following code snippet:

```py
    """A messy linked list..."""

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

    knight: Node = Node(3, None)
    bishop: Node = Node(2, knight)
    rook: Node = Node(1, bishop)
    print(rook)
    castle: Node = Node(0, bishop)
    print(castle)
```

## Solution

<details>
<summary>SOLUTION</summary>

<img class="img-fluid" src="/static/practice-mem-diagrams/linked_list_soln.png" alt="Memory diagram of code listing with the Node class and a messy linked list."  />

</details>