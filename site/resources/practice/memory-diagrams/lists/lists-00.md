---
title: Practice Memory Diagram
author:
- Alyssa Lytle
page: lessons
template: overview
---

# Snippet

```
    def f(x: list[str]) -> str:
        for y in range(0,len(x)):
            x[y] += "x"
        return x[y]

    def g(x: list[str]) -> list[str]:
        new_list: list[str] = []
        for z in x:
            new_list.append(str(z))
        return new_list

    record: list[str] = ["x", "y"]
    print(f(record))
    print(g(record))
```

# Solution

*Coming Soon*

<!-- * Note that for this solution, we did not represent the `range()` function on the heap! We instead just represented `y` as a variable on the stack that gets updated. If you chose to include a "range" object to the heap, we wouldn't take points off, but we are really just looking for the value of `y`!

<img class="img-fluid" src="/static/assets/f23/lists00-sol.png" alt=""  />

*Image Descriptions:*
Under Globals:
* Variable f points to a function labeled Fn [1-4] on the Heap.
* Variable g points to a function labeled Fn [1-6] on the Heap.
* Variable record points to a list object on the Heap with the type list[str].

The f function frame has:
* Return Address (RA) pointing to line 13.
* Variables x and y, with x pointing to the same list object on the Heap as the global variable record and y with a value of 1 and a crossed-out value of 0.
* Return Value (RV) with a value of "yx".

The g function frame has:
* Return Address (RA) pointing to line 14.
* Variables x pointing to the same list object as the global variable record and new_list pointing to a second list object on the Heap with the type list[str].
* Variable z with a crossed-out reference to a string "xx" and updated to point to a string "yx".
* Return Value (RV) points to the second list[str] object on the heap.

The Heap section shows two list objects and two string objects:
* The first list on the heap has two values. The first value is “xx” with a crossed-out value of “x”. The second value is “yx” with a crossed-out value of “y”.
* The second list on the heap has two values. The first value is “xx” and the second value is “yx”.

The Output section at the top first prints “yx”, then the list [“xx”,”yx”]. -->
