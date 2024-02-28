---
title: Practice Memory Diagram
author:
- Alyssa Lytle
page: lessons
template: overview
---

# Snippet

```
    def mystery(x: dict[str,float], y: str) -> str:
        if y in x:
            return str(x[y])
        else:
            return "not in dictionary"

    x = "y"
    y = "z"
    test: dict[str,float] = {"z": 3.14}
    print(mystery(test,y))
```

# Solution

<img class="img-fluid" src="/static/practice-mem-diagrams/mystery-dict-sol.png" alt=""  />

*Image Description:*
The memory diagram provided displays elements in the Output, Stack, and Heap sections.

Stack:

The Globals frame contains three variables and a function:
* Function mystery points to a function definition on the Heap spanning lines 1 to 5.
* Variable x with the string value "y".
* Variable y with the string value "z".
* Variable test points to a dictionary on the Heap.

The mystery frame has:
* Return Address (RA) at line 10.
* Return Value (RV) is the string “3.14”.
* Variable x points to the same dictionary object as test
* Variable y has a value of “z”.

Heap:
* A dictionary object with string keys and a floating-point value is present. It contains a single entry where the key is the string "z" and the value is the floating-point number 3.14.

Output:
The output section shows the floating-point number 3.14.