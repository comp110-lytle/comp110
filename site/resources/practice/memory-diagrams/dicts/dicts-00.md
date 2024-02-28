---
title: Practice Memory Diagram
author:
- Alyssa Lytle
page: lessons
template: overview
---

# Snippet

```
    def f(x: dict[str,int]) -> int:
        for y in x:
            x[y] += 1
        return x[y]

    def g(x: dict[str,int]) -> dict[str,str]:
        new_dict: dict[str,str] = {}
        for z in x:
            new_dict[z] = str(z)
        return new_dict

    record: dict[str, int] = {"x": 20, "y": 40}
    print(f(record))
    print(g(record))
```

# Solution

<img class="img-fluid" src="/static/practice-mem-diagrams/record-sol.png" alt=""  />

*Image Description:*
The memory diagram is divided into three segments: Output, Stack, and Heap.

Under the stack, the Globals frame contains references to three objects:
* Function f points to a function on the Heap defined from lines 1 to 4.
* Function g points to a function on the Heap defined from lines 6 to 10.
* The variable record points to a dictionary object on the Heap with string keys and integer values.

The F frame has:
* Return Address (RA) at line 13.
* Return Value (RV) is the integer 41.
* Variable x points to a the same dictionary object on the heap as record.
* Variable y with a crossed-out value of “x” and updated to “y”.

The G frame has:
* Return Address (RA) at line 14.
* Variable x points to the same dictionary object as record.
* Variable new_dict to a second dictionary object on the Heap.
* Variable z with a crossed-out value of “x” updated to “y”.

The heap has two dictionary objects:
* The first dictionary object is associated with the variable record in Globals frame and the variable x in the F and G frames. It contains two string keys, 'x' with the integer value 20 crossed out and updated to 21, and 'y' with the integer value 40 crossed out and updated to 41.
* The second dictionary object is associated with the variable new_dict in the G frame, with string keys 'x' and 'y' and string values ‘x’ and ‘y’ respectively.

Output:
The output displays the integer 41 and a dictionary object with keys 'x' and 'y', each paired with their respective values 'x' and 'y' as strings.