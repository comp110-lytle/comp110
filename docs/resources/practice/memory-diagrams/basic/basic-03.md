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

    age: int = 20
    year: int = 2024
    older_age: int = age + 10
    later_year: int = year + 10
    print("In " + str(later_year) + " you'll be " + str(older_age))
</code></pre>

# Solution
<img class="img-fluid" src="/static/assets/sp24/basic-03-sol.png" alt=""  /> 



*Image Description:* 

The memory diagram consists of two sections labeled "Stack" and "Output." The Stack section has one frame titled "Globals," containing four variables with corresponding values: age with a value of 20, year with a value of 2024, older_age with a value of 30, and later_year with a value of 2034. The Output section contains a single string that reads: "In 2034 you'll be 30".