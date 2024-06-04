---
title: Practice Memory Diagram
author:
- Alyssa Lytle
page: lessons
template: overview
---

# Snippet

```
    def column_vals(table: list[dict[str, str]], header: str) -> list[str]:
        """Return a list of all values under a specific header."""
        result: list[str] = []
        # loop through each element (dictionary) of the list
        for elem in table:
            # for each dictionary (elem), get the value at key "header" and add that to result
            result.append(elem[header])
        return result


    def columnar(table: list[dict[str,str]]) -> dict[str, list[str]]:
        """Reformat data so it's a dictionary with column headers as keys"""
        result: dict[str, list[str]] = {}
        # loop through keys of one row of the table to get the headers
        first_row: dict[str,str] = table[0]
        for key in first_row:
            # for each key (header), make a dictionary entry with all the column values
            result[key] = column_vals(table, key)
        return result

    data: list[dict[str,str]] = [{'Comp': '110', 'Bio': '100'}, {'Comp': '210', 'Bio': '200'}]
    columnar(data)
```

# Solution


<!-- <img class="img-fluid" src="/static/practice-mem-diagrams/data-sol.png" alt="Image Description Here"  /> -->

<!-- ## Image Description  -->
*(Coming Soon)*
