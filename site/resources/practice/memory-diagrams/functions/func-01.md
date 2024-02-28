---
title: Practice Memory Diagram
page: lessons
template: overview
---

# Snippet

<pre>
<code class="python">   """Practice diagram."""

    def main() -> None:
        """Entry point of program."""
        strings: list[str] = ["hey", "o", "eh", "e"]
        word: str = make_word(strings)
        print(word)


    def make_word(root: list[str]) -> str:
        """A nonsensical function that makes a 'word'."""
        word: str = ""
        i: int = 0
        while i < len(root):
            if i % 2 == 0:
                word += root[i]
            else:
                if len(word) < 5:
                    word += root[i]
                else:
                    return word
            i += 1
        return word


    main()
</code></pre>

# Solution


