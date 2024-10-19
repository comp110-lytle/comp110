---
title: Practice Memory Diagram
author:
- Alyssa Lytle
- Viktorya Hunanyan
page: lessons
template: overview
---

# Snippet

```
    def column_vals(table: list[dict[str, str]], header: str) -> list[str]:
        """Return a list of all values under a specific header."""
        result: list[str] = []
        for elem in table:
            result.append(elem[header])
        return result


    def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
        """Reformat data so it's a dictionary with column headers as keys."""
        result: dict[str, list[str]] = {}
        first_row: dict[str, str] = table[0]
        for key in first_row:
            result[key] = column_vals(table, key)
        return result

    data: list[dict[str, str]] = [{'Comp': '110', 'Bio': '100'}, {'Comp': '210', 'Bio': '200'}]
    columnar(data)
```

# Solution


<img class="img-fluid" src="/static/mem-diags/columnar-mem.jpg" alt="Image Description Here"  />

## Image Description 
*(Coming Soon)*
