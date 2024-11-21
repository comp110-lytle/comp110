---
title: Practice Memory Diagram
author:
- Viktorya Hunanyan
page: lessons
template: overview
---

# Snippet

```python
    def reverse_list_with_twist(lst, left, right):
        if left >= right:
            return None

        if lst[left] % 2 == 1 and lst[right] % 2 == 1:
            reverse_list_with_twist(lst, left + 1, right - 1)
        else:
            temp = lst[left]
            lst[left] = lst[right]
            lst[right] = temp
            reverse_list_with_twist(lst, left + 1, right - 1)

    lst1 = [1, 2, 3, 4, 5, 6]
    reverse_list_with_twist(lst1, 0, 5)
    print(lst1)
```

# Solution
*(Coming Soon)*
<!-- [Solution Video](https://youtu.be/mr_7bk3F6to)

<img class="img-fluid" src="/static/practice-mem-diagrams/silly-loop.png" alt="Image Description Here"  />  -->

## Image Description 
*(Coming Soon)*