---
title: Practice Memory Diagram
author:
- Izzi Hinks
page: lessons
template: overview
---

## Snippet

```py
    class Concert:
        artist: str
        seats: dict[str, bool]
    
        def __init__(self, a: str, s: dict[str, bool]):
            self.artist = a
            self.seats = s
    
        def assign_seats(self, wanted_seats: list[str], name: str) -> None:
            for seat in wanted_seats:
                if seat in self.seats:
                    available: bool = self.seats[seat]
                    if available:
                        print(f"{name} bought seat {seat} to see {self.artist}!")
                        self.seats[seat] = False
                    else: 
                        print(f"Seat {seat} is unavailable :(")
    
    lenovo_seats: dict[str, bool] = {"K1": True, "K2": True, "K3": False}
    show: Concert = Concert(a = "Travisty", s = lenovo_seats)
    show.assign_seats(wanted_seats = ["K2", "K3"], name = "Kay")
```

## Solution

<details>
<summary>SOLUTION</summary>

Concert memory diagram solution (see the solution video [here](https://youtu.be/Fr0lF3o9u5o)!).

<img class="img-fluid" src="/static/practice-mem-diagrams/concert.png" alt="Memory diagram of code listing with Concert classes."  />

</details>