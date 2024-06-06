---
title: Practice Memory Diagram
author:
- Kris Jordan
- Alyssa Lytle
page: lessons
template: overview
---

# Snippet

<pre>
<code class="python">   """Practice diagram."""

    def change_and_check(x: int, nums: list[int]) -> int:
        """Let's see what happens!"""
        if x < 0:
            return 0
        i: int = 0
        while i < len(nums):
            nums[i] += x
            i += 1
        i = 0
        while i < len(nums):
            if nums[i] == x:
                return 0
            i += 1
        return x - 1


    def main() -> None:
        """The entrypoint of this program."""
        num_1: int = 0
        list_1: list[int] = [1, 2, num_1]
        list_1.append(change_and_check(2, list_1))
        list_1.append(change_and_check(3, list_1))

    main()
</code></pre>

# Solution
<!-- 
<img class="img-fluid" src="/static/practice-mem-diagrams/change-and-check.png" alt="Image Description Here"  /> -->
