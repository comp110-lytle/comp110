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
    class Knight:
        """A medieval Knight."""
        name: str

        def __init__(self, name: str):
            self.name = name

        def __str__(self) -> str:
            return f"Sir {self.name}"

    class Castle:
        """A medieval castle with a drawbridge for crossing a surrounding moat and a guarding knight."""
        guard: Knight
        drawbridge_up: bool

        def __init__(self, guard: Knight, bridge_up: bool):
            self.guard = guard
            self.drawbridge_up = bridge_up

        def __str__(self) -> int:
            if self.drawbridge_up:
                return f"Guarded by {self.guard} and closed to outsiders!"
            else:
                return f"Guarded by {self.guard} but open to all!"
            
        def open(self) -> None:
            if self.drawbridge_up:
                print("Let down the bridge!")
                self.drawbridge_up = False
            else:
                print("Already open!")

        def close(self) -> None:
            if not self.drawbridge_up:
                print("Pull up the bridge!")
                self.drawbridge_up = True
            else:
                print("Already closed!")


    lancelot: Knight = Knight("Lancelot")
    my_castle: Castle = Castle(lancelot, False)
    print(my_castle)
    my_castle.close()
    print(my_castle)
```

## Solution

<details>
<summary>SOLUTION</summary>

<img class="img-fluid" src="/static/practice-mem-diagrams/castle_soln.png" alt="Memory diagram of code listing with Guard and Castle classes."  />

</details>