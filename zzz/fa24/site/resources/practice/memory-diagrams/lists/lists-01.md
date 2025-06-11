---
title: Practice Memory Diagram
author:
- Created by Navya Katraju
- Reviewed by Olivia Xiao
- Published by Alyssa Lytle
page: lessons
template: overview
---

# Snippet


<pre>
<code class="python">    def check_quiz(responses: list[bool]) -> int:
        answer_key: list[bool] = [True, True, False]
        correct: int = 0
        idx: int = 0
        while idx < len(responses):
            if responses[idx] == answer_key[idx]:
                correct += 1
                idx += 1
            else:
                idx += 1
        return correct

    def main() -> None:
        my_quiz: list[bool] = [True, True, True]
        grade: int = check_quiz(my_quiz)
        print(f"{grade} out of 3 questions correct.")


    main()
</code></pre>

# Solution

[Video](https://youtu.be/ZAH1mpf6GKc?si=8BgFglBAlJ4QJJQS)

<img class="img-fluid" src="/static/practice-mem-diagrams/lists-01-sol.jpg" alt=""/>


*Image Description*

The Memory Diagram includes one box titled Output and below that box two columns, the left one titled Stack and the right one titled Heap.

The Stack includes 3 frames in the following order from top to bottom including Globals, main, and check_quiz.

The Globals frame has 2 variables including check_quiz and main.
- check_quiz has id 0, it is a function on the Heap (lines 1-11).
- main points id 1, it is a function on the Heap (lines 14-17).

The main frame has 4 items including the RA and RV, and variables named my_quiz and grade.
- The RA is defined at line 19.
- The RV is None.
- my_quiz has id 2, it is a list[bool] on the Heap.
    - Indexes 0, 1, 2 and values True, True, True respectively.
- grade is 2.

The check_quiz frame has 6 items including the RA and RV, and variables named responses, answer_key, correct, and idx.
- The RA is defined at line 15.
- The RV is 2.
- responses has id 2.
- answer_key has id 3, it is a list[bool] on the Heap.
    - Indexes 0, 1, 2 and values True, True, False respectively.
- correct is 2.
    - Previous values of correct include 0 and 1, which are now crossed out.
- idx is 3.
    - Previous values of idx include 0, 1, and 2, which are now crossed out.

The Heap includes 2 function objects, and 2 list[bool] objects.

Output includes the phrase: “2 out of 3 questions correct.” 