---
title: In Class Code Writing
author:
- Alyssa Lytle
page: lessons
template: overview
---

# In Class Code Writing

Here's the solution from class:

```
from __future__ import annotations

class GameCollection:

    inventory: list[str]
    wishlist: list[str]
    budget: float

    def __init__(self, curr_inventory: list[str], wish: list[str], start_budget: float):
        self.inventory = curr_inventory
        self.wishlist = wish
        self.budget = start_budget
    
    def purchase(self, name: str, cost: float) -> None:
        # If cost is less than the budget attribute: 
        if cost < self.budget:
            # subtract cost from the budget 
            self.budget -= cost
            # add name to inventory
            self.inventory.append(name)
            # and if name is in wishlist, remove it from wishlist
            idx: int = 0
            while idx < len(self.wishlist):
                curr_game: str = self.wishlist[idx]
                if curr_game == name:
                    # This means name IS in my wishlist! So, remove it!
                    self.wishlist.pop(idx)
                idx += 1
        # Else (cost is greater than the budget attribute):
        else: 
            # print “Sorry! Not enough money!” and do nothing else.
            print("Sorry! Not enough money!")

    def __add__(self, new_game: str) -> GameCollection: # Call with self + new_game
        new_wishlist: list[str] = []
        # Copy over self.wishlist
        for item in self.wishlist:
            new_wishlist.append(item)
        # Add new_game to new wishlist
        new_wishlist.append(new_game)
        new_collection: GameCollection = GameCollection(self.inventory, new_wishlist, self.budget)
        return new_collection

# Instantiation
my_games: GameCollection = GameCollection(curr_inventory=["Sims"], wish=["Witcher"], start_budget=50.75)
# Use the purchase method call to try and purchase “Stardew” at price 40.25
my_games.purchase("Stardew", 40.25)
print(my_games.inventory)
print(my_games.budget)
# Use the purchase method call to try and purchase “Witcher” at price 60.00
my_games.purchase("Witcher", 60.00)
# Create a new variable ryans_games that is my_games with “Mario” added to the wishlist.
ryans_games: GameCollection = my_games + "Mario"
# Print out the inventory, wishlist, and budget attributes
print(ryans_games.wishlist)
print(my_games.wishlist)
```