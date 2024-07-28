---
title: For Loops Questions
author:
- Alyssa Lytle
- Megan Zhang
- David Karash
page: lessons
template: overview
---

# Questions

## Conceptual

1.1 Rewrite the following code snippet with same functionality using a `for ... in` loop.
1.2 Rewrite the following code snippet with same functionality using a `for ... in range(...)` loop.

```
    stats: list[int] = [7, 8, 9]
    index: int = 0
    total: int = 100
    while index < len(stats):
        total -= stats[index]
        index += 1
```


[Solutions](#conceptual-solutions)

# Solutions

## Conceptual Solutions


1.1
```
    stats: list[int] = [7, 8, 9]
    total: int = 100
    for elem in stats:
        total -= elem
```

1.2
```
    stats: list[int] = [7, 8, 9]
    total: int = 100
    for index in range(0, len(stats)):
        total -= stats[index]
```