---
title: EX05 - River Simulation 
author:
  - Alyssa Byrnes
  - Sophie Jiang
page: exercises
template: overview
---


For this exercise, you are going to practice making and instantiating classes in order to simulate a small river ecosystem with bears and fish! You will see that some "skeleton code" has been set up for you to fill in. 

# Part I

<!-- ## 0. Pull the skeleton code

You will find the starter files needed by "pulling" from the course workspace repository. Before beginning, be sure to:

0. Be sure you are in your course workspace. Open the file explorer and you should see your work for the course. If you do not, open your course workspace through File > Open Recent.
1. Open the _Source Control View_ by clicking the 3-node (circles) graph (connected by lines) icon in your sidebar or opening the command palatte and searching for _Source Control_.
2. Click the Ellipses in the Source Control pane and select "Pull" from the drop-down menu. This will begin the pulling process from the course repository. It should silently succeed.
3. Return to the File Explorer pane and open the `exercises` directory. You should see it now contains another directory named `ex05`. If you expand that directory, you should see the starter files for the code you'll be writing.
4. If you do not see the `ex05` directory, try once more but selecting `"Pull From"` and select `origin` in step 2.

### Troubleshooting
If you're having trouble pulling:

* Make sure you PUSHED all of your changes to backup first!!!
* In your terminal, type `git config pull.rebase false`
* In your Visual Studio command center, select `Pull From...` -> `Upstream` -> `Upstream/Head`. (If not an option, do `Origin` -> `Main`.) 

If you're still having issues, come to office hours!
 -->

## 1. Create Bear Class
All of the work for this part will be done in the `ex05` directory in the file `bear.py`.

### 1.1 `class Bear` attributes
For this part, you are going to create and initialize a class to represent the Bears living by the river. In the file `bear.py`, you will see a class defined with the name `Bear`. Give it the attributes `age` and `hunger_score` which is are both integers. (You won't use `hunger_score` in Part I, but it'll be useful later!)

### 1.2 `Bear#__init__`
Within the `Bear` class, modify `__init__` so that it initializes both `self.age` and `hunger_score` with the value `0`.



## 2. Create Fish Class

Now we are going to create a class to represent the fish in the river. 

### 2.1 `class Fish` attributes
In the `fish.py` file, there will be a class defined called `Fish`. Like `Bear`, give it have the attribute `age` which is an integer. (It does *NOT* need a `hunger_score` attribute.) 

### 2.2 `Fish#__init__`
Within the `Fish` class, modify `__init__` so that it initializes `self.age`  with the value `0`.

## 3. Create River Class

Now that you have some animals, you can create and populate a river! 

### 3.1 `class River` attributes
In `rivers.py`, give the class `River` the following attributes:

- `day`: an `int` that tells you what day of the river's lifecycle you are modeling
- `bears`: a `list` of  `Bear`s that stores the river's bear population
- `fish`: a `list` of  `Fish` that stores the river's fish population

The `__init__` method is already defined for you. It takes as parameters: `self`, `num_fish: int`, `num_bears: int` and does the following:

* initializes `self.fish` to contain `num_fish` many Fish
* initializes `self.bears` to contain `num_bears` many Bears
* initializes `self.day` to be `0`

