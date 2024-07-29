---
title: While Loops + Functions Questions
author:
- Alyssa Lytle
- Megan Zhang
- David Karash
page: lessons
template: overview
---

# Questions

## Conceptual

1. Produce a memory diagram for the following code snippet, being sure to include its stack and output.  

```
    def main() -> None:
        """Main Function"""
        y: int = g(1)
        f(y)
        print(g(f(3)))
        
    def f(x: int) -> int:
        """Function 0"""
        if x % 2 == 0:
            print(f"{x} is even")
        else:
            x += 1
        return x
        
    def g(x: int) -> int:
        """Function 1"""
        while x % 2 == 1:
            x += 1
        return x

    main()
```

1.1 Why is it that `main()` is defined above `f()` and `g()`, but we are able to call `f()` and `g()` inside `main()` without errors?

1.2 On line 5, when `print(g(f(3)))` is called, is the code block inside of the `while` loop ever entered? Why or why not?

1.3 What would happen if a line was added to the end of the snipped that said `print(x)`. Why?

[Solutions](#conceptual-solutions)

# Solutions

## Conceptual Solutions

1. <img class="img-fluid" src="/static/practice-mem-diagrams/Qz2-md.png" alt="The memory diagram includes a box on the top labeled Output and a box on the bottom labeled Stack, next to an area labeled Heap.
The first frame in the Stack is labeled Globals and contains the variables main, f, and g. The variable main points to a small box on the heap that says fn 1-5. The variable f points to a small box on the heap that says fn 7-13. The variable g points to a small box on the heap that says fn 15-19.
The next frame on the stack is labeled main and contains a return address and a variable y. The return address is 21 and y has a value of 2. The next frame is labeled g and contains a return address, return value, and a variable x. The return address is 2, the variable x has a value of 2 with the previous value of 1 crossed out, and the return value is 3. The next frame is labeled f and contains a return address, return value, and a variable x. The return address is 4, the variable x has a value of 2, and the return value is 2. The next frame is labeled f and contains a return address, return value, and a variable x. The return address is 5, the variable x has a value of 4 with the previous value of 3 crossed out, and the return value is 4. The final frame is labeled g and contains a return address, return value, and the variable x. The return address is 5, the variable x has a value of 4, and the return value is 4.
The output box contains a line that says (in quotes) 2 is even. Then, on the next line it says (in quotes) 4.
">

1.1 Even though `main` is defined before `f` and `g`, it isn't **called** until after `f` and `g` are defined.

1.2 No because `x = 4`, so `x % 2 == 1` is False, and therefore the code block inside is never run.

1.3 There would be an error because `x` is a local variable inside both `f` and `g`. Therefore, the program does not recognize that `x` exists in this context.