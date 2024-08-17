---
title: Graders Guide to Grading Comments
author:
  - Alyssa Lytle
  - Viktorya Hunanyan
page: logistics
template: overview
site-branch: team
---

This semester, we are hoping to make commenting mandatory! We hope this will encourage students to think critically about what makes sense and why, helping them make important conceptual leaps. Grading comments will be part of the manual grading process, as many exercises already include this element. We are incorporating it into every write-up, requiring meaningful comments that describe what is happening. These comments don't need to be extensive but should reflect a good-faith effort to explain the process in the student's own words.

This document is intended to guide anyone involved in grading. 

## Good vs Bad Commenting

### Good Commenting

1. <img class="img-fluid" src="/static/assets/good_ex_one.png"/>

   **Reason:**

   This is from Wordle. This is an example of good commenting because it clearly shows that the student understands what they have learned so far – instantiating variables, loops, user input, concatenating, and reassigning variables. When students learn a new topic, it is expected for them to identify where they are using it. Because this was their first introduction to while loops, especially having a nested while loop, it makes sense why there is this much commenting. Even though these comments clearly show a conceptual understanding, they do not have to be this extensive, especially as we tend towards the end of the semester. 

2. <img class="img-fluid" src="/static/assets/good_ex_two.png"/>

   **Reason:**
   
    This is from dict_utils. This is an example of good commenting because it clearly shows that the student understands what is happening at each step. In terms of dictionaries, they identify what they are iterating through with respect to a dictionary object. Even though they have learned to instantiate variables, the student still comments “create blank dict to hold…”. This is good commenting as opposed to simply saying “instantiating an empty dictionary” since it gives a reason for why they are doing what they are doing. Sometimes this isn’t necessary. For example ‘max: int = 0’. Since students are already familiar with instantiating variables and using them to hold values (such as with indexing), commenting on this process is not necessary but still shows that the student understands what the use of the dictionary is for. 

3. <img class="img-fluid" src="/static/assets/good_ex_three.png"/>

   **Reason:**
   
    This is dict_utils. This is an example of good commenting because it clearly shows that the student understands what is happening at each step and is explaining it in their own words. Even when some things are obvious to us, we have to keep in mind that for the majority of students this is their first time coding. Comments like “iterate through all ‘keys’ in our input dict” serve as reminders for students about what the for loop is doing, translating the code into plain English. While most of the comments state the “obvious”, there are two lines that show the student is really trying to understand. These are: 

        “tis makes the value of blank_dict now the key”
        
        “therfore ‘inverts’ the two” 

4. <img class="img-fluid" src="/static/assets/good_ex_four.png"/>

   **Reason:**
   
    This is from list_utils. Notice that non-extensive commenting doesn’t always mean bad commenting. Here, the student kept comments to a minimal but noted conceptual details. Before list_utils, students have already learned to iterate using a while loop, are familiar with indexing, functions, and conditionals. Now they are practicing iterating through lists and practicing obtaining values from the list. The comments could improve on specifying that to obtain a value in the list you must index on the list but overall this is an example of good commenting. 


### Bad Commenting

1. <img class="img-fluid" src="/static/assets/bad_ex_one.png"/>

   **Reason:**

    This is dict_utils. This is an example of not so great commenting because it simply points out things that students have already learned. They already learned to instantiate a variable and have had practice with return statements. This does not show any sort of conceptual understanding of what is happening in the code, especially about what the exercise is testing them on (dicts and lists). 


    To improve, one comment can be sufficient! Since elem already describes each value in inp_list, there's no need to comment on what is being iterated over, as the variable names are self-explanatory. The if statement is also clear about what it is testing, so a comment like "if the element is a key in our_dict" is not necessary. However, a comment in the else block is appropriate, as it explains the condition that is not met by the if statement and clarifies why the else block differs (i.e., why we assign 1 as a value at a key instead of incrementing it). Although some comments may not be necessary, students are still encouraged to include them if they find it helpful. For example, as seen in the second-to-last example in the “Good” section, translating code into plain English can aid in understanding and improve clarity.

    <img class="img-fluid" src="/static/assets/improved_ex_one.png"/>

