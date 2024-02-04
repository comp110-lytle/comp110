---
title: Practice Memory Diagram
author:
- Alyssa Lytle
page: lessons
template: overview
---

# Snippet
<pre>
<code class="python">   """ Practice Memory Diagram """

    x: int = 10
    result: str = ""

    while x >= 0:
        if x % 3 > 0:
            result = result + str(x)
        else:
            result = str(x) + result
        x = x - 1

    print(result)
</code></pre>

# Solution

<img class="img-fluid" src="/static/mem-diags/while-02-sol.jpg" alt=" " />