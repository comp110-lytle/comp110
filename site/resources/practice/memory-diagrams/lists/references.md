---
title: Practice Memory Diagram
page: lessons
template: overview
---

# Snippet

<pre>
<code class="python">   """Practice diagram."""

    def create() -> list[int]:
        """An obnoxious way to make a list."""
        list_1: list[int] = []
        i: int = 0
        while i < 3:
            list_1.append(i)
            i += 1
        return list_1


    def increase (a_list: list[int], x: int) -> None:
        """Lets pump it up!"""
        i: int = 0
        while i < len(a_list):
            a_list[i] += x
            i += 1
        return None


    def main() -> None:
        """Entrypoint of the program."""
        list_1: list[int] = create()
        list_2: list[int] = list_1
        list_1 = create()
        increase(list_1, 2)

        print(list_1)
        print(list_2)


    if __name__ == "__main__":
        main()
```
</code></pre>

# Solution


