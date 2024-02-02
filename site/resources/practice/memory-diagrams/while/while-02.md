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
Coming sooon

<!-- [Video](https://youtu.be/ihPlv30PAeg?si=cjvtNKLicOluykVU)

<img class="img-fluid" src="/static/assets/f23/basic-00-sol.png" alt="The memory diagram includes a column on the left titled Stack and a column on the right titled Output. The stack contains variable `b` with value ''Partner'' and variable `a` with the original value of ''Howdy'' crossed out and updated to ''Howdy Partner''. The Output has the string `Howdy Partner`. "  />

*Image Description:* The memory diagram includes a column on the left titled Stack and a column on the right titled Output. The stack contains variable `b` with value ''Partner'' and variable `a` with the original value of ''Howdy'' crossed out and updated to ''Howdy Partner''. The Output has the string `Howdy Partner`. " -->