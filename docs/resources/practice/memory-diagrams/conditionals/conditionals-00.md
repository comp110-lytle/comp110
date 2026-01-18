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

    x: str = "Hello"
    y: int = len(x)
    if y % 4 == 1:
        y *= 2
    y -= 6
    print(y)
    print(x[y])
</code></pre>

# Solution

[Video](https://youtu.be/o73Rk9ni5Rc)

<img class="img-fluid" src="/static/assets/f23/conditionals-00-sol.png" alt="The memory diagram includes a column on the left titled Stack and a column on the right titled Output. The stack contains variable `x` with value ''Hello'' and variable `y` with the original value of 5 crossed out and updated to 10, then crossed out and updatd again to 4. The Output has the value 4 and the string ''o''."  /> 

*Image Description:* The memory diagram includes a column on the left titled Stack and a column on the right titled Output. 

The stack contains variable `x` with value "Hello" and variable `y` with the original value of 5 crossed out and updated to 10, then crossed out and updatd again to 4. 

The Output has the value 4 and the string "o".