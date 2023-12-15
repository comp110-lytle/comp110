---
title: Node Class
author:
- Alyssa Byrnes
page: lessons
template: overview
---
# Step 0: Pull the Workspace

You will find the starter files needed by "pulling" from the course workspace repository. Before beginning, be sure to:

0. Be sure you are in your course workspace. Open the file explorer and you should see your work for the course. If you do not, open your course workspace through File > Open Recent.
1. Open the _Source Control View_ by clicking the 3-node (circles) graph (connected by lines) icon in your sidebar or opening the command palatte and searching for _Source Control_.
2. Click the Ellipses in the Source Control pane and select "Pull" from the drop-down menu. This will begin the pulling process from the course repository. It should silently succeed.
3. Return to the File Explorer pane and open the `lessons` directory. You should see it now contains another directory named `recursion`. If you expand that directory, you should see the starter files for the code you'll be writing.
4. If you do not see the `lessons/recursion` directory, try once more but selecting `"Pull From"` and select `origin` in step 2.

### Troubleshooting
If you're having trouble pulling, try these:

* Try running `git config pull.rebase true` in your terminal and pull again!

* In your Visual Studio command center, select `Pull From...` -> `Upstream` -> `Upstream/Head`

* Try committing and pushing all of your work (like you do for exercises), and pull again!

If you're still having issues, ask for help/come to office hours!

# Step 1: Follow the instructions!

All of the instructions for Parts 0-2 are defined in `LinkedList.ipynb`!
You are going to be modifying the `Node` class inside the file `node.py`.

# Step 2: Submit!

Create a submission by running: 

`python -m tools.submission lessons/recursion`
