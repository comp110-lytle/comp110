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

    i: int = 0
    s: str = ""

    while i < 4:
        if i % 2 == 0:
            s += "h"
        elif i % 3 == 0:
            s += "!"
        else:
            s += "e"
        i += 1
    print(s)
</code></pre>

# Solution

[Video](https://youtu.be/Uj6OGZuW464?si=mbgy26DKt4A5onN-)


<img class="img-fluid" src="/static/mem-diags/while-00.png" alt=" " />

