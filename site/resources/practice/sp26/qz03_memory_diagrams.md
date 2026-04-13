---
title: Quiz 03 Memory Diagram Practice
author:
- Alyssa Lytle
- Kris Jordan
- Benjamin Eldridge
- Jack Coury
- Izzi Hinks
page: lessons
template: overview
---

# Object-Oriented Programming

1. Complete a memory diagram for the following code listing. 

```py
1 class Dog:
2     name: str
3     age: int
4     
5     def __init__(self, n: str, a:int):
6         self.name = n
7         self.age = a
8         
9     def speak(self) -> None: 
10        print(self.name + " says woof!")
11        
12    def birthday(self) -> int:
13        self.age += 1 
14        return self.age
15        
16 class Cat:
17    name: str
18    age: int
19    
20    def __init__(self, n: str, a:int):
21        self.name = n
22        self.age = a
23        
24    def speak(self) -> None: 
25        print(self.name + " says meow!")
26        
27    def birthday(self) -> int:
28        self.age += 1 
29        return self.age
30    
31 rory: Dog = Dog(n = "Rory", a = 4)
32 print(rory.birthday())
33 miso: Cat = Cat("Miso", 2)
34 miso.speak()
```

2. Complete a memory diagram for the following code listing. 

```py
1  class Concert:
2      artist: str
3      seats: dict[str, bool]
4  
5      def __init__(self, a: str, s: dict[str, bool]):
6          self.artist = a
7          self.seats = s
8  
9      def assign_seats(self, wanted_seats: list[str], name: str) -> None:
10         for seat in wanted_seats:
11             if seat in self.seats:
12                 available: bool = self.seats[seat]
13                 if available:
14                     print(f"{name} bought seat {seat} to see {self.artist}!")
15                     self.seats[seat] = False
16                 else: 
17                    print(f"Seat {seat} is unavailable :(")
18 
19 lenovo_seats: dict[str, bool] = {"K1": True, "K2": True, "K3": False}
20 show: Concert = Concert(a = "Travisty", s = lenovo_seats)
21 show.assign_seats(wanted_seats = ["K2", "K3"], name = "Kay")
```

<details>
<summary>SOLUTIONS</summary>

1. Dog and Cat memory diagram solution (see the solution video [here](https://youtu.be/_S1ISCVHdic)!).

<!-- <img class="img-fluid" src="/static/practice/qz03_practice/dog_cat.png" alt="Memory diagram of code listing with Dog and Cat classes."  /> -->

2. Concert memory diagram solution (see the solution video [here](https://youtu.be/Fr0lF3o9u5o)!).

<!-- <img class="img-fluid" src="/static/practice/qz03_practice/concert.png" alt="Memory diagram of code listing with Concert classes."  /> -->

</details>


# Magic Methods


1. Diagram the following code snippet:

```py
1     class Knight:
2         """A medieval Knight."""
3         name: str
4
5         def __init__(self, name: str):
6             self.name = name
7
8         def __str__(self) -> str:
9             return f"Sir {self.name}"
10
11    class Castle:
12        """A medieval castle with a drawbridge for crossing a surrounding moat and a guarding knight."""
13        guard: Knight
14        drawbridge_up: bool
15
16        def __init__(self, guard: Knight, bridge_up: bool):
17            self.guard = guard
18            self.drawbridge_up = bridge_up
19
20        def __str__(self) -> str:
21            if self.drawbridge_up:
22                return f"Guarded by {self.guard} and closed to outsiders!"
23            else:
24                return f"Guarded by {self.guard} but open to all!"
25            
26        def open(self) -> None:
27            if self.drawbridge_up:
28                print("Let down the bridge!")
29                self.drawbridge_up = False
30            else:
31                print("Already open!")
32
33        def close(self) -> None:
34            if not self.drawbridge_up:
35                print("Pull up the bridge!")
36                self.drawbridge_up = True
37            else:
38                print("Already closed!")
39
40
41    lancelot: Knight = Knight("Lancelot")
42    my_castle: Castle = Castle(lancelot, False)
43    print(my_castle)
44    my_castle.close()
45    print(my_castle)
```

<details>
<summary>SOLUTION</summary>

<img class="img-fluid" src="/static/practice/qz04_practice/castle_soln.png" alt="Memory diagram of code listing with Guard and Castle classes."  />

</details>

# Recursive Structures


1. Create a memory diagram of the following code snippet:

    ```py
    1     """A messy linked list..."""
    2
    3     from __future__ import annotations
    4 
    5     # Node class definition included for reference!
    6     class Node:
    7         value: int
    8         next: Node | None
    9 
    10        def __init__(self, val: int, next: Node | None):
    11            self.value = val
    12            self.next = next
    13
    14        def __str__(self) -> str:
    15            rest: str
    16            if self.next is None:
    17                rest = "None"
    18            else:
    19                rest = str(self.next)
    20            return f"{self.value} -> {rest}"
    21
    22    knight: Node = Node(3, None)
    23    bishop: Node = Node(2, knight)
    24    rook: Node = Node(1, bishop)
    25    print(rook)
    26    castle: Node = Node(0, bishop)
    27    print(castle)
    ```

<details>
<summary>SOLUTION</summary>

<img class="img-fluid" src="/static/practice/qz04_practice/linked_list_soln.png" alt="Memory diagram of code listing of linked list."  />

</details>