---
title: Practice Memory Diagram
author:
- Navya Katraju
page: lessons
template: overview
---

# Snippet

```python
class Job:
    title: str
    hourly_pay: int
    weekly_hours: int

    def __init__(self, t: str, h: int, w: int):
        self.title = t
        self.hourly_pay = h
        self.weekly_hours = w
    
    def give_raise(self, raise_amt: int) -> None:
        self.hourly_pay += raise_amt
        print(f"You now make ${self.hourly_pay} an hour.")
    
    def calculate_pay(self) -> int:
        wages: int = self.hourly_pay * self.weekly_hours
        return wages

my_job: Job = Job("barista", 9, 10)
my_job.give_raise(2)
earnings: int = my_job.calculate_pay()
print(f"You made ${earnings} this week.")
```

# Solution
![navyak_solution_8](navyak_solution_8.png)

*Image Description*
The Memory Diagram includes 3 columns titled Stack, Heap, and Output, from left to right.
The Stack includes 4 frames in the following order from top to bottom: Globals, Job #__init__, Job #give_raise, and Job #calculate_pay. 
The Globals frame has 3 variables including Job, my_job, and earnings.
- Job points to a class definition on the Heap (lines 4-25)
- my_job points to an object of the Job type on the Heap. The attributes are as follows:
    - title is "barista".
    - hourly_pay is 11 (previous value is 9 which is now crossed out).
    - weekly_hours is 10.
- earnings is 110.
The Job #__init__ frame has 6 variables, including the RA, RV, self, title, hourly_pay, and weekly_hours.
- The RA is defined at 22
- The RV points to the same object on the Heap as my_job in the Globals frame.
- self points to the same object on the Heap as my_job in the Globals frame.
- title is "barista".
- hourly_pay is 9.
- weekly_hours is 10.
The Job #give_raise frame has 4 variables including the RA, RV, self, and raise_amt.
- The RA is defined at 23.
- The RV is None.
- self points to the same object on the Heap as my_job in the Globals frame.
- raise_amt is 2
The Job #calculate_pay frame has 3 variables including the RA, RV, and self.
- The RA is defined at 24.
- The RV is None.
- self points to the same object on the Heap as my_job in the Globals frame.
Output includes the two phrases "You now make $11 an hour." and "You made $110 this week."