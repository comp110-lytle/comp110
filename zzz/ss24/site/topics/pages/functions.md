---
title: Functions
author:
- Aneka Happer
page: resource
template: overview
---

## Function Syntax

Here's the syntax for writing functions:

~~~ {.python }
def <functionName>(<parameter>: <type>, <anotherparameter>: <type> ...) -> <returnType>:
    <function body statements>
    <return statement>
~~~

### Name
Just like all variables, functions have names. We establish a function's name after the __def__ keyword.

### Parameters
Parameters are what the function takes in. They go inside the parentheses ( ) following the function name, and we must give them types. Parameters are local to the function definition, so they can only be used within the function. 

- located within the () of a function definition
- refer to variables that the user passes in when the function is called
- are local to the function definition (can only be used after the : of the function definition)
- function can have multiple parameters seperated by commas
- if there are no parameters the parentheses are left empty 

### Return Type
The return type of a function indicates the type of data the function will return. The function must return a variable or expression that simplifies to the same type as the return type.

- can be __int__, __float__, __bool__, __str__, or __None__
- function must return an object or expression that simplifies to the same type as the return type
- procedures do not contain a return statement

### Function Body
Everything after the colon in the first line (:) makes up the function body. Statements in the body of the function will only be executed when the function is called.

- gives 'functionality' to the function
- code will only be executed when the function is called elsewhere in the code
- if not void, MUST contain a return statement

### Return Statement
The return statement is located inside the function body and indicates when the function call

- type must match the return type of its function
- every function that returns a value must have at least one return statement
- as soon as any return statement is reached the function call is complete, even if within an if-then-else block!

Example function:

~~~ {.python .numberLines startFrom="1"}
def matchMaker(person1: str, person2: str) -> str:

    couple: str = "Congratulations" + person1 + " " + person2

    return couple
~~~

We can see the parts of the function in the following way:

*Parameters*: Person1 and Person2 (both strings)

*Return type*: string

*Function body*: couple: str = "Congratulations" + person1 + " " + person2

*Return statement*: return couple;

Although in the example above, we only have one type in our parameters, you can have multiple

For example, we could modify the matchMaker function in the following way:

~~~ {.python .numberLines startFrom="1"}
def matchMaker(person1: str, person2: str, areCompatible: bool) -> str:

    couple: str = "I'm not sure..."

    if(areCompatible):
        couple = "Congratulations" + person1 + " and " + person2

    return couple
~~~

If we wanted to use the function, we would just call it using the function name followed by ( ) where we would include arguments to match the parameters the function requires.

Arguments are what we pass into parameters. For example, calling matchMaker as it appears in the example above:

~~~ {.python }
result: str = matchMaker("Jim", "Pam", true)

# would return "Congratulations Jim and Pam" which would become result's value
~~~

Arguments don't have to be literals though, we can also (and much more commonly) pass *variables* into functions.

For example using the matchMaker function defined above:

~~~ {.python .numberLines startFrom="1"}
name1: str = "Kevin"
name2: str = "Angela"
loveTest: bool = false

result: str = matchMater(name1, name2, loveTest)

# would return "I don't know..." which would become results value
~~~

A helpful way to think of a function is to compare it to a recipe:

