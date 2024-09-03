---
title: Practice Memory Diagram
author:
- Created by Kaleb White
- Edited by Rosey Anim, Alyssa Lytle
- Solution by Viktorya Hunanyan
page: lessons
template: overview
---

# Snippet

<pre>
<code class="python">   def big_func(a: int) -> int:
        return a + 2

    def bigger_func(b: int) -> int:
        return big_func(a=b) * 2

    def biggest_func(num: int) -> int:
        return bigger_func(b=num) ** 2

    def main() -> None:
        print(str(biggest_func(num=110)) + " is a big number!")

    main()
</code></pre>

# Solution
<img class="img-fluid" src="/static/practice-mem-diagrams/big_func.jpg" alt="Image Description Here"  />

## Video

[Video](https://youtu.be/vpPrAIKvMPk)

## Image Description
*(Coming Soon)*

<!-- [Video](https://youtu.be/TOeZrIu0GnQ?si=uKDO2Ym6Wdi3RBKT)

<img class="img-fluid" src="/static/practice-mem-diagrams/func-import-00-sol.png" alt=""/> -->