2. **NO COMMENTS == BAD COMMENTING.**

    **No comments imply that there were no challenges or moments spent considering how to approach a code.** It's quite rare for a student to complete every exercise, code question, and practice problem without engaging in some form of problem-solving. Even as a TA, I always use a piece of paper to map out my approach when working on practice problems. This process often results in comments being added to my code. 
    
    As a general rule, **if 2 or more minutes are spent thinking about how to write a particular line or block of code, it’s a good idea to add a comment.** Explain what’s happening on that line, how the solution was reached, the reasoning behind the approach, or provide a note for future reference to recall the problem-solving steps.

**!!!!!!**

As mentioned above, comments don't need to be extensive, but they should reflect a genuine effort to explain the process in the student's own words. We don’t want to be too pedantic about commenting so that it doesn’t start feeling like a chore to be done at the end of coding. Instead, it should be an integral part of the problem-solving process. Sometimes stating the obvious is fine, but you can notice a “good-faith” effort usually at the end of a function or section of code where everything comes together like in the second-to-last example in the “Good” section.

If you notice that many students are not making a sincere effort to comment and explain their code, let us know and we will issue an announcement to emphasize the importance of good commenting and provide examples of what that looks like.

**!!!!!!**

## When Would You Usually Expect to See Comments?

As the semester progresses, we anticipate fewer comments on basic concepts like simple `while` loops, variable instantiation, and value assignment, as students should become comfortable with these topics. Instead, we expect comments to focus on specific objects, values (especially with nested data types), and conceptual ideas in OOP. However, at the start of the course, it's important to see comments that may seem obvious, such as `#instantiating a variable ‘bear’ to hold the string value “Good doggy!”` or `#returning a string`. These comments often serve as clarifications for students who are just beginning to learn computational thinking.

We expect comments to appear when students first learn a new topic. As they progress, comments on earlier topics will naturally decrease, with the focus shifting to newer concepts.

### Key Moments to Expect Comments:

- When introducing a new topic or concept (e.g., `for` loops, `for…in range()` loops, lists, dictionaries, class objects, accessing attributes locally vs. globally).
- When working with nested data types: Comments should help clarify the structure and access patterns of nested data types, such as lists of dictionaries, or dictionaries of lists. This is particularly important when navigating or modifying nested structures.
- When implementing complex logic or algorithms (e.g., recursion, searching algorithms, programs where there are a lot of reassignments or variables to store values), should be thoroughly commented to explain the thought process, the purpose of each step, and any edge cases considered.
- When handling errors or exceptions, especially if there are multiple possible outcomes or if the handling is non-obvious.

## Encourage Commenting!

When helping a student and noticing that they don’t know where to start or have conceptual misunderstandings, start by walking them through the problem as you normally would, explaining the key concepts and steps. Afterward, ask the student to walk you through the problem by explaining it back to you. This will help reinforce their understanding and reveal any remaining gaps in their knowledge.

Once they've explained the problem, instruct them to comment on their code in the same way they explained it. Encourage them to identify and annotate the key moments where everything starts to make sense or when they gain a deeper understanding of the concept. These comments should serve as markers of their learning process, highlighting not only the technical steps but also their growing comprehension.

Additionally, remind them to:

- Focus on the logic and flow: Have them comment on why each part of the code is necessary and how it contributes to solving the problem.
- Identify breakthrough moments: Encourage them to note when they understand a tricky concept, such as how a loop iterates through a data structure or how a function returns a value.
- Highlight areas of uncertainty: If they’re still unsure about certain parts, suggest that they leave comments to indicate these areas for further review or discussion.
- Reflect on the problem-solving approach: Ask them to comment on their approach to solving the problem, including any alternative strategies they considered and why they chose the final one.