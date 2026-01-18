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

    a: int = 2
    b: int = 6
    if a > b:
        print(a-b)
    elif b < 10:
        print(b/a)
    else:
        print(a+b)
    print(b)
</code></pre>

# Solution

<img class="img-fluid" src="/static/assets/f23/elif-00-sol.png" alt="The memory diagram includes a column on the left titled Stack and a column on the right titled Output. The stack contains variable `a` with value 2 and variable `b` with the value 6. The Output has the value 3.0 and the value 6. "  />

*Image Description:*
The memory diagram is divided into two sections: Stack and Output.

In the Stack section, under the label Globals, there are two variables:
* Variable a with the value 2.
* Variable b with the value 6.

In the Output section, two values are shown in a vertical sequence:
* The string "3.0".
* The string "6", which is the value of variable b.
