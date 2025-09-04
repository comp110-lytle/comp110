---
title: Practice with Conditionals, Local Variables, and User Input
author:
- Alyssa Lytle
page: lessons
template: overview
---

# Practice with Conditionals, Local Variables, and User Input

## Part 0. Introduction and Setup

For this challenge question, you are going to be writing a simple number guessing game!

First, right click on your "CQs" folder and select "New File...". Name this file `cq00_conditionals.py`.

Make sure to initialize your file with a docstring and `__author__` variable!

## Part 1. `guess_a_number`: Signature

Now, let's write a function that takes no inputs and doesn't return anything called `guess_a_number`. All inputs will be made by the user and nothing will be returned, but rather displayed in your terminal! 

Start by just creating the signature and having the function `return None`. We will add more to it in a bit

## Part 2. Calling your Function

Let's go ahead and call our function to see what it does!

Below your function definition call `guess_a_number()`. 

Now, try running your file! You'll notice you don't get any output yet because even though your function is being called, it doesn't do anything yet!

## Part 3. `guess_a_number`: Giving it Functionality

###  3.0 Establish a Secret Number

First, let's establish a secret number for the player of the game to guess! 
Create a *local variable* inside your function body that is called `secret`, is an `int` and equals `7`. (You'll get a warning line under your variable, but that's ok! It's just because we haven't used it yet.)


### 3.1 User Input

Next in the code, you should ask the player to "Guess a number: " using the `input` function and store their response as a *local variable* in the function. 

Then, print back the following string *exactly*: "Your guess was x", where `x` is the number they input.

Here's an example of what it should look like in your terminal:

<pre>
<div class="terminal">
/workspace (main*) > python -m CQs.cq00_conditionals
Guess a number: 7
Your guess was 7
</div>
</pre>

and in your trailhead:
<img class="img-fluid" src="/static/cqs/cq02/guess_trailhead.png">

### 3.2 Give Feedback

Now, you should tell the player whether or not their guess was correct, too high, or too low! You can do this using your conditionals!

* If their guess is correct, print `"You got it!"`
* If their guess is too low, print `"Your guess was too low! The secret number is x"` where `x` is the value of the secret number.
* If their guess is too high, print `"Your guess was too high! The secret number is x"` where `x` is the value of the secret number.

Here's an example of what it should look like in your terminal:

<pre>
<div class="terminal">
/workspace (main*) > python -m CQs.cq00_conditionals
Guess a number: 7
Your guess was 7
You got it!
</div>
</pre>

<pre>
<div class="terminal">
/workspace (main*) > python -m CQs.cq00_conditionals
Guess a number: 9
Your guess was 9
Your guess was too high! The secret number is 7
</div>
</pre>


<pre>
<div class="terminal">
/workspace (main*) > python -m CQs.cq00_conditionals
Guess a number: 2
Your guess was 2
Your guess was too low! The secret number is 7
</div>
</pre>


and in your trailhead:
<img class="img-fluid" src="/static/cqs/cq02/correct_guess.png">

<img class="img-fluid" src="/static/cqs/cq02/high_guess.png">

<img class="img-fluid" src="/static/cqs/cq02/low_guess.png">

## Part 4. Add `__name__ == "__main__"`

Finally, replace the line where you call `guess_a_number()` with:

```
    if __name__ == "__main__":
        guess_a_number()
```

Right now, you're just doing this because it's good practice, but we will explain why you do it soon! However, now that you know conditionals, you can get some intuition behind what it's doing. It's checking the value of some variable `__name__` and only calling your function if `__name__ == "__main__"`. More on this later! ;)

## Part 5. Submission

Create a .zip file by running the following command in your terminal:

```python -m tools.submission CQs/cq00_conditionals.py```

Then, drag and drop that .zip file into Gradescope!