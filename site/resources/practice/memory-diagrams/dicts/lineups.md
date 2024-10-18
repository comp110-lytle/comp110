---
title: Practice Memory Diagram
author:
- Created by Coralee Rogers
- Reviewed by Alyssa Lytle
page: lessons
template: overview
---

# Snippet

```
    starting = dict[str, list[str]] = {}
    starting["2017"] = ["Berry", "Meeks", "Jackson"]
    starting["2023"] = ["Love", "Bacot", "Black"]

    print(starting["2017"][2])
    print(starting["2023"])
    starting["2023"][2] = "Johnson"
    print(starting["2023"])
```

# Solution
<img class="img-fluid" src="/static/practice-mem-diagrams/lineup-sol.png" alt="Image Description Here"  />

*Image Description:*
The memory diagram provided contains three main components: Stack, Heap, and Output.

Stack:
* The Stack section contains a single frame labeled "Globals."
* Inside Globals, there is a variable named starting pointing to a list on the Heap.

Heap:
* The first part is a dictionary object with string keys and lists of strings for values. There are two keys: "2017" and "2023." Each key points to a different list.
* The second part consists of two lists of strings. Each list contains five elements with indices from 0 to 4.
* The first list contains the following strings: "Berry", "Meeks", "Jackson", "Pinson", and "Hicks".
* The second list contains the strings: "Love", "Bacot", "Black", "Johnson" (with “Nance” crossed-out), and "Davis".

The output section has three outputs:
* The string “Jackson”
* The list [“Love”, “Bacot”, “Black”, “Nance”, “Davis”]
* The list [“Love”, “Bacot”, “Black”, “Johnson”, “Davis”]