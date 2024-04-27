---
title: Practice Memory Diagram
author:
- Alyssa Lytle
page: lessons
template: overview
---

# Snippet

```
    class Games:
        
        set: list[str]
        wishlist: list[str]
        
        def __init__(self, set: list[str], wishlist: list[str]):
            self.set = set
            self.wishlist = wishlist
        
        def __str__(self) -> str:
            return f"My games: {self.set}"
        
        def purchase(self, game):
            if game in self.wishlist:
                idx: int = 0
                while idx < len(self.wishlist):
                    if game == self.wishlist[idx]:
                        self.wishlist.pop(idx)
                    idx += 1
            self.set.append(game)
            
    collection: Games = Games([], ["Uno", "Life"])
    collection.purchase("Uno")
    collection.purchase("Catan")
    print(collection)
```

# Solution

<!-- <img class="img-fluid" src="/static/practice-mem-diagrams/playlist_sol.png" alt=""  />  -->