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

x: int = 2
y: str = "yo"
z: str = "2"
if len(y) > 1:
    y *= x
else:
    y = "no"
if x > 0:
    print(z)
print(y)    
</code></pre>

# Solution

<img class="img-fluid" src="/static/assets/sp24/conditionals-01-sol.png" alt="The memory diagram includes a column on the left titled Stack and a column on the right titled Output."  /> 

*Image Description:* 
The memory diagram is divided into two main sections: Stack and Output.

In the Stack section, under the label Globals, there are three variables displayed:
* Variable x with the value 2.
* Variable y with the original value "yo" crossed out and updated to "yoyo".
* Variable z with the value "1".

In the Output section, the following are displayed in a vertical sequence:
* The number 2.
* The string "yoyo"
