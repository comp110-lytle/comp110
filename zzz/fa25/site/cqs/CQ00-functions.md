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

## Function Definition: `mimic`

Now, you are going to write a function on your own! This function will just take your input and repeat it back to you! *Define a function* with the following expectations:

- Name: `mimic`
- Parameters: 
  - `message` parameter of type `str` - the message that we will be mimicing!
- Return type: `str`
- Add a Docstring describing the purpose of the function.

The function should simply return `message` back to you!

You can test this function by *calling* it under the "Interact" tab of your trailhead! You should get behavior looking something like this: 

<img class="img-fluid" src="/static/cqs/cq00/mimic.png">

## Function Definition: `main`

Now you are going to write your `main` function! This is a common convention in programming. The `main` function pulls together your functions, which are building blocks, into a main function that implements the high-level logic of your program. 

This program is only going to print the result of calling `mimic`. It won't actually *return* anything, so you can declare it's return type as `None`.

Define the signature of this function with the following expectations:

- Name: `main`
- Parameters: no parameters
- Return type: `None`
- Add a Docstring describing the purpose of the function.

The body of your function should contain the following line: 

```
 print(mimic(message="Howdy!"))
```
To understand what this line of code is doing, just like in math, you can expect to work your way from the innermost parentheses outward.

You'll see that it is *calling* the `mimic` function with the argument `message="Howdy!"`, and then in the outer parentheses is it *printing* the result. This is called a *nested function call* because the result (aka *return value*) of the `mimic` function is then being passed as an argument to the `print` function.

You can test this function by *calling* it under the "Interact" tab of your trailhead! You should get behavior looking something like this: 

<img class="img-fluid" src="/static/cqs/cq00/main_call.png">


## Calling Your Function Inside the File

Before you do anything else, try clicking on the "Run" tab in your trailhead. You'll see something like this.

<img class="img-fluid" src="/static/cqs/cq00/no-output.png">

This is to be expected because so far `cq00_functions.py` only contains a function *definitions*; nothing has been *called* in your file!

Let's edit the module to *call* the `main` function when it's run! At the bottom of your `cq00_functions.py` file, add the following lines of code to the bottom of your file (note the indentation, as it is important!):

```python
if __name__ == "__main__":
  main()
```

Before revealing what this code is doing, please try saving your code and look under the "Run" tab in the Trailhead. You should see something like this:

<img class="img-fluid" src="/static/cqs/cq00/howdy_output.png">

You'll notice it is *calling* the `main` function which in turn prints the result of calling the `mimic` function with the argument `message="Howdy!"`!

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

Try it out in your trailhead! You should see something like this!

<img class="img-fluid" src="/static/cqs/cq00/name_main_call.png">

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