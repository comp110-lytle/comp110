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

    a: str = "a"
    b: str = a + "b" + "b"
    print(b + a)
    a = a + str(len(b))
    print(a)
</code></pre>

# Solution

[Video](https://youtu.be/gz98DsakdiU)

<img class="img-fluid" src="/static/assets/f23/basic-02-sol.png" alt="The memory diagram includes box on top labeled output, and below that a column on the left titled Stack and a column on the right titled Heap. The stack contains variable `a` with initial value ''a'' crossed out and updated to ''a3'' and variable `b` with the value ''abb''. The Output has the strings `abba` and `a3`. "  /> 

*Image Description:*

The memory diagram includes box on top labeled output, and below that a column on the left titled Stack and a column on the right titled Heap. The stack contains variable `a` with initial value ''a'' crossed out and updated to ''a3'' and variable `b` with the value ''abb''. The Output has the strings `abba` and `a3`.