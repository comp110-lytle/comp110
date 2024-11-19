---
title: Practice Memory Diagram
author:
- Viktorya Hunanyan
page: lessons
template: overview
---

# Snippet

```python
    def remove_all_occurrences(inp_list, val):
        i = 0
        while i < len(inp_list):
            if type(inp_list[i]) == list:
                remove_all_occurrences(inp_list[i], val)
                if len(inp_list[i]) == 0:
                    inp_list.pop(i)
                else:
                    i += 1
            elif inp_list[i] == val:
                inp_list.pop(i)
            else:
                i += 1

    my_list = [1, 2, 3, 2, 4, 2, 5]
    remove_all_occurrences(my_list, 2)
    print(my_list)

    my_sec_list = [2, [1, 2, [2, 3]], 4, 2]  # you can ignore the type on this -- types in python are funky
    # this does not mean ignore types -- this is just one exception
    remove_all_occurrences(my_sec_list, 2)
    print(my_sec_list)
```

# Solution
*(Coming Soon)*
<!-- [Solution Video](https://youtu.be/mr_7bk3F6to)

<img class="img-fluid" src="/static/practice-mem-diagrams/silly-loop.png" alt="Image Description Here"  />  -->

## Image Description 
*(Coming Soon)*