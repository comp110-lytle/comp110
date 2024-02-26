---
title: Practice Memory Diagram
author:
- Created by Kaleb White
- Edited by Rosey Anim, Alyssa Lytle
page: lessons
template: overview
---

# Snippet

<pre>
<code class="python">   def big_func(num: int) -> int:
        a: int = num + 2
        return a

    def bigger_func(num: int) -> int:
        a: int = big_func(num) * 2
        return a

    def biggest_func(num: int) -> int:
        a: int = bigger_func(num) ** 2
        return a

    def main() -> None:
        a: int = 110 
        a = biggest_func(a)
        print(f"Wow! {a} is a big number!")

    main()
</code></pre>

# Solution

<img class="img-fluid" src="/static/practice-mem-diagrams/func-import-00-sol.png" alt=""/>