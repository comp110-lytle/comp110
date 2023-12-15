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

<img class="img-fluid" src="/static/assets/f23/dicts00-sol.png" alt=""  />
