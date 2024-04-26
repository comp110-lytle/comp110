---
title: PlaneTicket Practice Problem 
author:
- Alyssa Lytle
page: lessons
template: overview
---

Practice Problem 

<!-- 
# Instructions

## Writing class, methods, and functions
1. Write a `PlaneTicket` class with attributes: `departure_city: str`, `arrival_city: str`, `departure_time: int`, `ticket_cost: float`.
2. Write an `__init__` magic method that takes `city_a: str`, `city_b: str`, `depart: int`, and `cost: float` as arguments as creates a new `PlaneTicket` with the attributes `departure_city = city_a`, `arrival_city = city_b`, `departure_time = depart`, and 
`ticket_cost = cost`.
3. Write a `__str__` magic method to print out ticket info. (Format however you want.)
4. Write a `delay` method that takes `delay_hours: int` as an argument and increases the `departure_time` by that much. (Think of time like military time… 1 am is `0100`, 1 pm is `1300`, etc.)
5. Write a `discount` method that takes a `discount: float` as an argument and discounts `ticket_cost` by that percent. (E.g. if `discount = .15`, then discount `ticket_cost` by 15%)
6. Write a `find_cheapest_ticket` *function* that takes as input a list of `PlaneTicket`s and returns the `PlaneTicket` with the lowest cost.

## Writing code to instantiate class and test methods and functions
1. Create a `PlaneTicket` object that starts in “Raleigh” and ends in “New Orleans”. It departs at 10 am (`1000`) and costs $85.25.
2. Print out the ticket info.
3. Delay the flight by 2 hours.
4. Discount it by 10%.
5. Create another `PlaneTicket` object that starts in “Orlando” and ends in “San Fransisco”. It departs at 11 am (1100) and costs $100.50.
6. Print out the which ticket is cheaper using the `find_cheapest_ticket` function.



<!-- # Solution


    from __future__ import annotations

    class PlaneTicket:
        
        departure_city: str
        arrival_city: str
        departure_time: int
        ticket_cost: float
        
        def __init__(self, city_a: str, city_b: str, depart: int, cost: float):
            """Initialize PlaneTicket Class"""
            self.departure_city = city_a
            self.arrival_city = city_b
            self.departure_time = depart
            self.ticket_cost = cost
            
        def __str__(self) -> str:
            """Visualize my ticket"""
            my_ticket_str: str = f"Depart from {self.departure_city} at {self.departure_time}. "
            my_ticket_str += f"Arrive at {self.arrival_city}. It costs ${round(self.ticket_cost, 2)}."
            return my_ticket_str 
        
        def delay(self, delay_hours: int) -> None:
            """Delay departure_time by delay_hours"""
            self.departure_time += (delay_hours * 100)
            self.departure_time %= 2400
        
        def discount(self, discount: float) -> None:
            """Discount ticket_cost by 'discount'"""
            #If discounting by .15, then multiply by (1-.15) 
            self.ticket_cost = self.ticket_cost * (1 - discount)
            
    def compare_prices(ticket1: PlaneTicket, ticket2: PlaneTicket) -> PlaneTicket:
        """Return the cheaper ticket"""
        if ticket1.ticket_cost < ticket2.ticket_cost: 
            return ticket1
        else: #ticket1 cost >= ticket2
            return ticket2
            

    my_ticket: PlaneTicket = PlaneTicket("Raleigh", "New Orleans", 1000, 85.25)

    print(my_ticket)

    my_ticket.delay(2)
    my_ticket.discount(.10)

    other_ticket: PlaneTicket = PlaneTicket("Orlando", "San Fransisco", 1100, 100.50)

    print(compare_prices(my_ticket, other_ticket)) -->

<!-- # Memory Diagram
Per request, I made a memory diagram of this code (skipping the second calls to `__init__` and `__str__`).

1. [Code Snippet 1](/static/practice-mem-diagrams/planess1.png) | [Code Snippet 2](/static/practice-mem-diagrams/planess2.png) | [Solution](/static/practice-mem-diagrams/planemd.pdf)  --> -->