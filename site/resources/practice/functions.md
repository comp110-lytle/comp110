---
title: Functions Questions
author:
- Alyssa Lytle
- Megan Zhang
- David Karash
page: lessons
template: overview
---

# Questions

## Conceptual

1. What is a function call, and how does it differ from a function definition?
2. What is the difference between parameters and arguments in the context of functions?
3. What is a function signature, and why is it significant?
4. Can the return statement in a function be replaced with a print statement? Why or why not? 
5. Does a function need to have a return statement? Why or why not? 
6. What will follow the arrow in a function signature if the return statement is “return None”? What does this mean?
7. Use the following to write the format of a function signature. You might not need to use all and can use any multiple times:  `def`, (), =, function_name, param_1, param_2, param_n, arg_1, arg_2, arg_n, type_of_value, ->, :
8. Use the following to write the format of a function call. You might not need to use all and can use any multiple times: `def`, (), =, function_name, param_1, param_2, param_n, arg_1, arg_2, arg_n, type_of_value, ->, :
9. When you call a function, once the function is executed, where do you return back to? 
10. When you call a function, is the return value outputted? If yes, explain how? If not, explain how you could print the return value? 
11. If you never encounter a `return` statement in your function, what is your return value? 
12. What is the purpose of the `return` keyword, and what happens if it is omitted in a function?
13. What happens if you call a function before it is defined? Why?
14. How can you pass a function as an argument to another function? How does this work? Provide an example.


[Solutions](#conceptual-solutions)

## Spot the error

1. Looking at the following code, is there something wrong with the code? If yes, what is it and why is it a problem?

```
def fuel_needed(distance, mpg):
   return distance / mpg

def total_fuel_cost(distance, mpg, price_per_gallon):
   fuel_needed(distance, mpg) * price_per_gallon

# Example usage:
print(total_fuel_cost(distance=300, mpg=25, price_per_gallon=4))
```

2. Looking at the following code, is there something wrong with the code? If yes, what is it and why is it a problem?

```
def fuel_needed(distance, mpg):
   return distance / mpg

def total_fuel_cost(distance, mpg, price_per_gallon):
   print(fuel_needed(distance, mpg) * price_per_gallon)

# Example usage:
total_fuel_cost(distance=300, mpg=25, price_per_gallon=4)
```

3. Looking at the following code, is there something wrong with the code? If yes, what is it and why is it a problem?

```
def fuel_needed(distance, mpg):
   return distance / mpg

def total_fuel_cost(distance, mpg, price_per_gallon):
   print(fuel_needed(distance, mpg) * price_per_gallon)

# Example usage:
total_fuel_cost(distance=300, mpg=25, price_per_gallon=4)
```


## Function writing

1. Define a function `greet`. It will take a single parameter, `name`, which is a string. The function will print a greeting message that includes the name of the person you would like to greet, along with additional details about the name. Specifically, it will print a message that states what the first and last letters of the name are. It should then `return` a string expressing happiness to see the person. Refer to the example usage to help construct your function body. Define a `main` function. This will be the entrypoint to your program. Inside the `main` function, call the `greet` function with the argument as specified by the example usage. The `main` function should print the value `return`ed by the `greet` function. Finally, call your `main` function. 

Example usage: 

~~~ {.plaintext}
    $ python -m greet
    Hello Molly, your name starts with a M and ends with a y
    I'm so happy to see you Molly!
~~~

Answer the following questions about your code. Make sure you check your code by looking at the solution before doing this. Diagram your code snippet. 

```
1. On what line(s) is there a *return type* declaration?

2. On what line(s) is there a *signature*?

3. On what line(s) are there *arguments*?

4. On what line(s) are there *parameters* declared?

5. On what line(s) is something *returned*?

6. On what line(s) is something *printed*?

[Solutions](#conceptual-solutions)


# Solutions

## Conceptual Solutions

1. 1 (optional: 5)

2. 1, 5

3. 6 (optional: 8)

4. 1 (optional: 5)

5. 3

6. 2, 6

