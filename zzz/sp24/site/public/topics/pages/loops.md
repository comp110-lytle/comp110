---
title: Loops
author:
- Claire Helms
page: resource
template: overview
---

## While Loops

A __while loop__ is a block of code that will continue 'looping' (repeating) until its boolean condition becomes false.

### Syntax

~~~ {.python .numberLines startFrom="1"}
while [boolean expression "test"]:
    # useful code that executes as long as the boolean 
    # expression is true (repeat block)

    # Manipulation of boolean condition (i.e. changing boolean 
    # expression "test" from True to False by manipulating 
    # counter variable, i.e. i += 1)
~~~

After the last statement in the repeat block completes, the computer will __jump backwards__ to the test and start anew. If the test evaluates to __True__, the computer will *move through 
the repeat block again*. If the test evaluates to __False__, the computer will 'exit' the loop, *skipping over the repeat block*.

### While Loop Checklist

1. Boolean condition
    1. Located after 'while' and before ':'
    2. Can use any boolean operator (==, !=, >, <. >=. <=)
    3. Can also use a boolean variable (a_condition)
2. Code inside the while block (repeat block) is useful
3. A 'counter' variable or boolean expression that will eventually become False and exit the loop – this should be placed inside the body of the while loop.

### Examples of Counters

__Numerical counter:__ 

~~~ {.python .numberLines startFrom="1"}
while i < 10:
    # looping code
    i += 1
~~~

Common ways to increment a numerical counter include:

~~~ {.python }
i += 1  # the same as i = i + 1
i -= 1  # the same as i = i - 1
~~~

The counter variable can also be incremented by numerical amounts other than 1.

~~~ {.python .numberLines startFrom="1"}
i = i + 3
i = i - 5
~~~

__Boolean expression:__

~~~ {.python .numberLines startFrom="1"}
weekend: bool = False
day_of_week: int = 1

while weekend == false:
    # looping code
    if day_of_week == 6 or day_of_week == 7:
        weekend = True
        print("Yay, it's the weekend!")
    day_of_week += 1
~~~

### Something is Wrong!

If your loop just won't end, you probably have implemented an *infinite loop*. Make sure that your condition can eventually become false! Example:

~~~ {.python .numberLines startFrom="1"}
# incorrect:

i: int = 0
while i < 110:
    print("I love COMP110!")
print("Done")
~~~

This is incorrect because the counter 'i' is __never changed__ and thus will never be >= 110. Therefore, the while loop will __INFINITELY__ execute and the string "Done" will never print.

~~~ {.python .numberLines startFrom="1"}
# correct:

i: int = 0
while i < 110:
    print("I love COMP110!)
    i += 1
print("Done")
~~~

Now, the while loop will execute 110 times, printing "I love COMP110 *each time*. The string "Done" will be printed once i = 110.

### Nested While Loops!

We can nest while loops, meaning we can place one while loop inside of another! Check out this example:

~~~ {.python .numberLines startFrom="1"}
sound: str = ""
i: int = 1  
while i < 20: 
    count: int = 0 # each time the outer loop runs, count is reassigned to 0
    while count < 4:
        i *= 2  # increase the value in i, the counter variable for the outer loop
        count += 1  # increment count, the counter variable for the inner loop
        sound += "e"
    sound += "-iii-"
sound += "oh"

print(sound)  # will print the string "eeee-iii-eeee-iii-oh"
~~~

These nested loops build up the string 'sound'. The inner loop starts over and runs through again each time we reenter the outer loop.


## For-in Loops

__for-in loops__ are similar to __while loops__, but instead of looping through a statement until a boolean condition changes, a __for-in loop__ iterates over a collection of items.

### The Syntax:

~~~ {.python .numberLines startFrom="1"}
for [identifier] in [sequence]:
    # useful code that processes each identifier(item) in a sequence(collection). (repeat block)
~~~

__identifier__ is a variable name you choose for *each item* in the repeat block. 

### How Does this Work?

The assignment of the __identifier__ to each item in the sequence is handled for you, and so is the progression from one item to the next. (Thank you, computers!)

The loop ends after the repeat block evaluates the last item.

__for-in loops__ are great for when you want to process *every item* in a collection. Collections can include __Lists__, __Dictionaries__, __Sets__, and even __Strings__! Anything *iterable* can be processed by a __for-in loop__.

One advantage of __for-in loops__ are since iteration is taken care of by the computer, we don't have to worry about forgetting to increment/decrement our counter variable (*goodbye infinite loops!*).

### Converting a While Loop

Any __while loop__ can be turned into an equivalent __for-in loop__.
Here's an example of printing out elements of a List:

~~~ {.python .numberLines startFrom="1"}
from typing import List

i: int = 0
my_list: List[int] = [1, 2, 3, 4, 5, 6]

while i < len(my_list):
    print(my_list[i])
    i += 1

# can be rewritten as:

for item in my_list:
    print(item)
~~~

The output for both of these loops will be exactly the same: *1, 2, 3, 4, 5, 6*. These two types of loops are completely interchangeable; however, the syntax of a __for-in loop__ often proves to be preferable as you get more comfortable with the process.

### Which Loop to Use?

Although __for-in loops__ and __while loops__ are interchangeable, there are some instances where you want to use one over the other.

__While loops__ provide more control to the author because you must know how many times the loop should run – either by a specific numerical amount using a counter varible, or by telling the loop when to end based on a boolean condition.

__for-in loops__ are fantastic for-in looping through an entire collection of data in a deceptively simple way.

### Nested For Loops!

We can nest __for-in loops__, too!

~~~ {.python .numberLines startFrom="1"}
from typing import List

list_1: List[str] = ["spooky", "scary"]
list_2: List[str] = ["skeletons", "shivers"]

for word in list_1:
    for item in list_2:
        print(word, item)

~~~

The nested loops print out combinations of the two lists. The output of this will be '*spooky skeletons, spooky shivers, scary skeletons, scary shivers*'.


## Range Objects in Loops

You can also loop through a defined range using Python's __range()__ function.

Check out [this page](https://pynative.com/python-range-function/) for more information about this function!

While the syntax looks a bit different for using range within __with loops__ and __for-in loops__, both can use the __range()__ function in their implementation!

~~~ {.python .numberLines startFrom="1"}
i: int = 0
while i in range(5):
    print(i + ", ")
    i += 1

for i in range(5):
    print(i + ", ")
~~~

Both loops' outputs are '*0 1 2 3 4*'. This is another way to control the amount of times a loop repeats!