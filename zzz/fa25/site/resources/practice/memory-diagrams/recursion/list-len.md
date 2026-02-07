---
title: Practice Memory Diagram
author:
- Alyssa Lytle
page: lessons
template: overview
---

# Snippet

```
    def list_length(my_input: list[str]) -> int:
        if len(my_input) == 0:
            return 0
        else:
            my_input.pop(0)
            return 1 + list_length(my_input)
        
    a: list[str] = ["Tar", "Heels", "!"]
    list_length(a)
```

# Solution
[Solution Video](https://youtu.be/OxXJzYIHwfg)


<img class="img-fluid" src="/static/practice-mem-diagrams/list-len-rec.png" alt="Image Description Here"  />

## Image Description 
*(Coming Soon)*
