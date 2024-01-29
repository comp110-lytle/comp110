---
title: Practice Memory Diagram
author:
- Alyssa Lytle
page: lessons
template: overview
---

# Snippet

<pre>
<code class="python">    """ Practice Memory Diagram """

    a: str = "Mardi"
    b: str = "Gras"
    c: str = a[0] + a[len(b)]
    a = "yay!"
    print(c)
</code></pre>

# Solution

[Video](https://youtu.be/wxsA4kdyyUA)

<img class="img-fluid" src="/static/assets/f23/basic-01-sol.png" alt="The memory diagram includes box on top labeled output, and below that a column on the left titled Stack and a column on the right titled Heap. The stack contains variable `a` with initial value ''Mardi'' crossed out and updated to ''yay'', variable `b` with the value ''Gras'', and variable `c` with the value ''Mi''. The Output has the string `Mi`. "  />

*Image Description:* 
The memory diagram includes box on top labeled output, and below that a column on the left titled Stack and a column on the right titled Heap. 

The stack contains variable `a` with initial value ''Mardi'' crossed out and updated to ''yay'', 

variable `b` with the value ''Gras'', 

and variable `c` with the value ''Mi''. 

The Output box contains the string `Mi`. 