- parameters are the ingredients we need (can't make the recipe without the correct quantity and type of ingredients!)
- the function body is the instructions
- the return type would be whatever we want to make!


## The Main Function

The __main__ function, by convention, is the function that starts your program! It is formatted similarly to any other function definition (see below), and is used to call the other functions in the program! You can think of calling __main__ as being similar to turning your key in the ignition - it is what starts the engine of your program to get things running!

The main function does look a little different than the functions we are used to writing, but don't overthink it - it works essentially the same! We have a function definition and function body just as outlined above, however we are lacking parameters and a return statement. This is ok! When main() is called, the code in the function body executes, and then thats it! The only difference is that no value is returned. 

Below is an example of how the __main__ function can be used:

~~~ {.python .numberLines startFrom="1"}
# function definition 
def main() -> None:
    print("hello, world")

if __name__ == "__main__":
    # function call
    main()

# when main() is called, all of the code within the main function definition will execute
# in this case, "hello, world" will print in the browser!
~~~

## Arguments vs Parameters

Extra pieces of information required by the function definition are called __parameters__. These are like empty variables.

The values provided in the function call are called __arguments__. These are like the variables' values.

Here is an example of how we could call an arbitrary function f.

~~~ {.python .numberLines startFrom="1"}
def f(a: str, b: int, c: bool) -> bool:
    # function implementation would go here!

f("aardvark", 57, false)
~~~

In the example above using function f
- Parameters: a: str, b: int, c: bool
    - located in the function **definition**!
- Arguments: "aardvark", 57, false
    - located in the function **call**!
- "aardvark" matches with a, 57 with b, false with c

Arguments and parameters must line up via type and purpose 1:1...Remember, functions are like recipes that require specific 'ingredients' (aka arguments) in to produce a final result. If you don't give it the correct ingredients (or not enough/too many ingredients) you will get an error!

Examples of an __incorrect__ call of f:

~~~ {.python .numberLines startFrom="1"}
f(false, "aardvark", 57)
# these arguments don't match the order of the parameters!

f(2, 1)
# too few arguments! This function requires three parameters.
~~~

## Calling Functions 

If a function is like a written recipe, a function call is like opening the recipe book to follow the recipe.

- Function calls in Python have parentheses () after the function's name.
- Arguments are the values provided in the function call. They are found within the parentheses.
- Arguments get matched one-to-one with parameters. This means that each argument must be the same type as its corresponding parameter. Read more on the difference between arguments and parameters above.

Here is an example function:

~~~ {.python .numberLines startFrom="1"}
# Function definition:
def myFunc(a: str, b: int) -> int:  
    return b

# Function call:
myFunc("Hola", 1000)
~~~

The parameters are required in the order they are specified, and all parameters must be given an argument. Examples of __incorrect__ calls to myFunc:

~~~ {.python .numberLines startFrom="1"}
myFunc(1000, "Hola") # Incorrect order of arguments
myFunc(2, 1) # Incorrect types of arguments
myFunc(1000) # Too few arguments
myFunc(1, "Hi", "Hola") # Too many arguments
~~~

**Important notes:**
- Function calls are expressions! They evaluate to a single value.
    - Just as (3+1) * 2 simplifies to 8 (PEMDAS), myFunc("Hola", 1000) simplifies to 1000! 
    - Other actions may also be taken in the function body so watch out - but ultimately the original function call can be replaced/simplified to the lone return value.
- Parameters are usually used within the function-- but they aren't required to be. (In the myFunc function, parameter b is used, but parameter a is not. Though this isn't generally useful, it is allowed!)

__Function call tracing example:__

~~~ {.python .numberLines startFrom="1"}
def addOne(n: int) -> int: # (5)     
    return n + 1 # (6)

def main() -> None: # (2)    
    initial: int = 5 # (3)    
    increment: int = addOne(initial) # (4), (7)    
    print(increment) # (8)

main() # (1)
~~~

(1) The call to main starts the program and we jump into the __main__ function. 

(2) The code inside the main function definition begins executing. 

(3) *initial* is declared and assigned the value of 5. 

(4) *increment* is then assigned the value of the function call *addOne(initial)*. This is valid because function calls are also expressions and can evaluate to a single value. However, the return type of the function __must__ match the type of the variable.

(5) We then jump into the *addOne* function. The parameter, *n*, takes the value of the argument passed to the function, *initial*. 

(6) The value of the expression *n + 1* is returned. In this case, it's 6.

(7) The result of the call *addOne(initial)* is stored in *increment*.

(8) The value of *increment* is printed out and the program is done executing!

## Functions with non-None Return Types

