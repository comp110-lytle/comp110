---
title: Turtle Tutorial
author:
- Ezri White
- Edited by Alyssa Lytle
page: resources
template: overview
---

Python's turtle graphics library will allow us to use the different coding concepts we've learned so far to create fun patterns and designs! The turtle is essentially an invisible pen that we can code to move around our screen and draw. 

This tutorial will run through some common commands used with the turtle and you will have a fun mini-project at the end!

Begin by creating a Python program file in your `lessons` directory named `turtle_tutorial.py` 

You can run this file either by clicking the green play button or from the command line using:

`python -m lessons.turtle_tutorial`

## Importing and Setting Up the Turtle

Before we can begin using the turtle we have to import the library and set up our turtle object.

* To import a specific function or class: `from turtle import [function_name]`
* To set up a turtle object: `<_turtlevariable_> : Turtle = Turtle()`

Start by importing the following and then setting up our first turtle named `leo` (honoring the finest Ninja Turtle):

<pre>
<code class="python">    from turtle import Turtle, colormode, done
    leo: Turtle = Turtle()
</code> </pre>   



The second line _constructs_ a new `Turtle` object your program will control.

## Lines and Turning
In order to make the turtle do anything we will always use the syntax:

* `turtle_object_variable.method_name()`


* For example, with a variable named `leo`, bound to a `Turtle` object, you could move it forward to draw a line with: `leo.forward(distance)`
* To make the turtle move turn right: `leo.right(degrees)`
* To make the turtle move turn left: `leo.left(degrees)`

<pre>
<code class="python">   leo.forward(50)
   leo.left(30)
   leo.right(40)
</code> </pre>   

If you try running these commands, you may notice that a window pops up and then almost immediately disappears. We have to add an extra command to prevent this from happening.

* To make sure the window does not close until this function: `done()`

```
done()
```

The _done()_ function must come ___after___ all of the turtle functions that you want to see on the window.

#### Exercise One:

At this point you have all the commands needed to draw a square! Try and attempt this before moving onto the next section.

## Simplifying with Loops

After finishing exercise one you should have code that looks something like the following:

<pre>
<code class="python">    leo.forward(300)
    leo.left(90)
    leo.forward(300)
    leo.left(90)
    leo.forward(300)
    leo.left(90)
    leo.forward(300)
    leo.left(90)
</code> </pre>   

It should already be clear that this repetion is annoyingly tedious. Luckily, we can easily simplify this process.

* To repeat something a certain number of times: while (<_counter_variable_> < <_number_of_times_>):

<pre>
<code class="python">    i: int = 0
    while (i < 4):
        leo.forward(300)
        leo.left(90)
        i = i + 1
</code> </pre>   

#### Exercise Two:

Using the loop that we just made, try converting it into a triangle before moving on to the next section. 

## GoTo, Penup and Pendown

After finishing exercise two you should have code that looks like the following:

<pre>
<code class="python">    i: int = 0
    while (i < 3):
        leo.forward(300)
        leo.left(120)
        i = i + 1
</code> </pre>   

Now, what if we wanted to position our triangle in a different spot on the screen?

* To move the turtle to a new x, y position: <_turtlevariable_>.goto(<_x_coordinate_>,<_y_coordinate_>):

```
leo.goto(45, 60)
```


If you try running the above code before drawing the triangle you will notice an unwanted line is drawn. We need to lift the turtle off the page before using the goto!

* To prevent the turtle from drawing: <_turtlevariable_>.penup() __or__ <_turtlevariable_>.up()
* To allow the turtle to draw: <_turtlevariable_>.pendown() __or__ <_turtlevariable_>.down()

<pre>
<code class="python">    leo.penup()
    leo.goto(45, 60)
    leo.pendown()

    i: int = 0
    while (i < 3):
        leo.forward(300)
        leo.left(120)
        i = i + 1
</code> </pre>   

Before moving onto the next section, reposition your triangle so that it looks centered and make sure the size of the triangle is relatively large.

### Pen Color

