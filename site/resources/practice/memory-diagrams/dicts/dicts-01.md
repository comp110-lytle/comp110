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

<img class="img-fluid" src="/static/assets/f23/dicts01-sol.png" alt=""  />
