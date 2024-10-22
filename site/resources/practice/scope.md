---
title: Scope Conceptual Questions
author:
- Viktorya Hunanyan
- Alyssa Lytle
- Megan Zhang
- David Karash
page: lessons
template: overview
---

# Questions

## Conceptual

For the following, you must prove your answer to each question. Prove using both memory diagrams and verify your diagram with code in VS code.

1. Global variables are limited to the scope of the function they are declared in. (T/F)
2. Variables can have the same name but store different values if they are defined in a different scope. (T/F)
3. An object declared in the Globals frame can be passed into a function and the changes that occur on the object within the function frame will also be seen in the original object. (T/F)
    - 3a. The function copies the object and manipulates the copied object and pastes the chanegs in the original object. (T/F)
    - 3b. For the function to manipulate the object, the object must be passed as one of the parameters. (T/F)
    - 3c. The function does not create a copy of the object rather one of it's parameters holds the reference number to the object. (T/F)
    - 3d. The variable that holds the reference to the object in the function frame, holds the same value as the varibale that instantiated the object in the Globals frame. (T/F)
4. For the following code snippet, create a memory diagram of what is happening. Explain why we are able to do line 9: 

```python
xs = "01"
ys = "23"

def get_coords() -> None:
    x_idx: int = 0
    while x_idx < len(xs):
        y_idx: int = 0
        while y_idx < len(ys):
            print(f"({xs[x_idx]},{ys[y_idx]})")
            y_idx += 1
        x_idx += 1

 if __name__ == "__main__":
    get_coords()
```
5. Give an example of a Global variable being referenced inside of a local frame (this varible should not reference an object). Explain what is happening in your example and how scope is in use. 
6. Give an example of when a Global variable and a local variable have the same name but in different local frames, one is used over the other. 

[Solutions](#conceptual-solutions)

# Solutions

## Conceptual Solutions

1. False
Global variables are not limited to the function scope; they are accessible throughout the entire program unless shadowed by a local variable of the same name within a function. 

Example: 

```
    x = 10  # Global variable

    def func():
        print(x)  # Accesses the global variable

    func()  # Output: 10
```

Furthermore, when a `function_1` is called inside of the body of another function, `function_2`, `function_1` is accesible because it is global. Python will first check in `function_1`'s frame to see if `function_2` is defined and if it is not then it will move up to the last frame that does not have an RV. Once it does this, it will check again if function_2 is defined and if it is not, it will continue doing this until it has found `function_2` defined in a frame. It will eventially get to the globals frame where it will see function_2 is defined and holds a referene number that is defining what function_2 is. At this point, Python will understand that `function_1` is a function and return to the line where it was encountered in `function_2`'s body, now recognizing `function_1` as callable and executing it accordingly.

---

2. True
Variables in different scopes (such as global and local scope) can have the same name but will store different values within their respective scopes.

Example: 

```
    x = 10  # Global variable

    def func():
        x = 20  # Local variable with the same name
        print(x)  # Output: 20 (Local scope)

    func()
    print(x)  # Output: 10 (Global scope)
```

For more examples, please refer to the memory diagram page. 

---

3. True
If an object is passed to a function and modified, the changes are reflected globally because Python passes a reference to the object, not a copy. Remember, that we also pass values to the function and that value is the whatever is in your halfbox in memory. This will be a reference (reference number (id number)). Remember, to mutate an object, we pass by reference! 

Example: 

```
lst = [1, 2, 3]  # Global object (mutable)

def modify_list(some_list):
    some_list.append(4)

modify_list(lst)
print(lst)  # Output: [1, 2, 3, 4]
```

For more examples, please refer to the memory diagram page. 

3a. False; The function does not copy the object. Instead, it directly manipulates the original object via the reference.

3b. True; To manipulate an object, it must be passed as a parameter to the function, allowing the function to access and modify it.

3c. True; The function operates on the original object via the reference held by the parameter.

3d. True; The reference (memory address/id number) held in the function parameter is the same as the reference of the original object, so any changes to the object in the function are reflected globally.

---

4. On line 9, `xs[x_idx]` and `ys[y_idx]` access characters from the strings `xs` and `ys` using indexing.
A memory diagram would show the `Globals` frame holding `xs` and `ys` as string objects. The `x_idx` and `y_idx` variables exist within the local frame of `get_coords`, indexing into `xs` and `ys`. The print statement outputs pairs of characters from xs and ys, i.e., `(0,2), (0,3), (1,2), (1,3)`.

The ability to perform this operation comes from the fact that `xs` and `ys` are global variables, so they are accessible inside get_coords().

---

5. Example below: 

```
    x = 42  # Global variable

    def print_global():
        print(x)  # References the global variable

    print_global()  # Output: 42
```
- x is declared in the global scope.
- Inside the function print_global(), the global variable x is accessed and printed. Exactly the same explanation as number 1 except here, python is looking for the `x` variable. 
- The function does not have its own x, so it refers to the global one.

---

6. Example below: 

```
    x = 5  # Global variable

    def local_scope():
        x = 10  # Local variable with the same name
        print(x)  # Output: 10 (Local variable is used)

    local_scope()
    print(x)  # Output: 5 (Global variable remains unchanged)
```

As you seen in the body of the function, when we `print(x)`, `10` is output. This is because of the process described in question 1; python will look in the area it is currently in before moving to another space (just like real life, if you lose your airpods while sitting on the couch, you aren't going to start looking for you airpods in your kitchen, you start in the place where you are at and then expand outwards to the places that make sense.)