There are actually two common ways to change the color of the turtle! To complete this next section, open https://htmlcolorcodes.com/color-picker/ in a new tab.

* To change the color with a string value: <_turtlevariable_>.color("<_color_>")

```
leo.color("blue")
```


While this is useful for the basic colors it doesn't leave much room for creativity. In order to have more control over our colors we can use RGB (red, green, blue) values instead. Using the color picker, use the site to pick out your favorite color and copy the three numbers next to RGB.

* To enable RGB mode, add under the import statement: colormode(255)

```
colormode(255)
```
   

* To change the color with RGB values: <_turtlevariable_>.color(<_red_>, <_green_>, <_blue_>)

```
leo.color(99, 204, 250)
```
 

Red, Green and Blue are the primary colors of the digital world! By choosing different amounts of each color you are essentially mixing together a new color like you would mix paint.

### Fill Color

To fill in a shape we just have to tell the turtle when to start filling and end filling. It will fill with whatever the current color is.

* To begin fill: <_turtlevariable_>.begin_fill()
* To end fill: <_turtlevariable_>.end_fill()

<pre>
<code class="python">    leo.begin_fill()
    # code for shape to be filled 
    leo.end_fill()
</code> </pre>   

### Other Useful Color Commands

Any of the color commands can either be used with a color string or with RGB values.

* To set only pen color: <_turtlevariable_>.pencolor(<_color_>)
* To set only fill color: <_turtlevariable_>.fillcolor(<_color_>)
* To set fill and pen color: <_turtlevariable_>.color(<_pencolor_>, <_fillcolor_>)

<pre>
<code class="python">    leo.pencolor("pink")
    leo.fillcolor(32, 67, 93)
    leo.color("green", "yellow")
</code> </pre>   

#### Exercise Three:

See if you can use the color picker to determine the maximum and minimum values for red, green and blue. What values give a pure white and pure black? Pick a grey color. What do you notice about the three numbers?

Fill in your triangle with your color of choice and make sure to end fill after the triangle is drawn!

## Speed, Visibility and the Fun Part

Before finishing the rest of the tutorial we may want to speed up our drawing as well as hide the turtle.

* To change the speed: <_turtlevariable_>.speed(<_speed_>)
* To end fill: <_turtlevariable_>.hideturtle() __or__ <_turtlevariable_>.ht()

<pre>
<code class="python">    leo.speed(50)
    leo.hideturtle()
</code> </pre>   

### Mini-Project

Now we have all of the basic commands needed for creating interesting patterns:

1. After your first triangle is created, we will set up a new turtle to do the rest of the work. Name this one `bob`.

```
bob: Turtle = Turtle()
```
  

2. Practice some of the tutorial commands by:
    * changing bob's color to black or a darker version of your triabgle color
    * using the goto, penup and pendown commands to position `bob` in the same spot that `leo` started.
    * set `bob`'s speed to a higher value

3. Create an outline of `leo`'s filled in triangle by having `bob` add another triangle without filling it in with the same size specifications as the original. 
4. Duplicate the code you created to have `bob` create an outline. We will use this second loop to add some more exciting linework. Turn the side length of the triangle into a variable and use it for both triangles. For instance:

<pre>
<code class="python">    side_length: int = 300

    i: int = 0
    while (i < 3):
        bob.forward(side_length)
        bob.left(120)
        i = i + 1
</code> </pre>   

5. Inside the second outline triangle loop, multiply the side length variable by a number from 0.95 to 0.98. This will decrease the length of the side each time it is drawn.

```
side_length = side_length * 0.97
```
  

6. Right now this will look like it is not changing much. Try increasing the number of loops of the second outline triangle to a much higher number. Mess around with this until it seems to fully recede!
7. For one last magic touch, try changing the degrees of the second outline loop to just over 120. Mess around with a range of 120.5 to 123 until you get a result you like!
8. By slightly changing the different number values at each of these steps you will get a different design. Have some fun seeing what you can make!

Note that these are examples of _magic numbers_ and should be given a meaningfully named constant definition to describe their purpose in a well styled, final product!