---
title: Practice Memory Diagram
author:
- Navya Katraju
page: lessons
template: overview
---


# Snippet

```python
def login(user: str) -> bool:
    if user == "admin":
        print("Logging in...")
        return True
    else:
        return False


def new_password(pw: str) -> str:
    idx: int = 0
    while len(pw) < 6:
        pw += pw[idx]
        idx += 1
    return pw


def main() -> None:
    login("admin")
    print(f"Your new password is: {new_password('110')}")


if __name__ == "__main__":
    main()
```

# Solution

![navyak_solution_1.png](navyak_solution_1.png)

*Image Description*

The Memory Diagram includes one box titled Output and below that box two columns,
the left one titled Stack and the right one titled Heap.
The Stack includes 4 frames in the following order from top to bottom including
Globals, main, login, and new_password.
The Globals frame has 3 variables including login, new_password, and main.
- login points to a function on the Heap (lines 4-9).
- new_password points to a function on the Heap (lines 12-17).
- main points to a function on the Heap (lines 20-22).
The main frame has 2 items including the RA and RV.
- The RA is defined at line 26.
- The RV is None.
The login frame has 3 items including the RA and RV and a variable named user.
- The RA is defined at line 21.
- The RV is True.
- user is “admin”
The new_password frame has 4 items including the RA and RV and two variables named
pw and idx.
- The RA is defined at line 22.
- The RV is ‘110110’
- pw is ‘110110’
    - Previous values of pw include ‘110’, ‘1101’, and ‘11011’ which are now crossed
    out
- idx is 3
    - Previous values of idx include 0, 1, and 2 which are now crossed out.

The Heap includes 3 function objects.
Output includes the 2 phrases: “Logging in...” and “Your new password is: 110110.”