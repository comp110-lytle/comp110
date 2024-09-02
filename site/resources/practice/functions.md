---
title: Functions Questions
author:
- Alyssa Lytle
- Viktorya Hunanyan
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
7. Use the following to write the format of a function signature. You might not need to use all and can use any multiple times:  `def`, `()`, `=`, `function_name`, `param_1`, `param_2`, `param_n`, `arg_1`, `arg_2`, `arg_n`, `type_of_value`, `->`, `:`
8. Use the following to write the format of a function call. You might not need to use all and can use any multiple times:  `def`, `()`, `=`, `function_name`, `param_1`, `param_2`, `param_n`, `arg_1`, `arg_2`, `arg_n`, `type_of_value`, `->`, `:`
9. When you call a function, once the function is executed, where do you return back to? 
10. When you call a function, is the return value outputted? If yes, explain how? If not, explain how you could print the return value? 
11. If you never encounter a `return` statement in your function, what is your return value? 
12. What is the purpose of the `return` keyword, and what happens if it is omitted in a function?
13. What happens if you call a function before it is defined? Why?
14. How can you pass a function as an argument to another function? How does this work? Provide an example.


[Solutions](#conceptual-solutions)


## Calling functions

1. For the following code snippet, write a line of code that will result in the following output: 

```python
def flavor(taste: str, percent: float) -> None:
    print("This flavor is " + str(percent) + "% " + taste)
```

Output: 

~~~ {.plaintext}
    $ python -m flavor
    This flavor is 100% umami
~~~


2. For the following code snippet, write a line of code that will call the `main` function. Next, write a line of code to be inserted within the body of the `main` function. This line should call the `eat` function with the argument passed when the main function was called. 

```python
def eat(food: str) -> None:
    print("Eating " + food)

def main(food: str) -> None:
    food_item = "apple"
    eat(food=food)

```


3. For the following code snippet, write a line of code that will call the `have_done` function with the arguments `"homework"` and `False`. If you wanted to print the string created by the `have_done` function, how would you modify your function call? 

```python
def have_done(task, completed) -> str:
    return "Completed " + task + ": " + str(completed)
```

[Solutions](#calling-functions-solutions)


## Spot the error


1. Looking at the following code, is there something wrong with the code that stops the execution of the entire code? If yes, what is it and why is it a problem?

```python
def fuel_needed(distance: float, mpg: float) -> float:
    return distance / mpg

def total_fuel_cost(distance: float, mpg: float, price_per_gallon: float) -> float:
    fuel_needed(distance=distance, mpg=mpg) * price_per_gallon

# Example usage:
print(total_fuel_cost(distance=300, mpg=25, price_per_gallon=4))
```


2. Looking at the following code, is there something wrong with the code that stops the execution of the entire code? If yes, what is it and why is it a problem?


```python
def fuel_needed(distance: float, mpg: float) -> float:
    return distance / mpg

def total_fuel_cost(distance: float, mpg: float, price_per_gallon: float) -> None:
    print(fuel_needed(distance=distance, mpg=mpg) * price_per_gallon)

# Example usage:
total_fuel_cost(distance=300, mpg=25, price_per_gallon=4)

```

3. Looking at the following code, is there something wrong with the code that stops the execution of the entire code? If yes, what is it and why is it a problem?

```python
def greet(name: str) -> str:
    print("Hello " + name + ", your name starts with an " + name[0] + " and ends with an " + name[len(name) - 1])
    return "I'm so happy to see you " + name + "!"

def main() -> None:
    print(greet(name="Molly"))

# Example usage: 
main()

```

4. Looking at the following code, is there something wrong with the code that stops the execution of the entire code? If yes, what is it and why is it a problem?

```python
def greet(name: str) -> str:
    return "I'm so happy to see you " + name + "!"
    print("Hello " + name + ", your name starts with an " + str(name[0]) + " and ends with an " + str(name[len(name) - 1]))

def main() -> None:
    print(greet(name="Molly"))

# Example usage: 
main()
```


5. Looking at the following code, is there something wrong with the code that stops the execution of the entire code? If yes, what is it and why is it a problem?

```python
def greet(name: str) -> str:
    return "I'm so happy to see you " + name + "!"
    print("Hello " + name + ", your name starts with an " + str(name[0]) + " and ends with an " + str(name[len(name) - 1]))

def main() -> None:
    print(greet(name="Molly"))

# Example usage: 
main()

```

6. Looking at the following code, is there something wrong with the code that stops the execution of the entire code? If yes, what is it and why is it a problem?

```python
def greet(name: str) -> str:
    print("I'm so happy to see you " + name + "!")
    print("Hello " + name + ", your name starts with an " + str(name[0]) + " and ends with an " + str(name[len(name) - 1]))

def main() -> None:
    print(greet(name="Molly"))

# Example usage: 
main()

```

[Solutions](#spot-the-error-solutions)


# Solutions 

## Conceptual

1. A function definition is where you create the function and specify what it does. It includes the function signature and everything indented below it. The signature consists of the function name, parameters, the types of the parameters, and the return type. The function body contains the code block that executes when the function is called. A function call occurs when you invoke or execute the function by writing the function name followed by parentheses. If the function accepts inputs, the parentheses will contain the values assigned to the parameters, also known as arguments. When a function definition is encountered, the function body is not executed; it is bypassed until the function is called. To call a function, you must first define it.

2. Parameters are the variables listed in the function signature that define the expected inputs. Your parameters will hold the values passed into the function when the function is called. These values that are assigned to the parameters are called arguments. Arguments are the actual values passed to the function when it is called.

3. A function signature refers to the first line of a function definition, where the `def` keyword is used. Following the `def` keyword is the function name, and after the function name is a set of parentheses that enclose the parameter list. After the parameter list comes the return type. The function signature is important because it defines how the function can be called and what kinds of inputs and outputs are expected. Without a signature, you wouldn't know what parameters to provide or even how to call the function, since the function name would be missing.

4. No, the `return` statement cannot be replaced with a `print` statement. The return statement ends the function execution and passes a value back to the caller. The `print` statement merely outputs a value to the console without returning anything to the function caller.

5. No, a function does not need to have a return statement. If no return is present, the function will return None by default after completing its execution. However, using return is necessary when you need to send a value back to the caller.

6. The arrow (`->`) in a function signature will be followed by `None`. This indicates that the function does not return any meaningful value (ex. `int`, `float`, `bool`, etc.) and will return `None`. 

7. 

```python
def function_name(param_1: type_of_value, param_2: type_of_value, param_n: type_of_value) -> type_of_value:

```

8. 

```python
function_name(param_1=arg_1, param_2=arg_2, param_n=arg_n)
```

9. After the function is executed, you will return back to the point in the code where the function was called.

10. No, the return value is not automatically outputted. To see the return value, you need to use a print statement to output it. Your argument within the print function is going to be the call to your function that you would like to receive the return value from. 

11. If there is no `return` statement in a function, it returns `None` by default. 

12. The return keyword ends the function execution and specifies the value to be returned to the caller. If omitted, the function will return `None` after execution.

13. If you call a function before it is defined, you will get an error. Python reads from top to bottom and so if the function is not defined and memorized in memory, when python encounters the function at a function call, it will not know what the function_name is referring to. The function must be defined before it can be called as Python needs to know that the function is defined before executing trying to call it.

14. To pass a function's return value as an argument to another function, you need to call the first function, which will execute it and produce a return value. That return value can then be passed as an argument to the second function.

This works because when you call the first function, it returns a value, and that value is then used as input (an argument) for the second function.

Example: 

```python
def double(x: int) -> int:
    return x * 2

def add_five(y: int) -> int:
    return y + 5

print(add_five(y=double(x=3)))

```


## Calling functions

1. **For the `flavor` function:**

   To call the `flavor` function using keyword arguments:

   ```python
   flavor(taste="umami", percent=100.0)
   ```

2. **For calling the `main` function and modifying its body with keyword arguments:**

   To call the `main` function with a keyword argument:

   ```python
   main(food="apple")
   ```

   In the `main` function, to call the `eat` function with keyword arguments:

   ```python
   def main(food: str) -> None:
       food_item = "apple"
       eat(food=food)
   ```

3. **For calling `have_done` and printing the result with keyword arguments:**

   To call `have_done` with keyword arguments:

   ```python
   have_done(task="homework", completed=False)
   ```

   To print the result of this function call:

   ```python
   print(have_done(task="homework", completed=False))
   ```


## Spot the error

1. **Code Snippet 1:**

   **Problem:** The `total_fuel_cost` function does not return a value. It performs a calculation but does not include a `return` statement. As a result, it returns `None` by default, which leads to `print(total_fuel_cost(...))` printing `None` which is not the intended use of line 8. 

   **Solution:** Add a `return` statement in the `total_fuel_cost` function:

2. **Code Snippet 2:**

   **Problem:** There is no issue with this code that stops execution. The `total_fuel_cost` function correctly prints the result. 

   **Solution:** None needed; the code works as intended.

3. **Code Snippet 4:**

   **Problem:** There is no issue with this code that stops execution. The `greet` function prints a message and then returns a string. The `main` function calls `greet` and prints its return value.

   **Solution:** None needed; the code works as intended.

4. **Code Snippet 5:**

   **Problem:** The `print` statement after the `return` statement in the `greet` function is unreachable code. Once the `return` statement is executed, the function exits, and any code following it will not be executed. 

   **Solution:** Move the `print` statement before the `return` statement:

5. **Code Snippet 6:**

   **Problem:** There is a syntax error due to incorrect indentation. The `greet` function definition is not properly aligned.

   **Solution:** Correct the indentation of the `greet` function definition:

6. **Code Snippet 7:**

   **Problem:** There is no issue with this code that stops execution. The `greet` function prints two messages, and then `main` calls `greet` and prints its return value (which is `None`).

   **Solution:** None needed; the code works as intended.
