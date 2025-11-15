---
title: Practice Memory Diagram
author:
- Izzi Hinks
page: lessons
template: overview
---

```py
    class Dog:
        name: str
        age: int
        
        def __init__(self, n: str, a:int):
            self.name = n
            self.age = a
            
        def speak(self) -> None: 
            print(self.name + " says woof!")
            
        def birthday(self) -> int:
            self.age += 1 
            return self.age
            
    class Cat:
        name: str
        age: int
        
        def __init__(self, n: str, a:int):
            self.name = n
            self.age = a
            
        def speak(self) -> None: 
            print(self.name + " says meow!")
            
        def birthday(self) -> int:
            self.age += 1 
            return self.age
        
    rory: Dog = Dog(n = "Rory", a = 4)
    print(rory.birthday())
    miso: Cat = Cat("Miso", 2)
    miso.speak()
```

<details>
<summary>SOLUTION</summary>

Dog and Cat memory diagram solution (see the solution video [here](https://youtu.be/_S1ISCVHdic)!).

<img class="img-fluid" src="/static/practice-mem-diagrams/dog_cat.png" alt="Memory diagram of code listing with Dog and Cat classes."  />

</details>