### 3.2 Create a new River 
Call the `__init__` method by opening `river_simulation.py`, and constructing a river named `my_river` with 10 `Fish` and 2 `Bears`. (Don't forget to import the `River` class!)

### 3.3 `view_river()` method

Now, you are going to modify the method inside your `River` class called `view_river` which will print the river status out to you.

#### Define 

`view_river` should behave such that: 

- It takes no parameters other than `self` and returns nothing.

- It should print the following:  

<pre>
<div class="terminal">~~~ Day x: ~~~
Fish population: y
Bear population: z
</div>
</pre>

Where `x` is the current day of the river, `y` is the number of Fish in the river, and `z` is the number of Bears in the river. 

#### Call the method 

At the bottom of `river_simulation.py`, try viewing your river by calling `my_river.view_river()`. 

When you run `python -m exercises.ex05.river_simulation`, the output should be: 

<pre>
<div class="terminal">~~~ Day 0: ~~~
Fish population: 10
Bear population: 2
</div>
</pre>

## 4. Simulating "one day" and "one week" in the River
Now that you have a river with Bears and Fish, you can model how their population updates day-to-day.

`Bear` and `Fish` each have their own `one_day` method. Modify them so they have the following behaviors:

### 4.1 `Bear#one_day()`
The method `one_day()` in the `Bear` class takes no parameters other than `self` and does not return anything. It should increase the value of the `age` attribute by 1.

### 4.2 `Fish#one_day()`
The method `one_day()` in the `Fish` class takes no parameters other than `self` and does not return anything. It should increase the value of the `age` attribute by 1.

### 4.3 `River#one_river_week()` method
The method `one_river_day()` in the `River` class is defined for you. It'll do more once you've finished Part II, but notice that it calls the `one_day()` method for both the `Fish` and the `Bear`s.

Within the `River` class, define a method `one_river_week()` that takes no parameters other than `self` and does not return anything. It should simply call `one_river_day()` seven times.

At the bottom of `river_simulation.py`, test out the functionality of `one_river_week` by calling it. (You'll notice a pretty boring output. Don't worry, in Part II we will model population changes!)

# Part II

For Part II we will represent the circle of life... you will be simulating the life cycle of both the `Bear`s and the `Fish` in the `River`!


## 1. Removing Animals

### 1.1 `River#check_ages()`
As animal's age, they should be removed from the `River`. Modify the `check_ages` method so it has the following functionality.
If a `Fish`’s age is > 3 it should be removed from `fish`. 
If a `Bear`’s age is > 5 it should be removed from `bears`.

*Implementation hint:* You don't want to be removing things from a list *while* you're looping through it. Instead, create a new `list[Bear]` and copy all surviving `Bear`s over to that list rather than removing `Bear`s directly from `self.bears`. Then update `self.bears` to be equal to that copied list. Do the same thing for `self.fish`.

### 1.2 `River#remove_fish()`
Within the `River` class, create a `remove_fish` method that has `self` and `amount: int` as parameters and returns nothing. It should remove `amount` many `Fish` from the `River`. You should remove the **FRONTMOST** `Fish`. (The "front" being the `Fish` at index 0.)




## 2. Modelling Bear's Hunger
Now, unfortunately, comes the circle of life. A bear's gotta eat! This will involve modifying the `one_day()` method in the `Bear` class and making a new `eat()` method in the `Bear` class.

### 2.1 Modifying `Bear#one_day()`
Modify the method `one_day()` in the `Bear` class so that every day the `hunger_score` attribute decreases by 1.


### 2.2 `Bear#eat()` method
Now, you are going to create a new method in the `Bear` class called `eat()`. It has two parameters, `self` and `num_fish: int` and returns nothing.
It should update the `Bear`'s `hunger_score` so that it increases by `num_fish`. 
(For example, if `num_fish = 2`, a `Bear` ate 2 fish, so its `hunger_score` should increase by 2.)

### 2.3 Modifying `River#bears_eating`
Modify the `bears_eating` method, so that, for each `Bear`, if there are at least 5 `Fish` in the river, the `Bear` will eat 3 `Fish`. This involves removing 3 `Fish` from the river using the `remove_fish` method and calling `eat()` for the number of fish the `Bear` eats. 



### 2.4 Modifying `River#check_hunger`

Unfortunately, if a `Bear` gets hungry enough, it'll starve. Modify the `check_hunger` method so that it checks the `hunger_score` of every `Bear` in the river. If `hunger_score < 0`, then remove the `Bear` from the river.


*Implementation hint:* You don't want to be removing things from a list *while* you're looping through it. Instead, create a new `list[Bear]` and copy all surviving `Bear`s over to that list rather than removing `Bear`s directly from `self.bears`. Then update `self.bears` to be equal to that copied list.

## 3. Modelling Reproduction
Now we are going to model the reproduction of the Bears and the Fish! 

### 3.1 `River#repopulate_bears`

Modify the `repopulate_bears` method so that it has the following functionality.Each *pair* of Bear's will produce 1 offspring. In other words, if there are 2 bears, 1 new bear will be born and added to `bears`. To generalize, for `n` bears, there will be `n//2` new `Bear`s added to `bears`. 


### 3.2 `River#repopulate_fish`
Modify the `repopulate_fish` method so that it has the following functionality. Each *pair* of fish will produce 4 offspring. In other words, if there are 2 fish, 
4 new fish will be born and added to `fish`. To generalize, for `n` fish, there will be `(n//2) * 4` new `Fish` added to `fish`. 

## Autograding


Login to Gradescope and select the assignment named "EX05 - River Simulation". You'll see an area to upload a zip file. To produce a zip file for autograding, return back to Visual Studio Code.

If you _do not_ see a Terminal at the bottom of your screen, open the Command Palette and search for "View: Toggle Integrated Terminal".

To produce a zip file for `ex05`, type the following command (all on a single line):

`python -m tools.submission exercises/ex05`

In the file explorer pane, look to find the zip file named "yy.mm.dd-hh.mm-exercises-ex05.zip". The "mm", "dd", and so on, are timestamps with the current year, month, day, hour, minute. If you right click on this file and select "Reveal in File Explorer" on Windows or "Reveal in Finder" on Mac, the zip file's location on your computer will open. Upload this file to Gradescope to submit your work for this exercise.

Autograding will take a few moments to complete. For this exercise there will be points manually graded for style – using meaningful variable names and snake_case. If there are issues reported, you are encouraged to try and resolve them and resubmit. If for any reason you aren’t receiving full credit and aren’t sure what to try next, come give us a visit in office hours!