---
title: Image Descriptions
date: 2021-02-25
author:
  - Vrinda Desai
  - Alyssa Lytle
page: logistics
template: overview
site-branch: team
---

# Image Descriptions

An image description is meant for someone who is using a screenreader to be able to understand an image completely. In other words, they should know exactly what is on your memory diagram without physically looking at it! 

Below are a few examples:

## Intro Memory Diagram (No Heap): 

The memory diagram includes a column on the left titled Stack and a column on the right titled Output. The Stack contains variable `b` with value ''partner'' and variable `a` with the original value of ''Howdy'' crossed out and updated to ''Howdy Partner''. The Output has the string `Howdy Partner`.

## Full Memory Diagram:
The Memory Diagram includes one box titled Output and below that box two columns, the left one titled Stack and the right one titled Heap.

The Stack includes 4 frames in the following order from top to bottom including Globals, main, date_night, get_ready.

The Globals frame has 3 variables including date_night, get_ready, and main. 
date_night is assigned `id:0`, which corresponds to a function on the Heap marked with `id:0, lines 2-6`.
get_ready is assigned `id:1`, which corresponds to a function on the Heap marked with `id:1, lines 9-21`.
main is assigned `id:2`, which corresponds to a function on the Heap marked with `id:2, lines 24-26`.

The main frame has 2 items including the RA and RV.
The RA is defined at line 30.
The RV is None.

The date_night frame has 2 items including the RA and RV and 1 variable named x.
The RA is defined at line 25.
The RV is True.
x is 5.

The get_ready frame has 2 items including the RA and RV and 3 variables including excited, y, and outfit..
The RA is defined at line 26.
The RV is “pajamas” (in quotes).
excited is False. 
Previous values of excited include True which is now crossed out.
y is 7.
outfit is “pajamas” (in quotes).
Previous values of outfit include “swimsuit” which is now crossed out.


Output includes the phrase: “I’ll wear my pajamas!”