In __functions__ that have __non-None__ return types (dont worry, we'll cover "None" later), a value is __returned__ by the function when we call it. We know a function has a non-void return type by looking for a return type in the first line of the function definition or a return statement in the body of the function. Here's an example:

~~~ {.python}
def fun() -> int: # 'int' indicates the return type is number 
    return 110 # this is the return statement
~~~

In our function declaration after the parentheses and the arrow we see the word int, which is the return type. 

Another clue that this is a non-None function is that in the body, the statement return 110; means that this function will return the integer value 110. None functions will not include a return statement.

### Key points about return
- When a function is evaluated, once the computer hits a return statement, execution of the function ends and the specified value is returned. Any code within the function after the return statement will not be evaluated.
- Only __one__ return statement is evaluated during any one function call.
- The return type declared in the first line of the function __must be the same as__ the data type of what is actually being returned from within the body of the function.

Examples of non-void functions and their return statements used __incorrectly__:

~~~ {.python .numberLines startFrom="1"}
# Does not return an integer:
def a() -> int:
    return "Hello!"

# "Hello!" will not be printed
# once a function 'returns,' the function stops executing! 
# no other code in the function body will execute!
def b() -> int:
    return 2
    print("Hello!")

# The second return will never be reached, 
# because 1 was already returned:
def c() -> int:
    return 1
    return 2

# The non-None function does not have a return statement:
def d() -> int
    print(4)
~~~

### How it Works

When we call a function, the computer drops a bookmark there and jumps into the definition of the function it called. It does whatever we tell it in the function body and reaches the return statement. Once the computer hits a *return* it takes the value from the return statement and goes back, or returns, to the place of the bookmark. Here, it substitutes the function call with the value it brought back! Seeing this in action with an example will help it make more sense:

~~~ {.python .numberLines startFrom="1"}
main():
    myFavCourse: str = makeCourse("COMP", 110)
    print("The best course at Carolina is: " + myFavCourse)

def makeCourse(name: str, level: int) -> str:
    course: st = name + level
    return course
 
main();
~~~

We've got a lot going on here! This little program starts out with the import statement and the main function. 

After that, we see the definition for the *makeCourse* function. In this function, we declare the return type to be *str*. Within the function body, we see the statement *return* course. The type of what we're returning (the value stored in *course*) matches the return type we specified since *course* is the result of concatenating *name* and *level* so its type is also string.

*Note: until a function is called (even main()), we only need to acknowledge the function definitions...we dont really care about the function body until a function is called and that code is actually executed!*

When this program runs, the computer sees the definition of the main function first, and then it sees the definition of the *makeCourse* function. 

Next, the computer calls *main()*. This sends it into *main's* function body, which includes a call to the *makeCourse* function using arguments "COMP" and 110. At this function call, the computer drops a bookmark and heads on to the *makeCourse* function. 

There, the computer uses the arguments to make the string for the *course* variable, which it then returns. The computer brings the value of *course*, which is "COMP110", back with it into *main* where the bookmark was left, and drops this value there. So, *myFavCourse* is initialized with "COMP110". The last step in the program is to use this string in the print statement, then we're done!

### Usefulness
Functions that return are great for when we need to go through a lot of steps to get a value that we want to use in our code somewhere. Calling a non-void function tells the computer to head over to the function definition, do everything, and come back with the result once it's done. This is nice if we're doing complicated math or trying to combine a bunch of data in some way. We won't have to worry about all the little steps each time we need the value. Instead, we can tell the computer to go do the hard work for us and come back with the result, which we can then use as we keep going in our program.

## Procedures 

Sometimes a function returns __nothing__, called procedures! Procedures are super helpful when we need to modify variables or objects in our program, especially when we may need to make these same changes over and over again. Procedures allow us to make use of code that may not produce a return value but is still nonetheless pivotal to our program's execution.

Let's take a look at an example:

~~~ {.python .numberLines startFrom="1"}
def repeatPrint(line: str, repeats: int) -> None:
    i: int = 0
    while i < repeats:
        print(line)
        i = i + 1

def main() -> None:  
    repeatPrint("hello ", 2)
    repeatPrint("world ", 3)

main()
~~~

The resulting output to the screen will be:

*hello hello*

*world world world*

If we didn't make use of this procedure, we would've had to rewrite the same print statement 2 or 3 times. This example highlights how void functions reduce redundancy in our code!

Our __main__ function is also a procedure, although unlike other procedure we only call main once.