---
title: Quiz 3 OOP Memory Diagram Practice
author:
- Anna Xu
page: intranet
---

Hello everyone! This is the **Part 2** of practice questions for the upcoming **Quiz 03 on Tuesday, November 10th**. Part 1 (already posted) covered OOP code writing questions, this one will be on OOP memory diagrams, and Part 3 focusing on recursion memory diagram practice will be released later today. The solutions for these problems can be found [here](https://youtu.be/UDMVOrcN1xA). Good luck :)

## Instructions
Please create a memory diagram for each problem documenting the entire execution of the program like you have practiced in class. 

## Review Problems

### 1. Pokemon GO!

~~~{.python .numberLines startFrom="1"}
class Pokemon:
    xp: int
    alive: bool

    def __init__(self, xp: int):
        self.xp = xp
        self.alive = True
    
    def battle(self, opp: int) -> None:
        if self.alive is False:
            self.heal()
        if self.xp > opponent:
            self.xp += 10
        else:
            self.xp -= 10
            if self.xp <= 0:
                self.alive = False 
    
    def train(self) -> None:
        if self.alive:
            self.xp += 20
    
    def heal(self) -> None:
        self.alive = True


def main() -> None:
    pika: Pokemon = Pokemon(20)
    char: Pokemon = Pokemon(10)
    char.battle(pika.xp)
    char.train()
    pika.battle(char.xp)

    
if __name__ == "__main__":
    main()
~~~

### 2. Among Us (kind of)

~~~{.python .numberLines startFrom="1"}
from typing import List

class Player:
    tasks: List[str]
    imp: bool
    alive: bool

    def __init__(self, imp: bool, tasks: List[str]):
        self.imp = imp
        self.tasks = tasks
        self.alive = True

    def complete_task(self) -> None:
        if len(self.tasks) > 0:
            self.tasks.pop(len(self.tasks) - 1) # Remove the last item from the list


class AmongUs:
    crew: int
    imps: int

    def __init__(self):
        self.crew = 0
        self.imps = 0

    def add(self, p: Player) -> None:
        if p.imp:
            self.imps += 1
        else:
            self.crew += 1

    def kill(self, p: Player) -> None:
        p.alive = False
        self.crew -= 1
        self.check()
    
    def vote_out(self, p: Player) -> None:
        p.alive = False
        if p.imp:
            self.imps -= 1
        else:
            self.crew -= 1
        self.check()
    
    def check(self) -> str:
        if self.crew == 0:
            return "Imposters won!"
        if self.imps == 0:
            return "Crewmates won!"
        return "No one won yet."


def main() -> None:
    p1: Player = Player(True, [])
    p2: Player = Player(False, ["wires"])
    p3: Player = Player(False, ["trash", "medscan"])

    game: AmongUs = AmongUs()
    game.add(p1)
    game.add(p2)
    game.add(p3)

    p2.complete_task()
    p3.complete_task()
    game.kill(p2)
    game.vote_out(p1)


if __name__ == "__main__":
    main()
~~~
