---
title: Practice Memory Diagram
author:
- Navya Katraju
page: lessons
template: overview
---


# Snippet

```python
class HotelRes:
    city: str
    nights: int
    upgrade: bool

    def __init__(self, city: str, nights: int, upgrade: bool = False):
        self.city = city
        self.nights = nights
        self.upgrade = upgrade

    def calculate_cost(self, nightly_price: int | float) -> int | float:
        cost: int | float = self.nights * nightly_price
        if self.upgrade:
            cost += 100
        return cost
    
miami: HotelRes = HotelRes("Miami", 3, True)      
print(miami.calculate_cost(181.42))
nyc: HotelRes = HotelRes("NYC", 2)
print(nyc.calculate_cost(272))
```

# Solution
![navyak_solution_10](navyak_solution_10.png)

*Image Description*
The Memory Diagram includes 3 columns titled Stack, Heap, and Output, from left to right.
The Stack includes 5 frames in the following order from top to bottom: Globals, HotelRes #__init__, HotelRes #calculate_cost, HotelRes #__init__, and HotelRes #calculate_cost.
The Globals frame has 3 variables including HotelRes, miami, and nyc.
- HotelRes points to a class definition on the Heap (lines 4-20).
- miami points to an object of HotelRes type on the Heap.
    - city is "Miami"
    - nights is 3
    - upgrade is True
- nyc points to a different object of HotelRes type on the Heap.
    - city is "NYC"
    - nights is 2
    - upgrade is False
The first HotelRes #__init__ frame has 6 variables including the RA, RV, self, city, nights, and upgrade.
- The RA is defined at line 20.
- The RV points to the same object in Heap as miami.
- self also points to the same object in Heap as miami.
- city is "Miami"
- nights is 3.
- upgrade is True.
The first HotelRes #calculate_cost frame has 4 variables including the RA, RV, self, and nightly_price.
- The RA is defined at line 21.
- The RV is 644.26
- self points to the same object in Heap as miami.
- nightly_price is 181.42.
The second HotelRes #__init__ frame has 6 variables including the RA, RV, self, city, nights, and upgrade.
- The RA is defined at line 22.
- The RV points to the same object in Heap as nyc.
- self also points to the same object in Heap as nyc.
- city is "NYC"
- nights is 2.
- upgrade is False.
The second HotelRes #calculate_cost frame has 4 variables including the RA, RV, self, and nightly_price.
- The RA is defined at line 23.
- The RV is 544.
- self points to the same object in Heap as nyc.
- nightly_price is 272.
The Output includes 644.26 and 544.