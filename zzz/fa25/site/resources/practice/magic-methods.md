---
title: Magic Methods Questions
author:
- Benjamin Eldridge
page: lessons
template: overview
---

## Conceptual

1. Consider the following code snippet:

    ```py
        class Point:
            x: float
            y: float

            def __init__(self, x: float, y: float):
                self.x = x
                self.y = y

            def __str__(self) -> str:
                return f"({self.x}, {self.y})"

            def __repr__(self) -> str:
                return f"Point({self.x}, {self.y})"
        
        my_point: Point = Point(1, 2)
        my_str: str = f"My point is {my_point}!"
    ```

    Would the line of code that creates `my_str` also call the `Point` class's `__str__` method?

2. In order to call a magic method, you usually use its name (e.g. `__str__`) directly just like any other method (T/F).

3. The `__add__` method does not modify `self` (T/F).

4. What does a `__str__` method generally return? 

5. For the `Point` class, what would be the type of a `__gt__` method's return value? Is this true for all possible classes that a `__gt__` method could be defined for?

6. For the `Point` class, what would be the type of a `__add__` method's return value? Is this true for all possible classes that a `__add__` method could be defined for?

<details>
<summary>SOLUTIONS</summary>

1. Yes it would! In order to create a `str` object that includes `my_point` like this in the f-string, the `__str__` method of `my_point` is implicitly called.

2. False! It is almost always implicitly called such as in the previous question, or such as when the `__init__` method is called using the class name.

3. True! The `__add__` method creates a new object without modifying its parameters, including `self`.

4. The `__str__` returns a human-readable string that represents the object, usually including its attributes.

5. The type would be `bool`, and this is true for all possible classes that `__gt__` could defined for, since it is called when you make an expression using the comparison operator `>`, so the result must be a `bool`.

6. The type would be `Point`, but this is not true for all classes. The return type of `__add__` for a given class is that class, since `__add__` is used to create a new object of the same class based on the attributes of the two objects on either side of the `+` in the expression.

</details>

## Code Writing

1. Consider the following incomplete class definition along with the previously defined `Point` class:

    ```py
        class Rectangle:
            bottom_left: Point
            bottom_right: Point
            top_left: Point
            top_right: Point

            def __init__(self, bl: Point, br: Point, tl: Point, tr: Point):
                self.bottom_left = bl
                self.bottom_right = br
                self.top_left = tl
                self.top_right = tr

            def area(self) -> int:
                """Returns the area of the rectangle."""
                ...

            def perimeter(self) -> int:
                """Returns the perimeter of the rectangle."""
                ...

            def __gt__(self, other: Rectangle) -> bool:
                """Returns True if self has a larger _____ than other."""
                ...
    ```

    1.1. Fill in the methods for area and perimeter using the four `Point` attributes of the `Rectangle` class.

    1.2. Fill in the `__gt__` method in two ways, first as if the blank in the docstring said "area" and second as if the blank in the docstring said "perimeter". In both, make sure to use the `area` and `perimeter` methods that you defined (the two implementations of `__gt__` should look very similar).

    1.3. (Challenge Question) How could you equivalently write this class definition while using only two attributes? How would your `area`, `perimeter` methods change with only two attributes? Would your `__gt__` method change (in either case, area or perimeter)?

    1.4. (Challenge Question) Write a `__str__` method for `Rectangle` that works like in the following example:

    <pre>
    <div class="terminal">$ python 
    >>> my_rect: Rectangle = Rectangle(Point(0, 0), Point(1, 0), Point(0, 1), Point(1, 1))
    >>> print(my_rect)
    (0, 1) (1, 1)
    (0, 0) (1, 0)
    Area: 1
    Perimeter: 4
    </div>
    </pre>

    Hint: Use `"\n"` to add new lines! Example: 

    <pre>
    <div class="terminal">$ python 
    >>> print("Hello!\nHello again!")
    Hello!
    Hello again!
    </div>
    </pre>

<details>
<summary>SOLUTIONS</summary>

```py
    from __future__ import annotations

    # Included for context, and so you can run it yourself!
    class Point:
        x: float
        y: float

        def __init__(self, x: float, y: float):
            self.x = x
            self.y = y

        def __str__(self) -> str:
            return f"({self.x}, {self.y})"

        def __repr__(self) -> str:
            return f"Point({self.x}, {self.y})"

    class Rectangle:
        bottom_left: Point
        bottom_right: Point
        top_left: Point
        top_right: Point

        def __init__(self, bl: Point, br: Point, tl: Point, tr: Point):
            self.bottom_left = bl
            self.bottom_right = br
            self.top_left = tl
            self.top_right = tr

        # 1.1

        def area(self) -> int:
            """Returns the area of the rectangle."""
            x_length: int = self.bottom_right.x - self.bottom_left.x
            y_length: int = self.top_left.y - self.bottom_left.y
            return x_length * y_length

        def perimeter(self) -> int:
            """Returns the perimeter of the rectangle."""
            x_length: int = self.bottom_right.x - self.bottom_left.x
            y_length: int = self.top_left.y - self.bottom_left.y
            return (x_length * 2) + (y_length * 2)

        # 1.2
        # Note: In a real class definition it would be incorrect to have
        # two methods with the same name like this.

        def __gt__(self, other: Rectangle) -> bool:
            """Returns True if self has a larger area than other."""
            return self.area() > other.area()
        
        def __gt__(self, other: Rectangle) -> bool:
            """Returns True if self has a larger perimeter than other."""
            return self.perimeter() > other.perimeter()

        # 1.4
        
        def __str__(self) -> str:
            return f"{self.top_left} {self.top_right}\n{self.bottom_left} {self.bottom_right}\nArea: {self.area()}\nPerimeter: {self.perimeter()}"
```

For question 1.3, you can represent a rectangle with just two of its opposite corners, since the bottom left's x coordinate should be the same as it's top left x coordinate, and the same with the bottom and top right's x. Similarly, the bottom left's y coordinate should be the same as the bottom right's y coordinate, and the same with the top left and top right's y.

The `area` and `perimeter` methods you wrote previously might be the same, but likely are not since the most intuitive way to measure the x and y length of a rectangle would be on the same side. But by the same reasoning as we used to know where the other two corners are, we can calculate the x and y lengths like how it is shown below.

The implementation of `__gt__` would not change in either case, since `area` and `perimeter` would be the ones that changed but would still work as intended for you to compare the two of them!

```py
    class Rectangle:
        bottom_left: Point
        top_right: Point

        def __init__(self, bl: Point, tr: Point):
            self.bottom_left = bl
            self.top_right = tr

        def area(self) -> int:
            """Returns the area of the rectangle."""
            x_length: int = self.top_right.x - self.bottom_left.x
            y_length: int = self.top_right.y - self.bottom_left.y
            return x_length * y_length

        def perimeter(self) -> int:
            """Returns the perimeter of the rectangle."""
            x_length: int = self.top_right.x - self.bottom_left.x
            y_length: int = self.top_right.y - self.bottom_left.y
            return (x_length * 2) + (y_length * 2)
```

</details>