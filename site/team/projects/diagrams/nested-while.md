---
title: Practice Memory Diagram
author:
- Cora Rogers-Vickers
page: lessons
template: overview
---

# Snippet

<pre>
<code class="python">   """A nested while loop."""
    num_1: int = 1

    while num_1 <= 3:
        num_2: int = 1
        while num_2 <= 5:
            print(num_1 * num_2)
            num_2 += 1
        print("")  
        num_1 += 1
</code></pre>

# Solution

<!-- <img class="img-fluid" src="" alt="(Image Description as one line:) The memory diagram includes a column on the left titled Stack and a column on the right titled Output. The stack contains vars num_1 and num_2, and the output has the multiplication tables for 1-3."  /> -->

*Image Description:* 

The memory diagram includes a column on the left titled Stack and a column on the right titled Output. 

The stack contains:

* only one frame - globals
* within globals are the two variables: num_1 and num_2
* num_1 starts at 1 and ends at 4
* num_2 starts at 1, goes 2,3,4,5 and then back down to 1 again.  It does this three times, ending at 5 on the third loop.
* The output contains the multiplication tables up to 5 for 1-3.  On separate lines it contains 1,2,3,4,5, then 2,4,6,8,10, then 3,6,9,12,15.  There is a blank line space between each table.



