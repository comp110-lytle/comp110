---
title: Expressions, Statements, and Operators
author:
- Claire Helms
page: resource
template: overview
---

## Statements

### What are statements?

Every __statement__ you write is a separate instruction you're giving the computer.

In Python, statements do not end with any symbols, but in other languages such as Java, statements usually end with a semicolon (;)

In stored programs, you can write statements and, when the program runs, the computer evaluates each statement individually AND in order!

We explain what we want a program to do using statements. For example, statements are used every time we __declare__ or __initialize__ a variable, or when we __assign__ a new value to a variable. We also use statements in other ways, such as when we print things.

### Example

~~~{.python .numberLines startFrom="1"}
person: str  # Variable declaration statement
person = "Michael Scott"  # Variable assignment statement

quote: str = "'I'm not superstitious, but I am a little stitious.'"
# Varibale declaration and assignment in one statement!

print(quote)  # Print statement
print("-- " + person)  # Print statement
~~~

The printed output of this program looks like:

'I'm not superstitious, but I am a little stitious.'

-- Michael Scott


To get a better idea of what's really happening in a statement, let's look at the first print statement from our example: *print(quote)*

In this statement, we tell the computer to __print__ to the screen the string that is stored in the __quote variable__. So, when we run the program the computer will find what's stored in the quote variable *("'I'm not superstitious, but I am a little stitious.'")* and print that out on the screen. The computer is now done with this statement, so it will move on to the next statement, evaluating all statements until the program is complete.


## Expressions

### What are expressions?

__Expressions__ are combinations of variables, literals, operators, or functions that can be evaluated to produce a result. *Expressions simplify to a single value.*

This is the key: expressions evaluate to a typed value at runtime. The evaluation of an expression *only occurs when the program is running* OR when you ask the interactive Python interpreter to evaluate it. You can think of an __expression__ as an intent to do something.

Here is an example:

~~~{.python .numberLines startFrom="1"}
y: int = 4  # This is a STATEMENT because it is an instruction assigning 'y' to 4
x: int = 3  # This is a STATEMENT because it is an instruction assigning 'x' to 3

4 * x  # This is an EXPRESSION because it will evaulate to a single value
y + x  # This is anther EXPRESSION because it will also evaluate to a single value
~~~

In this example, the final two lines are __expressions__ because they evaluate to a single value. These lines also use __operators__, which are covered later on this page.

The types of __expressions__ you can execute with certain objects are dictated by the object's *type*. In the above example, __x__ and __y__ are typed __int__, so you can use mathematical operators __*__ and __+__ to compute a product or sum. Another object type is __boolean__, which we can use to execute a __boolean expression__ (boolean expressions are expressions that return True or False).

For example:

~~~{.python .numberLines startFrom="1"}
cat: bool = True  # STATEMENT assigning 'cat' to True
dog: bool = False  # STATEMENT assigning 'dog' to False

cat and dog  # EXPRESSION evaluating to a single value
cat or dog  # EXPRESSION evaluating to a single value
~~~

In this example, __cat__ is assigned to the boolean True, and __dog__ is assigned to the boolean __false__. The expression *"cat and dog"* evaluates to False, and the expression *"cat or dog"* evaluates to True. For a recap on why these evaluate to False and True respectively, [follow this link](/public/lessons/ls06-logical-operators.html)

Another example of a boolean expression is:

~~~{.python .numberLines startFrom="1"}
x: int = 3  # STATEMENT assigning 'x' to 3
y: int = 4  # STATEMENT assigning 'y' to 4

x > y  # EXPRESSION evaluating to a single value
y == x  # EXPRESSION evaluating to a single value
~~~

Both of these __expressions__ will evaluate to False because the value assigned to __x__ is not greater than the value assigned to __y__, and the value assigned to __y__ does not equal the value assigned to __x__. More on these __operators__ below.

### Function call expressions

Functions are oftentimes thought of as "subprograms" of a larger program and are usually written to carry out a specific task. For a review of functions, [follow this link](/lessons/ls08-functions.html)

A function call, once evaluated, returns a value. 

For example: let's use one of Python's built-in functions, __max()__. The max() function returns the maximum value of one or more items. Here is an example of a function call expression using max():

~~~{.python }
max(4, 5)  # evaluates to 5
~~~

### Method call expressions

Like function calls, when a method of an object is called, a value is often returned. Let's use String's method __upper()__:

~~~{.python .numberLines startFrom="1"}
my_string: str = "I love pizzaaa"  # Remember... this is a statement! (an instruction!)
my_string = my_string.upper()  # This is trickier... it is a statement assigning my_string to an EXPRESSION, which is my_string.upper() ! 
print(my_string)
~~~

