---
title: Practice Memory Diagram
author:
- Alyssa Lytle
page: lessons
template: overview
---

# Snippet

```
    class Stadium:
        sponsor: str
        capacity: int
        has_roof: bool
        ticket_price: int

        def __init__(self, s: str, c: int, h: bool, t: int = 20):
            self.sponsor = s
            self.capacity = c
            self.has_roof = h
            self.ticket_price = t
        
        def upgrade(self) -> None:
            if self.capacity > 75000:
                self.has_roof = True
                self.ticket_price += 10
            elif self.sponsor == "FedEx":
                self.capacity += 10000
                self.ticket_price += 5
            else:
                self.capacity += 5000
        
    def main() -> None:
        new_arena: Stadium = Stadium("FedEx", 70000, False)
        new_arena.upgrade()
        new_arena.upgrade()
        print(new_arena.ticket_price)


    main()
```

# Solution

<img class="img-fluid" src="/static/practice-mem-diagrams/stadium-sol.png" alt=""  /> 