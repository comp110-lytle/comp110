---
title: Environment Diagrams
author:
- Tori Hoffmann
page: resource
template: overview
---

## Environment Diagrams 101

### What is an environment diagram? 
- Environment diagrams are a visual aid that help us to trace through the execution of a program and keep track of the information we have stored on the stack and the heap at any given point!

### How to use an environment diagram: 
(1) First, we need to get all set up! Add columns for the stack, the heap, and the programs output. 
    - Reminder: 
        - The __stack__ is the program's "working space." It consists of a bunch of 'frames' that will correspond with each function call. The stack is specifically ordered and follows the same structure as your function calls!
        - The __heap__ is essentially dynamic memory. Variables that are reference types such as lists and objects live here!
(2) Add the globals frame to the call stack. This is always going to be your first frame on the stack and will hold __function definitions__ and any __global variables__.
    - For __function definitions__, write the name of the function in the globals frame and draw an arrow to the corresponding function object on the heap labeled: __Fn: [start line] - [end line]__.
    - Remember: __global variables__ are any variables defined outside of any context such as a function definition. If the variable isn't in the body of a function, it belongs here!
(3) Next, we have to deal with our first __function call__: the call to __main__! Remember, anytime a function is called it gets a frame on the stack that includes the following: 
    - The name of the function
    - The __return address__, or RA. This is the line where this function call was invoked and tells us where to return the function's return value when its execution is complete. 
    - The __return value__ of the function. 
    - Any __parameters__ or __local variables__ defined within that function.
        - Remember: Any reference types will live on the heap. To deal with this, we write the variable name in the frame on the stack and then point, or refer to, the data on the heap!
(3) Rinse and repeat! Anytime a new function is called, give it a frame on the stack and track all of it's important information! This way, the next time you are unsure what a variables value is, you have all the information you need right in front of you!

### Important Vocabulary Review
Wow, that's a lot of new vocab to remember! Below is a list of commonly used terms when talking about environment diagrams. Feel free to reference it anytime you find yourself getting confused!

- __Stack__: The program's "working space." It consists of a bunch of 'frames' that will correspond with each function call. The stack is specifically ordered and follows the same structure as your function calls!
- __Heap__: Dynamic memory! Variables that are reference types such as lists and objects live here!
- __Global Variables__: Variables defined outside of any context such as a function definition
- __Return Address__: This is the line where this function call was invoked. It tells us where to return the function's return value when its execution is complete. 
- __Return Value__: The value that is returned from a function call.
- __Current Frame__: The most recently added frame that has not returned. (No RV!)
- __Name Resolution__: The process of retrieving the value of a variable. A good rule of thumb for this is to look for name in the current frame. Not there? Check Globals frame!

## Environment Diagram Practice

Below are optional practice problems for drawing environment diagrams. Try tracing through the code blocks using the rules listed above!

### EX01: Classes
![](/static/assets/env-diagrams/code-blocks/env-classes.PNG)

#### Solution:

![](/static/assets/env-diagrams/diagrams/classes-solution.png)

### EX02: Linked Lists

![](/static/assets/env-diagrams/code-blocks/env-linked-list.PNG)

#### Solution:

![](/static/assets/env-diagrams/diagrams/recursion-solution.png)


### EX03: Recursion

![](/static/assets/env-diagrams/code-blocks/env-recursion.PNG)

#### Solution:

![](/static/assets/env-diagrams/diagrams/linked-list-solution.png)

Still looking for more practice? Check out the Environment Diagram Practice page in resources!