In this example, we first assign *my_string* to the string *"I love pizzaaa"*, which is a __statement__ because it is an assignment instruction. Then, we evaluate this string to be completely uppercase with the __upper()__ method. *THE EXPRESSION IS my_string.upper() BECAUSE IT RETURNS A NEW VALUE, WHICH IS THE UPPERCASE VERSION OF OUR STRING!* This is the new value assigned (assignment = statement) to *my_string*, so when we print *my_string*, the output is **"I LOVE PIZZAAA"**.

## Operators

### What are operators? 

__Operators__ are special symbols used to perform __mathematical functions, comparisons__, and __assignments__. They are not expressions nor statements, but they are often used *in* expressions and statements!

### Mathematical operators

Most mathematical operators are exactly the same as they are in math! For example: +, -, / and * for addition, subtraction, division and multiplication.

There are a few operators, though, that are not the same as their math counterparts. For example, to raise a number to a power we use the double asterisk (**).

~~~{.python }
x: int = 3 ** 2
~~~

x evaluates to 9.

Another less familiar operator is the __modulus__ (%). The modulus divides one number by another and tells us the remainder. This is useful for determining if one number is a factor of another, but that is not its only use.

~~~{.python }
x: int = 3 % 2
y: int = 4 % 2
~~~

x evalues to 1 because 2 can go into 3 once, leaving a remainder of 1.
y evaluates to 0 because 2 goes into 4 twice evenly with no remainder.

__Don't forget!__: like in algebra, our trusty order of operations applies... and yes, this means to remember __PEMDAS__! Just a quick reminder that __PEMDAS__ isn't just *Please excuse my dear Aunt Sally*, but it stands for the order in which multi-operator expressions are evaluated. (__P__ = Parentheses, __E__ = Exponents, __M__ = Multiplication, __D__ = Division, __A__ = Addition, and __S__ = Subtraction)

Additionally, any mathematical operator can be combined with an equals symbol = when incrementing a variable. For example:

~~~{.python }
x: int = 3
x += 3
~~~

In this example, x is first assigned the integer value of 3, and then it is incremented by another 3, reassigning the value of 6 to x. You can read "*x += 3*" as "*x is x plus three*."

### Assignment and concatenation operators

For __assigning__ variables, use the = operator. Assigning a variable is considered a statement because it is an instruction to the computer. However, you can *assign* a statement to an expression if what's being assigned is an expression. 

For example: (For __string concatenation__, use the + operator.
)

~~~{.python .numberLines startFrom="1"}
first_name: str = "Creed"  # assignment statement
last_name: str = "Bratton"  # assignment statement
full_name: str = first_name + " " + last_name  # assignment statement AND expression 
~~~

In this example, *full_name* is assigned to the expression *first_name + " " + last_name*.

*full_name* evaluates to 'Creed Bratton'. We use the = operator to assign the variables *first_name, last_name* and *full_name* values, and we use the + operator to concatenate *first_name and last_name*

### Conditional operators

Booleans are either true or false, but we can also have __expressions__ that are true or false. This means we can have whole expressions that are booleans. Boolean expressions use __conditional operators__, which are operators that help compare data. The following two types of operators are conditional operators!

### Relational operators

Many of these symbols come from math and are pretty recognizable:

__>__

This is the 'greater than' operator. Is the number on the left of the '>' larger than the one on the right? If *yes*, the epxression is True. If *no*, the expression is False.

__<__

This is the 'less than' operator. Is the number on the left of the '<' smaller than the one on the right? If *yes*, the epxression is True. If *no*, the expression is False.

__>=__

This is the 'greater than or equal to'/'is at least' operator. (Looks like ≥ in math). Is the number on the left of the '>=' larger or equal to than the one on the right? If *yes*, the epxression is True. If *no*, the expression is False.

__<=__

This is the 'less than or equal to'/'is at most' operator. (Looks like ≤ in math). Is the number on the left of the '<>=' smaller than or equal to the one on the right? If *yes*, the epxression is True. If *no*, the expression is False.


### Equality Operators

Should I use a single = OR a double == ? Remember, the singe = is an __assignment__ operator, which temporarily links a variable to its *assigned* value. SO what is the double == for?

The __==__ is the __equal to__ operator. It has TWO equals symbols in a row. 

The __==__ checks for *deep equality*, or if the objects are the same. An expression with __==__ evaluates to a boolean.

    1066 == 1066 would be True
    21 == 939 would be False

The __!=__ is the __not equal to__ operator. The ! symbol means *"NOT"*. It has an exclamation point followed by a singular equals symbol, and it works oppositely to the __==__ operator.

    1066 != 1066 would be False
    21 != 939 would be True


For more information about expressions, check out [this lesson page!](/lessons/expressions.html)