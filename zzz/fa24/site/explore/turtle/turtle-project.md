---
title: Turtle Scene Project
author:
- Kris Jordan
- Ezri White
page: projects
---

## Overview

In this project you will design a structured program _and a beautifully artistic scene painted painstakingly on your screen, and ours, by our little `Turtle` friends_.

Before beginning this project, you should complete the [Turtle Graphics Introduction Tutorial](/explore/turtle/turtle-tutorial.html).

The scene you choose to create should have some element in it that repeats / is reused at least three times. Perhaps it's a forest of trees, or a house with many windows, or a flock of birds scattered in the distance, maybe it's stars in the night sky, or snowflakes floating fancily about. Pick a scene that sparks joy and transports you to a place of [hygge](https://www.youtube.com/watch?v=kE5pSH3lQxU) and happiness.

If you need inspiration, [look no further](https://www.youtube.com/watch?v=0n4f-VDjOBE). Remember, when learning how to program there are no mistakes, just happy, little accidents.

## Learning Objectives

1. You will gain experience breaking a complex task you want to achieve into smaller, parameterized functions. This technique is called problem decomposition.
2. You will gain experience passing objects to functions and becoming more comfortable with the idea of procedures.
3. You will gain experience reading official documentation in order to achieve your vision without knowing exactly what tools you have available at the onset.
4. You will produce a program that is longer and more involved than any of the earlier exercises.

## Requirements

This is an open-ended project and we encourage both exploration and pushing yourself. The rubric applied to your project is as follows:

1. Define at least four separate _procedures_ whose purpose is to draw visual components of your scene and are meaningfully named to describe what component they'll draw. These procedures must make use of at least three parameters: one `Turtle` object parameter and two `float` parameters for the `x` and `y` coordinates of _where_ to start drawing the component on your canvas. You are encouraged to implement other "helper" procedures that abstract simpler ideas for use in your required procedures (for example, a procedure that draws a `line` between any two coordinates or a `rectangle` procedure). For this project you are required to use the `turtle` package's object-oriented interface as shown in the tutorial and the examples of this document.

2. Have a `main` _procedure_ whose purpose is to construct any `Turtle` objects and make use of the component procedures described in the previous requirement to place the components of your scene. It does not need to take any parameters. After your functions are all defined, including `main`, you should use the `if __name__ == "__main__":` idiom demonstrated in [Lesson 12 - Magic 8-Ball Tutorial](/students/lessons/ls12-magic-8ball.html).

3. Call at least one of your four required component procedures twice to place that component twice in your scene in different locations.

4. Use a `while` loop to avoid repetitive code in some part of your scene.

5. Fill at least one shape in your scene with a color other than white.

6. Change the marker's tracing color for at least one shape in your scene to something other than black. This is demonstrated in the [Turtle Tutorial](/students/resources/turtle_tutorial.html).

7. Static Types - Be sure to specify each function's _parameter's types_ and _return type_.

8. Linting: Good, Pythonic style - refer to the [Style Guide](/students/resources/style-guide.html) for help.

9. Effortful and meaningfully descriptive `docstring` documentation for the module (top of file) and each function definition.

Hitting the low bar on the minimum requirements with the minimal effort possible will result in a maximum score of 85%. To earn beyond 90%, we will look for the following criteria and ask that you use the file's `docstring` to document which of these points you are attempting and tell us where to look in your program to find them (specific line numbers).

10. Avoid any single function from becoming _too_ complex. When programming in general, if you find yourself writing a very complex function, it's likely you should break it down further into simpler functions. To earn credit for this, break your most complex component procedure besides `main` down further into simpler, but still meaningfully named procedures. To earn credit for this, your component procedure should _call_ these simpler procedures.

11. Impress us by trying out something you find interesting! Describe what you are attempting here in the file's `docstring` so we know what to look for. Remember, a `docstring` can span more than one line, it just ends with the `"""`. Some ideas you could try for here:

* Read through the `Turtle` documentation page to find a function to use that we did not make use of in the turtle tutorial and make use of it in your project: <https://docs.python.org/3.8/library/turtle.html#turtle-methods>
* Use loops and procedures in clever ways to draw an interesting pattern or complex component
* Make clever use of randomness in your scene by using a function imported from the `random` module: https://docs.python.org/3.8/library/random.html
* Go above and beyond with a scene more complex than could be achieved with only four components added to it.

It is worth noting it is very *ok*, and perhaps expected, for your scene to look like a drawing you might have been proud of in kindergarten. Such is the nature of doing art on a medium you're new to. The end visual result is less interesting than the process by which you got there. Your grade will not be impacted by the ultimate beauty of your creation. With that said, drawing 5 lines on the screen with as little effort as possible and calling it "art" may very well be _art_, but will likely not result in full credit. You should be able to look at your program and appreciate that you put significant effort into it.

## Getting started

In your course workspace, expand the `projects`. Right click in `projects` and add a file named `turtle_project.py`.

You can use the following template to begin your program. Unlike the tutorial, you will need to write functions which control your scene.

We'll begin by adding a `main` function that takes no parameters and, since it is a _procedure_ has a return type of `None`.

~~~ {.python .numberLines startFrom="1"}
"""TODO: Describe your scene program."""

__author__ = "Your PID"

from turtle import Turtle, colormode, done 


def main() -> None:
    """The entrypoint of my scene."""
    # TODO: Declare your Turtle variable(s) here.
    # TODO: Call the procedures you define and pass your Turtle(s) as an argument.
    done()

# TODO: Define the procedures for other components in your scene here.

# TODO: Use the __name__ is "__main__" idiom shown in 
~~~

To give you an example of what is expected in your four "component" procedures, consider this one that draws a _square_ and adds an additional _parameter_ for you to control the width of the square:

~~~ {.python .numberLines startFrom="1"}
def draw_square(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a square of the given width whose top-left corner is located at x, y."""
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    i: int = 0
    while i < 4:
        a_turtle.forward(width)
        a_turtle.right(90)
        i = i + 1
~~~

Your component procedures, and any other "helper" functions you define, can add whatever additional parameters you'd like. Notice that parameters tend to give your procedures extra flexibility. If the `draw_square` function did not have a `width` parameter, then it could only draw squares of the exact same, "hard-coded" width.

The `Turtle` object's `setheading` method takes a `float` value that is the _degrees_ to face the turtle in. So, in the example above, each time the `draw_square` procedure is called the turtle's heading is reset to head toward `0.0` degrees (along the x-axis headed in a positive direction). Since your component procedures do not know the starting position of the turtle or the direction it is heading in, you will likely benefit from using `goto` and `setheading` to move it and face it in the direction you'd like.

After defining this procedure we could call it from the _body_ of the `main` function to draw a few squares. For example, by replacing `...` with the following `Turtle` variable construction and `draw_square()` calls:

~~~ {.python .numberLines startFrom="1"}
def main() -> None:
    """The entrypoint of my scene."""
    ertle: Turtle = Turtle()
    draw_square(ertle, -5, 5, 10)
    draw_square(ertle, -10, 10, 20)
    draw_square(ertle, -15, 15, 30)
    draw_square(ertle, -20, 20, 40)
    done()
    # Challenge: Try rewriting those four repeated calls in a loop
    # and using arithmetic expressions to calculate each of the arguments
    # based on your counter variable's value rather than hard coded int
    # literals. For example, the first argument could be: (i + 1) * -5

~~~

## Have fun, get creative!

------

## Submission Instructions

To prepare your scene for submission, be sure to add a docstring to your module (at the top of the file) and a global `__author__` variable set to a string which contains your 9-digit PID. If you are attempting the final 15% of the project, also be sure to describe what to look for in your program per the instructions above. Add that description to your docstring.

The programmer's job is not completed merely by achieving some desired functionality. Programming is a craft and a programmer's work should be documented and adhere to common stylistic rules. Autograding for this assignment performs checks for the 25 points dedicated to such concerns: _linting_ and _static type checking_. These checks are focused on nit-picky improvements. Developing good habits around fixing these concerns as you move through your programming career will pay dividends, just like brushing your teeth.

Here are a few suggestions for cleaning up your code in anticipation of _static type checking_:

1. Be sure you declare every parameter's type
2. Be sure you declare every return type (since most of this project is _procedural_, it's likely they're `None`)

Read the [Style, Linting and Autograder](/students/resources/style-guide.html) guide in anticipation of _linting_ (style checking). 

On your first submission, you are likely to see a number of lint and type checking issues arise. Don't be dismayed! Remember, each is telling you the line number to find the issue on and describes what the issue is. Many of these rules the linter will teach you through some trial and error and by the end of the course you will be in the practice of writing code in a good, Pythonic style. If you do not understand the suggestions, refer to the [Style, Linting, and Autograder guide](/students/resources/style-guide.html#how-to-read-the-autograder).

To build your submission, run `python -m tools.submission projects/pj00_turtle_scene.py` to build your submission zip for upload to Gradescope. Don't forget to backup your work by creating a commit and pushing it to GitHub. For a reminder of this process, see the previous exercises.

## Frequently Asked Questions

### How can I get my scene to render faster?

Start by increasing your `Turtle` object's speed to the maximum speed. For example, if you have a `Turtle` variable named `bob`, you could increase its speed with `bob.speed(MAX_SPEED)` where `MAX_SPEED` is a constant set to `0` per the [official documentation](https://docs.python.org/3.8/library/turtle.html#turtle.speed).

Once you have the hang of writing procedures and a feel for how interacting with Turtle objects work, you can further supercharge your Turtle with some "hacks". By default the `Turtle` renderer will update the scene as your method calls occur. However, for complex scenes it's often desireable to have the scene drawn instantaneously. To do so we will disable the tracer from updating until your scene is completed. You will need to import the functions `tracer` and `update` from the `turtle` package, alongside `done` and `colormode`. Then, you can update your `main` function to turn off tracing and update after your scene instructions complete:

~~~ {.python .numberLines startFrom="1"}
def main() -> None:
    """The entrypoint of my scene."""
    tracer(0, 0)  # Disable delay in tracing
    ...  # TODO: your code
    update()  # Now update the rendering
    done()
    
~~~

Note that updating the speed of your rendering in this way is entirely optional and not expected.