---
title: Practice Memory Diagram
author:
- Viktorya Hunanyan
page: lessons
template: overview
---

# Snippet

```python
    def increment_values(dct):
        for key in dct:
            value = dct[key]

            if type(value) == int:
                dct[key] = value + 1

            elif type(value) == dict:
                increment_values(value)

    dct1 = {'a': 1, 'b': 2, 'c': 3}
    increment_values(dct1)
    print(dct1)

    dct2 = {'x': 5, 'y': {'a': 1, 'b': 2}, 'z': 3}
    increment_values(dct2)
    print(dct2)
```

# Solution
*(Coming Soon)*
<!-- [Solution Video](https://youtu.be/mr_7bk3F6to)

<img class="img-fluid" src="/static/practice-mem-diagrams/silly-loop.png" alt="Image Description Here"  />  -->

## Image Description 
*(Coming Soon)*