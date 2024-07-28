---
title: While Loop Questions
author:
- Alyssa Lytle
- Megan Zhang
- David Karash
page: lessons
template: overview
---

# Questions

## Conceptual

1. Produce a memory diagram for the following code snippet, being sure to include its stack and output.  

        WORD: str = "happy"
        l1_idx: int = 0
        l2_idx: int = 0
        t1: str = ""
        t2: str = ""
        n_appearances: int = 0

        while l1_idx < len(WORD):
            t1 = WORD[l1_idx]
            n_appearances = 1
            l2_idx = 0

            while l2_idx < len(WORD):
                t2 = WORD[l2_idx]

                if (t1 == t2) and (l1_idx != l2_idx):
                    n_appearances = n_appearances + 1
                l2_idx = l2_idx + 1
            print(f"{WORD[l1_idx]} appears {n_appearances} times.")
            l1_idx = l1_idx + 1

1.1 What would happen if `while l1_idx < len(WORD)` in line 8 was replaced with `while l1_idx < len(WORD) - 1`? Why?

1.2 What would happen if `l2_idx=0` was moved to inside the second while loop? In other words, what if lines 11-13 were changed to:


```
    while l2_idx < len(WORD):
        l2_idx = 0
```

1.3 What would happen if, in line 16, `if (t1 == t2) and (l1_idx != l2_idx):` was replaced with `if (t1 == t2):`? Why?

1.4 What would happen if line 18 (`l2_idx = l2_idx + 1`) was removed? Why?

1.5. What would happen if the `<` symbol in line 8 was replaced with `<=`? (In other words, what if it was changed to `while l1_idx <= len(WORD):`)? Why?


[Solutions](#conceptual-solutions)

# Solutions

## Conceptual Solutions

1. 
<img class="img-fluid" src="/static/practice_worksheets/sp23/q1_sol1.png" alt ="The memory diagram includes a box on the top labeled Output and a box on the bottom labeled Stack, next to an empty area labeled Heap. 
The Stack contains the variables WORD, l1 underscore idx, l2 underscore idx, t1, t2, and n underscore appearances. The WORD variable contains the value happy in quotes. 
The variable l1 underscore idx has the value of 5, with previous values of 0, 1, 2, 3, and 4 all crossed out. L2 underscore idx has the final value of 5, with previous values of 0, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, and 4 all crossed out. T1 has the final value of y with previous values of an empty string, h, a, p, p, and y all in quotes and crossed out. T2 has the final value of y (in quotes) with previous values of an empty string, h, a, p, p, y, h, a, p, p, y, h, a, p, p, y, h, a, p, p, y, h, a, p, and p all in quote and crossed out. Finally, the variable n underscore appearances has the final value of 1 with previous values of 0, 1, 1, 1, 2, 1, and 2 all crossed out. 
The output box contains the sentence h appears 1 times. Below that, on a separate line is the output a appears 1 times. Next, is the line p appears 2 times., p appears 2 times., and y appears 1 times. each on separate lines. 
"/>

(We do not *require* that you write out all interim values as long as the initial and final values are correct like in the solution below. However, writing the interim values will help for practice purposes and to avoid mistakes!)

<img class="img-fluid" src="/static/practice_worksheets/sp23/q1_sol2.jpg" alt="The memory diagram has three columns, labeled from left to right Stack, Heap, and Output. Under the stack, there is a frame labeled Globals. 
The globals frame contains the variables WORD, l1 underscore idx, l2 underscore idx, t1, t2, and n underscore appearances. The WORD variable contains the value happy in quotes. The variable l1 underscore idx has the value of 5 with the previous value of 0 crossed out. The variable l2 underscore idx has the value of 5 with the previous value of 0 crossed out. The variable t1 has the final value of y in quotes, with the previous value an empty string in quotes crossed out. The variable t2 has the final value of y in quotes, with the previous value of an empty string in quotes crossed out. Finally, the variable n underscore appearances has the value 1 with the previous value 0 crossed out.
The heap column is empty.
The output column contains the sentence h appears 1 times. Below that, on a separate line is the output a appears 1 times. Next is the line p appears 2 times., p appears 2 times., and y appears 1 times. each on separate lines. 
">

**Here's a link to a [video of the solution](https://www.youtube.com/watch?v=NqNuPjnq-UE)!**

1.1 "y appears 1 times." would not print. This is because `l1_idx` will not enter the while loop for `l1_idx = 4`. (For more practice, it'd be good to diagram this instance out to see how it would impact the final values of other variables.)

1.2 An infinite loop would occur because `l2_idx` would always equal `1` when returning to the top of the loop, and therefore `l2_idx < len(WORD)` will always be True.

1.3 If `l1_idx != l2_idx` is no longer required, this means that each letter can count itself twice. For example, `WORD[0] == WORD[0]` is true, so `n_appearances` for `"h"` would increase to `2`.

1.4 There would be an infinite loop because `l2_idx` will never increase, and therefore `l2_idx < len(WORD)` will always be True.

1.5 There would be an index error because there would be the case where `l1_idx = 5`, so on line 9 `WORD[5]` would be searching for the element at index 5 in `"happy"`, when the indexes only go up to 4.
