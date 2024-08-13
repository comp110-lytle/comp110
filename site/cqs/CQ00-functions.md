---
title: Functions Challenge Question 
author:
- Alyssa Byrnes
page: lessons
template: overview
---

## Introduction and Setup

These Challenge Questions are designed to help you implement some of the concepts you've learned on small problems before you handle larger problems in your exercises!

To start, right click in the "Explorer" pane of your workspace and select "New Folder...". Name this new folder `CQs`. This is where you will be writing and storing your challenge questions this semester!

Now, right click on your "CQs" folder and select "New File...". Name this file `cq00_functions.py`. *The `.py` at the end of the file name is necessary, or your program won't run!*

Make sure to initialize your file with a docstring and `__author__` variable just like you did in EX00!

## Function Definition

Now, you are going to write a function on your own! This function will just take your input and repeat it back to you! *Define a function* with the following expectations:

- Name: `mimic`
- Parameters: 
  - `message` parameter of type `str` - the message that we will be mimicing!
- Return type: `str`
- Add a Docstring describing the purpose of the function.

The function should simply return `message` back to you!

You can test this function by *calling* it under the "Interact" tab of your trailhead! You should get behavior looking something like this: 

<img class="img-fluid" src="/static/cqs/cq00/mimic.png">

## Calling Your Function Inside the File

Before you do anything else, try clicking on the "Run" tab in your trailhead. You'll see something like this.

<img class="img-fluid" src="/static/cqs/cq00/no-output.png">

This is to be expected because `cq00_functions.py` only contains a function definition; nothing has been called or printed!

Let's edit the module to call the function when it's run! At the bottom of your `cq00_functions.py` file, add the following lines of code to the bottom of your file (note the indentation, as it is important!):

```python
if __name__ == "__main__":
    print(mimic(message="Howdy!"))
```

Before revealing what this code is doing, please try saving your code and look under the "Run" tab in the Trailhead. You should see something like this:

<img class="img-fluid" src="/static/cqs/cq00/mimic-module-call.png">

Now, come back to the code, and try and break down the second line for yourself. Just like in math, you can expect to work your way from the innermost parentheses outward.

You'll see that it is *calling* the `mimic` function with the argument `message="Howdy!"`, and then in the outer parentheses is it *printing* the result. This is called a *nested function call* because the result (aka *return value*) of the `mimic` function is then being passed as an argument to the `print` function.

The first line, `if __name__ == "__main__":` is a special kind of statement called a *conditional statement* you'll learn about in a few weeks. The effect it has here is when you run this program in the "Run" tab, the indented code beneath the `if` statement will be evaluated. However, when you load this program in the REPL of the "Interact" tab, the code beneath the if statement will not be run. This gives us the best of both worlds! We will learn more about *how* this works in the future, but for now it's good to just know that it provides you with this functionality!

## Prompting For User Input

Finally, we are going to make our module a little more interactive by prompting the user for input! 

Change the line:


```python
print(mimic(message="Howdy!"))
```

to: 

```python
print(mimic(message=input("What is your message?")))
```

Again, before we explain what this does, try saving your code and look under the "Run" tab in the Trailhead. You should see that it prompts you for a message. Type in any message and hit enter. It should repeat that message right back to you!

Similar to the `print` function, `input` is a function that has built-in behavior. The *argument* will be whatever message you want displayed to the user. (E.g. `"What is your message?"`) The *return* value will be a `str` with whatever input the user has typed. Notice that it is passing the return value of the `input` function as an argument to the `mimic` function, which is why it repeats the user input back to you!


## Submission

Just like you did for EX00, create a .zip file by running the following command in your terminal:

```python -m tools.submission CQs/cq00_functions.py```

Then, drag and drop that .zip file into Gradescope!

## Congratulations!

You completed your first challenge question! Hopefully now you're more comfortable with the following concepts:

* Defining a function
* Calling a function in the "interact" tab of the trailhead
* Calling a function within the module
* The basic behavior behind the line `if __name__ == "__main__":`
* The `input` function
* Nested function calls