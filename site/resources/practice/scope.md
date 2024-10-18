---
title: Scope Conceptual Questions
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

For the following, you must prove your answer to each question. Prove using both memory diagrams and verify your diagram with code in VS code.

1. Global variables are limited to the scope of the function they are declared in. (T/F)
2. Variables can have the same name but store different values if they are defined in a different scope. (T/F)
3. An object declared in the Globals frame can be passed into a function and the changes that occur on the object within the function frame will also be seen in the original object. (T/F)
    - 3a. The function copies the object and manipulates the copied object and pastes the chanegs in the original object. (T/F)
    - 3b. For the function to manipulate the object, the object must be passed as one of the parameters. (T/F)
    - 3c. The function does not create a copy of the object rather one of it's parameters holds the reference number to the object. (T/F)
    - 3d. The variable that holds the reference to the object in the function frame, holds the same value as the varibale that instantiated the object in the Globals frame. (T/F)
4. For the following code snippet, create a memory diagram of what is happening. Explain we are able to do line 9: 

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

2. True
Variables in different scopes (such as global and local scope) can have the same name but will store different values within their respective scopes.

3. True
If an object is passed to a function and modified, the changes are reflected globally because Python passes a reference to the object, not a copy. Remember, that we also pass values to the function and that value is the whatever is in your halfbox in memory. This will be a reference (reference number (id number)). Remember, to mutate an object, we pass by reference! 
    - 3a. False; The function does not copy the object. Instead, it directly manipulates the original object via the reference.
    - 3b. True; To manipulate an object, it must be passed as a parameter to the function, allowing the function to access and modify it.
    - 3c. True; The function operates on the original object via the reference held by the parameter.
    - 3d. True; The reference (memory address/id number) held in the function parameter is the same as the reference of the original object, so any changes to the object in the function are reflected globally.

*More solutions to come*
