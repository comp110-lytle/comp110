---
title: Practice Memory Diagram
author:
- Navya Katraju
page: lessons
template: overview
---

# Snippet

```python
class RoboPet:
    name: str
    energy: int

    def __init__(self, name: str, energy: int = 10):
        self.name = name
        self.energy = energy

    def do_trick(self, difficulty: int | float):
        if self.energy >= difficulty:
            print(f"{self.name} did a trick!")
            self.energy -= difficulty
        else:
            print(f"{self.name} is too tired!")
    
    def charge(self, amt: int):
        self.energy += amt

my_pet: RoboPet = RoboPet("Spot")
my_pet.do_trick(11.5)
my_pet.charge(10)
print(my_pet.energy)
```

# Solution
![navyak_solution_9](navyak_solution_9.png)

*Image Description*
The Memory Diagram includes 3 columns titled Stack, Heap, and Output, from left to right.
The Stack includes 4 frames in the following order from top to bottom: Globals, RoboPet #__init__, RoboPet #do_trick, and RoboPet #charge. 
The Globals frame has 2 variables including RoboPet and my_pet.
- RoboPet points to a class definition on the Heap (lines 4-20)
- my_pet points to an object of RoboPet type on the Heap
    - name is "Spot"
    - energy is 20
        - previous value of 10 is crossed out.
The RoboPet #__init__ frame has 5 variables, including the RA and RV, self, name, and energy.
- The RA is defined at line 22.
- The RV points to the same object in Heap as my_pet.
- self also points to the same object in Heap as my_pet.
- name is "Spot".
- energy is 10.
The RoboPet #do_trick frame has 4 variables including the RA and RV, self, and difficulty.
- The RA is defined at line 23.
- The RV is None.
- self points to the same object in heap as my_pet.
- difficulty is 11.5
The RoboPet #charge frame has 4 variables including the RA and RV, self, and amt.
- The RA is defined at line 24.
- The RV is None.
- self points to the same object in heap as my_pet.
- amt is 10.
The Output includes the phrase "Spot is too tired!" and the number 20.