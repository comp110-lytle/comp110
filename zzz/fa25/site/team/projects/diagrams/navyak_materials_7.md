---
title: Practice Memory Diagram
author:
- Navya Katraju
page: lessons
template: overview
---

# Snippet

```python
class Person:
    name: str
    age: int

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def birthday(self) -> None:
        print(f"Happy birthday {self.name}!")
        self.age += 1
        print(f"You are now {self.age} years old.")

me: Person = Person("Bob", 43)
me.birthday()
```

# Solution
![navyak_solution_7](navyak_solution_7.png)

*Image Description*
The Memory Diagram includes two columns, the left titled Stack and the right titled Heap. Below this is the Output.
The Stack includes 3 frames in the following order from top to bottom: Globals, Person #__init__, and Person #birthday.
The Globals frame has 2 variables including Person and me.
- Person points to a class definition on the Heap (lines 4-15)
- me points to an object of the Person class on the Heap.
    - The attributes are name, which is "Bob" and age, which is 44 (the previous value, now crossed out, is 43).
The Person #__init__ feame has 5 variables, including RA, RV, self, name, and age.
- The RA is defined at line 17.
- The RV points to the same object on the Heap as me in the Globals frame.
- self points to the same object on the Heap as me in the Globals frame.
- name is "Bob".
- age is 43.
The Person #birthday frame has 3 variables, including RA, RV, and self.
- The RA is defined at line 18.
- The RV is None.
- self points to the same object on the Heap as me in the Globals frame.
Output includes two phrases: "Happy birthday Bob!" and "You are now 44 years old."