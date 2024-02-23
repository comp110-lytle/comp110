---
title: EX05 - Runtime Analysis
author:
- Alyssa Lytle
- Vrinda Desai
page: exercises
template: overview
---

 
## Introduction


<pre>
<div class="terminal">
   
</div>
</pre>


<pre>
<div class="terminal">
    $ python -m exercises.ex01_simple_battleship 
    Pick a secret boat location between 1 and 4: 2
    Guess a number between 1 and 4: 2
    🟦🟥🟦🟦
    Correct! You hit the ship.
</div>
</pre>

## Background Lesson: Emoji

In this exercise you will need to make use of an advanced string concepts: emoji! 🤠

Before beginning work on this exercise, read the following lesson and complete the related questions on Gradescope: [Unicode, Emoji, Escape Sequences, and f-Strings](/lessons/strings.html)

## 0. Pull the skeleton code

You will find the starter files needed by "pulling" from the course workspace repository. Before beginning, be sure to:

0. Be sure you are in your course workspace. Open the file explorer and you should see your work for the course. If you do not, open your course workspace through File > Open Recent.
1. Open the _Source Control View_ by clicking the 3-node (circles) graph (connected by lines) icon in your sidebar or opening the command palatte and searching for _Source Control_.
2. Click the Ellipses in the Source Control pane and select "Pull" from the drop-down menu. This will begin the pulling process from the course repository. It should silently succeed.
3. Return to the File Explorer pane and open the `exercises` directory. You should see it now contains another directory named `ex08`. If you expand that directory, you should see the starter files for the code you'll be writing.
4. If you do not see the `ex08` directory, try once more but selecting `"Pull From"` and select `origin` in step 2.

### Troubleshooting
If you're having trouble pulling, try:

* In your Visual Studio command center, select `Pull From...` -> `Upstream` -> `Upstream/Head`

If you're still having issues, come to office hours!


## Part 1. Linear Search


