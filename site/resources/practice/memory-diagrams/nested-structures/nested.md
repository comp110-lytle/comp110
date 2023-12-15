---
title: Practice Memory Diagram
author:
- Alyssa Lytle
page: lessons
template: overview
---

# Snippet
        def mystery(x: list[dict[str, int]], y: str) -> int:
            idx: int = 0
            total: int = 0
            while idx < len(x):
                temp: dict[str,int] = x[idx]
                if y in temp:
                    total += temp[y]
                idx += 1
            return total

        y: list[dict[str, int]] = [{"Happy": 1, "Birthday": 2}, {"Happy": 3, "Tuesday": 4}]
        mystery(y, "Happy")
        print(y[0])

# Solution


<img class="img-fluid" src="/static/practice-mem-diagrams/nested-sol.png" alt="Image Description Here"  />

## Image Description 
*(Coming Soon)*
