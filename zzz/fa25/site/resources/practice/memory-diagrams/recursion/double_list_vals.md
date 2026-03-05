---
title: Practice Memory Diagram
author:
- Viktorya Hunanyan
page: lessons
template: overview
---

# Snippet

```python
    def double_elements(inp_list, index):
        if index < len(inp_list):
            inp_list[index] *= 2
            double_elements(inp_list, index + 1)

    my_list = [1, 2, 3, 4, 5]
    double_elements(my_list, 0)
    print(my_list)
```

# Solution
<!-- [Solution Video](https://youtu.be/mr_7bk3F6to) -->

<img class="img-fluid" src="/static/mem-diags/double_elements.jpg" alt="Image Description Here"  /> 

## Image Description 
*(Coming Soon)*