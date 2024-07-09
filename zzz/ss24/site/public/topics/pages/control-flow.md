---
title: Control Flow
author:
- Aneka Happer
page: resource
template: overview
---

## If Statements

### if-then

Using __booleans__ or boolean expressions, which evaluate to true or false, we can create complex logical programs. If-then statements involve the keyword __if__, parentheses __()__, a __conditional statement__, curly braces __{}__ and some __code__ to execute!

~~~ {.python }
if <conditional statement>:      
   # code to execute
~~~

The conditional statement acts as a gate to the code contained within its curly braces, only allowing the program to access and execute the code in the braces if the expression evaluates to __true__.

The code outside the if-block is completely independent from the conditional and will execute regardless of the conditional statement's truth value.

### if-then-else

Adding the __else__ keyword to an if-statement allows the programmer to provide an additional code block in the case that the conditional statement evaluates to false.

~~~ {.python .numberLines startFrom="1"}
if <conditional statement>:    
    # code to execute
else:
    # code that executes when conditional statement is false
~~~

The code within the else block (surrounded by the curly braces after the __else__ keyword and after the comment) executes only when the conditional is false. 

*IMPORTANT: Only one of the code blocks (that in the if-block or that in the else-block) executes. After it is executed, the loop is exited and we continue with the rest of the code that follows it.* 

There are tons of conditional operators that can be used within if-else blocks!

### nested if-else statements

Within the *then* block (the code to execute when the conditional is true) of an if statement or within an else block we can write as many statements as we want.

We also have just learned that *if-then* and *if-then-else* are themselves statements. This means we can put if-then and if-then-else statements within then blocks or else blocks. That may sound a little confusing, but the key point is that anywhere we have a statement we can use an if or if-then-else statement, so we can __nest__ these! Nesting __if__ statements gives us more control and lets us be more specific with different options for our program. Let's look at an example to clear things up:

~~~ {.python .numberLines startFrom="1"}
person: str = "Stanley"
 
print("What's my favorite food?")
 
if (person == "Kevin"):
    print("chili")
else:
    if (person == "Stanley"):
        print("pretzels")
    else:
        print("cake")
 
# this program will print:
#  What's my favorite food?
#  pretzels

~~~

### elif statements

Since it is common for us to nest if-then and if-then-else statements, we've got a way to make this neater and simpler to use. This is where __elif__ comes in. Instead of opening an else block and inside of that opening another if-block, we can combine these steps. This is how we get an elif block. It does the same as an if block inside of an else block, but it's shorter to write! It also makes the formatting of the code more readable and easier to follow.

Here are the steps to convert from an if nested inside an else block to one elif:

1. Begin by deleting everything from the se: in else: to the start of the nearest if.
2. Then, remove the extra indentation in the so that if/elif/else are all at the same level and their bodies are all one level in.

Here's the example from above, but this time using elif:

~~~ {.python .numberLines startFrom="1" }
person: str = "Stanley"
 
print("What's my favorite food?")
 
if (person == "Kevin"):
    print("chili")
elif (person == "Stanley"):
    print("pretzels")
else:
    print("cake")
 
# this program will print:
#  What's my favorite food?
# pretzels

~~~

Using if-then, if-then-else, and elif statements help us direct the logical flow of a program by increasing our control over which boolean combinations lead to which output. We can make more complex code that does more with fewer lines!

## try-except blocks

__Try/except__ blocks can be used to prevent programs from crashing when an error is encountered. If you expect certain lines of code to potentially raise an error (for example, __ValueError__), put them in a try block. If the error does actually end up occurring, then instead of crashing the program, the code in the except block will run. Since our solution is to simply ignore the error, the ellipsis are sufficient for the except block. If no error is raised when the try block runs, then the except block will be skipped over.

For example, in the code below we except an error because the variable ~~~person~~~ is never defined, so the code in the excpet block would print.

~~~ {.python .numberLines startFrom="1"}
try:
  print(person)
except:
  print("An exception occurred")

~~~




