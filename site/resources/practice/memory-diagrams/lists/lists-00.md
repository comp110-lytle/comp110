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


* Note that for this solution, we did not represent the `range()` function on the heap! We instead just represented `y` as a variable on the stack that gets updated. If you chose to include a "range" object to the heap, we wouldn't take points off, but we are really just looking for the value of `y`!

<img class="img-fluid" src="/static/assets/f23/lists00-sol.png" alt=""  />

