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

<img class="img-fluid" src="/static/practice-mem-diagrams/lists-02-sol.jpg" alt=""/>


<!-- * Note that for this solution, we did not represent the `range()` function on the heap! We instead just represented `y` as a variable on the stack that gets updated. If you chose to include a "range" object to the heap, we wouldn't take points off, but we are really just looking for the value of `y`!

<img class="img-fluid" src="/static/assets/f23/lists00-sol.png" alt=""  /> --->

*Image Descriptions:*
Under Globals:
* Variable f has id 0, it is a function labeled Fn [1-4] on the Heap.
* Variable g id 1, it is a function labeled Fn [1-6] on the Heap.
* Variable record id 2, it is a list object on the Heap with the type list[str].

The f function frame has:
* Return Address (RA) pointing to line 13.
* Variables x and y, where x has id 2, and y with a value of 1 and a crossed-out value of 0.
* Return Value (RV) with a value of "yx".

The g function frame has:
* Return Address (RA) pointing to line 14.
* Variables x has id 2, new_list has id 3 which is list object on the Heap with type list[str].
* Variable z has the crossed-out string "xx", with a final value of "yx".
* Return Value (RV) has id 3.

The Heap section shows two list objects and two string objects:
* The first list on the heap has two values. The first value is “xx” with a crossed-out value of “x”. The second value is “yx” with a crossed-out value of “y”.
* The second list on the heap has two values. The first value is “xx” and the second value is “yx”.

The Output section at the top first prints “yx”, then the list [“xx”,”yx”]. 
