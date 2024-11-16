---
title: Practice Memory Diagram
author:
- Viktorya Hunanyan
page: lessons
template: overview
---

# Snippet

```python
    def remove_all_occurrences(lst, value):
        i = 0
        while i < len(lst):
            if type(lst[i]) == list:
                remove_all_occurrences(lst[i], value)
                if len(lst[i]) == 0:
                    lst.pop(i)
                else:
                    i += 1
            elif lst[i] == value:
                lst.pop(i)
            else:
                i += 1

    lst1 = [1, 2, 3, 2, 4, 2, 5]
    remove_all_occurrences(lst1, 2)
    print(lst1)

    lst2 = [2, [1, 2, [2, 3]], 4, 2]
    remove_all_occurrences(lst2, 2)
    print(lst2)
```

# Solution
*(Coming Soon)*
<!-- [Solution Video](https://youtu.be/mr_7bk3F6to)

<img class="img-fluid" src="/static/practice-mem-diagrams/silly-loop.png" alt="Image Description Here"  />  -->

## Image Description 
*(Coming Soon)*