---
title: Quiz 03 General Practice
author:
- Alyssa Lytle
- David Karash
- Megan Zhang
- Viktorya Hunanyan
- Benjamin Eldridge
- Izzi Hinks
page: lessons
template: overview
---

# Object-Oriented Programming (OOP)

## Multiple Choice

1. True or False: A class definition provides a pattern for creating objects, but doesn’t make any objects itself.

    a. True
    
    b. False

2. True or False: All instances of a class have the same attribute values.

    a. True
    
    b. False

3. True or False: An object's attribute values cannot be accessed from outside the class.

    a. True
    
    b. False

4. What is the difference between a class and an object?

    a. A class is a collection of objects
    
    b. A class is a blueprint; an object is a specific instance of that blueprint

    c. They are the same in Python

    d. An object can contain classes, but not the other way around

5. True or False: Because class definitions have attributes, local variables are not allowed inside method definitions.

    a. True
    
    b. False

6. What does it mean to "instantiate" a class?

    a. Define the class
    
    b. Import a module

    c. Create an object from a class

    d. Define attributes

7. True or False: The constructor of a class is only called once in a program, no matter how many objects of that class are constructed.

    a. True
    
    b. False

8. The first parameter of any method is _____ and it is given a reference to the object the method was called on.

    a. me
    
    b. self

    c. init

    d. this

    e. current

9. An instance of a class is stored in the: 

    a. stack

    b. heap

    c. output

10. True or False: Once attributes are initialized in the initializer/constructor, the values cannot be changed.

    a. True
    
    b. False

11. True or False: A class definition introduces a new data type, or type of object, in your program.

    a. True
    
    b. False

<details>
<summary>SOLUTIONS</summary>

1. True

2. False

2. False

3. A class is a blueprint; an object is a specific instance of that blueprint

4. False

5. Create an object from a class

6. False

7. self

8. heap

9. False

10. True

</details>

## Select All That Apply

Consider the following code listing. Select all lines on which any of the concepts below are found. Select \code{N/A} if the concept is not in the code listing.

```py
    class Point:
        x: float
        y: float
 
        def __init__(self, x: float, y: float):
            self.x = x
            self.y = y
 
        def flip(self) -> None:
            temp: float = self.x
            self.x = self.y
            self.y = temp

        def shift_y(self, dy: float) -> None:
            self.y += dy

        def diff(self) -> float:
            return self.x - self.y
```


1. Constructor Declaration

    a. 1

    b. 2

    c. 5

    d. 9

    e. 11

2. Attribute Declaration

    a. 2

    b. 3

    c. 6

    d. 7

    e. 10

3. Attribute Initialization

    a. 2

    b. 3

    c. 6

    d. 7

    e. 10

4. Method Declaration

    a. 1

    b. 9

    c. 10

    d. 14

    e. 17

5. Local Variable Declaration

    a. 2

    b. 3

    c. 6

    d. 7

    e. 10

6. Instantiation

    a. 1

    b. 5

    c. 9

    d. 10

    e. N/A

<details>
<summary>SOLUTIONS</summary>

1. Line 5 only

2. Lines 2 and 3

3. Lines 6 and 7

4. Lines 9, 14, and 17

5. Line 10

6. N/A

</details>

## Short Answer

1. What does `self` refer to in Python classes?
 
2. Similar to how a function is first *defined* then *called*, a class is first *defined* then ____.

3. When a method is called, do you have to pass an argument to the `self` parameter?

4. When is `self` used outside of a class definition?

5. Use the following point class to answer the questions.

    ```py
        class Point:
            x: float
            y: float
    
            def __init__(self, x: float, y: float):
                self.x = x
                self.y = y
    
            def flip(self) -> None:
                temp: float = self.x
                self.x = self.y
                self.y = temp
    
            def shift_y(self, dy: float) -> None:
                self.y += dy
    
            def diff(self) -> float:
                return self.x - self.y
    ```

    5.1. Write a line of code to create an explicitly typed instance of the Point class called my_point with an x of 3.7 and y of 2.3. 

    5.2. Write a line of code to change the value of the my_point variable's x attribute to 2.0. 

    5.3. Write a line of code to cause the my_point variable's y attribute to increase by 1.0 using a method call.

    5.4. Write a line of code to declare an explicitly typed variable named x. Initialize x to the result of calling the diff method on my_point.


<details>
<summary>SOLUTIONS</summary>

1. `self` refers to the current instance of the class that the methods will operate on if those methods are called in the future on an instance of that class.

2. Instantiated

3. No! When you call the constructor for a class, `self` is automatically made by python in order for the rest of the constructor to finish making the object. In the case of other methods, python knows that `self` is the object that you called the method on, often the variable name that comes before the method call (e.g. for `my_point.shift_y(1.0)`, `self` is `my_point`).

4. `self` is not used outside of a class definition. Outside of a class definition you use the name of the variable storing an object to refer to it.

5.1. `my_point: Point = Point(x=3.7, y=2.3)`

5.2. `my_point.x = 2.0`

5.3. `my_point.shift_y(1.0)`

5.4. `x: float = my_point.diff()`

</details>


## Function + Method-Writing With Instances of a Class

### `Course`

1. Write a function (NOT A METHOD) called `find_courses`. Given the following `Course` class definition, `find_courses` should take in a `list[Course]` and a `str` prerequisite to search for. The function should return a list of the `names` of each Course whose `level` is 400+ and whose `prerequisites` list contains the given string.

``` 
    class Course:
        """Models the idea of a UNC course."""
        name: str
        level: int
        prerequisites: list[str]
```

2. Write a method called `is_valid_course` for the `Course` class. The method should take in a `str` prerequisite and return a `bool` that represents whether the course’s `level` is 400+ and if its `prerequisites` list contains the given string.

## Class-Writing

<!-- ### `ChristmasTreeFarm`

This class is slightly challenging, but take it step by step! Create a `ChristmasTreeFarm` class with the following specifications:

a. The `ChristmasTreeFarm` class should have one attribute: a `list[int]` named `plots`. 
    * Basic behavior of `plots` (you will define this later):
    * This list will hold values that represent the size of the tree planted in each plot. 
    * If the value at an index of the list is 0, then the plot at that index is empty (does not have a tree). 
    * Any value other than 0 indicates that a tree is growing in that plot!
    b. The *constructor* for the class should take two arguments: `plots: int` and `initial_planting: int`, both of type int. 
        * The first parameter, `plots`, represents the *total* number of plots in the farm. (Notice that the attribute `plots` and the parameter `plots` for this constructor are different, and represent different things!) 
        * The second parameter, `initial_planting`, represents the number of plots that that will have trees already planted in them. These initially planted plots will be trees of size 1.
        * The constructor should initialize the `plots` *attribute* to an empty `list`, and then append `initial_planting` trees of size 1. After that, the constructor should fill the rest of the plots with zeroes to indicate that they are empty!
    c. The class should define a method called `plant`.
        * This method should have a parameter of type `int`, representing the  plot index at which a tree should be planted. 
        * The tree should be size 1 when planted. If this method is called on a plot that already has a tree, the old tree will be uprooted and replaced with a new baby tree (size 1).
    d. The class should define a method called `growth`. 
        * This method should increase the size of each planted tree by 1. (Remember that unplanted plots are represented by a 0 in the `plots` list.)
    e. The class should define a method called `harvest`. 
        * This method should have a parameter `replant` of type `bool` that will determine whether this method replants trees (sets them to size 1 after harvest) or leaves the plots empty (sets them to size 0 after harvest). 
        * For this method, trees that are at least size 5 will be harvested. The method will `return` the count of how many trees were successfully harvested (type `int`).
    f. The class should *overload* the addition operator. 
        * This method should work between two objects of type `ChristmasTreeFarm`. 
        * The method should return a new `ChristmasTreeFarm` object whose size is the sum of the given `ChristmasTreeFarm`'s, and whose initial plantings are the sum of the number of planted trees in the given `ChristmasTreeFarm`s.
     --> 


### `Car`

Write a Python class called `Car` that represents a basic model of a car with the following specifications:

* Include attributes `make: str`, `model: str`, `year: int`, `color: str`, and `mileage: float`.  
* Write a constructor to initialize all attributes.
* Implement a method for updating the mileage of the car, `update_mileage`, that takes an amount of `miles: float` as input and updated the mileage attribute. 
* Implement a method displaying the car's attribute information as a string called `display_info`. It should just print the information and not return anything. (You can take creative liberty, as long as it prints out all attributes!)
* Implement a *function* (NOT a method) called `calculate_depreciation` that calculates the depreciation of the car  by taking a `Car` object as input and `depreciation_rate: float` and returns the mileage multiplied by the depreciation rate. 

Practice calling these methods by instantiating a new car object and calling them! 

## Class Writing + Magic Methods

### `HotCocoa`

Create a class called `HotCocoa` with the following specifications:

a. Each `HotCocoa` object has a `bool` attribute called `has_whip`, a `str` attribute called `flavor`, and two `int` attributes called `marshmallow_count` and `sweetness`.

b. The class should have a constructor that takes in and sets up each of its attribute’s values.

c. Write a method called `mallow_adder` that takes in an `int` called `mallows`, increases the `marshmallow_count` by that amount, and increases the `sweetness` by that amount times 2.

d. Write a `__str__` magic method that displays (aka returns a string with) the details of the hot cocoa order mimicing the following: 
    - If it has whipped cream:
        `"A <flavor> cocoa with whip, <marshmallow_count> marshmallows, and level <sweetness> sweetness.`
    - If it doesn't have whipped cream:
        `"A <flavor> cocoa without whip, <marshmallow_count> marshmallows, and level <sweetness> sweetness.`

e. Write an `order_cost` *function* that takes as input a `list` of `HotCocoa` objects to represent an order and returns the total cost of the order. A `HotCocoa` with whip is $2.50 and without whip is $2.00.

#### Instantiation Practice

- Create an instance of `HotCocoa` called `my_order` with no whip, `"vanilla"` flavor, 5 marshmallows, and sweetness level 2.

- Add whipped cream. (Change `has_whip` to `True`.)

- Add 2 marshmallows using `mallow_adder`.

- Create another `HotCocoa` instance called `viktoryas_order` with whip, `"peppermint"` flavor, 10 marshmallows, and sweetness level 2.

- Calculate the cost of `[my_order, viktoryas_order]` by calling `order_cost`.

- Print out the details of the `HotCocoa` instance `my_order`.

### `TimeSpent`

Create a class called `TimeSpent` with the following specifications:

a. Each `TimeSpent` object has a `str` attribute called `name`, a `str` attribute called `purpose`, and an `int` attribute called `minutes`.

b. The class should have a constructor that takes in and sets up each of its attribute’s values.

c. Write a method called `add_time` that takes in an `int` and increases the `minutes` attribute by this amount. The method should return `None`.

d. Write an `__add__` magic method that takes in an `int` called `added_minutes` and returns a new `TimeSpent` object with the same attribute values except that `minutes` is increased by `added_minutes`.

e. Write a method called `reset` that resets the amount of time that is stored in the `minutes` attribute.  The method should also return the amount that was stored in `minutes`. 

f. Write a `__str__` magic method returns a line reporting information about the current `TimeSpent` object.  Suppose a `TimeSpent` object has `name` = `“Ariana”`, `purpose` = `“screen time”`, and `minutes` = `130`.  The method should return: `“Ariana has spent 2 hours and 10 minutes on screen time.”`

g. Write a *function* called `most_by_purpose` that takes as input a `list` of `TimeSpent` objects and a `str` to represent a purpose, and returns the name of the person who spent the most time doing that specific activity. 
    - Example usage: 
    <pre>
    <div class="terminal">
    >>> a: TimeSpent = TimeSpent("Alyssa", "studying", 5)
    >>> b: TimeSpent = TimeSpent("Alyssa", "doom scrolling", 100)
    >>> c: TimeSpent = TimeSpent("Vrinda", "studying", 200)
    >>> most_by_purpose([a, b, c], "studying")
    'Vrinda'
    </div>
    </pre>


## Solutions

### Function + Method Writing With Class Objects

#### `Course` Solution

1.
```
    def find_courses(courses: list[Course], prereq: str) -> list[str]:
        """Finds 400+ level courses with the given prereq."""
        results: list[str] = []

        for c in courses:
            if c.level >= 400:
                for p in c.prerequisites:
                    if p == prereq:
                        results.append(c.name)
        
        return results
```


2.
```
    def is_valid_course(self, prereq: str) -> bool:
        """Checks if this course is 400+ level and has the given prereq."""
        if self.level < 400:
            return False
        else: 
            for p in self.prerequisites:
                if p == prereq:
                    return True
            return False
```

### Class-Writing


<!-- ### `ChristmasTreeFarm` solution

```
    """Diagraming practice for Quiz 03."""

    class ChristmasTreeFarm:
        """A christmas tree farm!"""

        plots: list[int]

        def __init__(self, plots: int, initial_planting: int) -> None:
            """Sets up the farm."""
            self.plots = []
            i: int = 0
            while i< initial_planting:
                self.plots.append(1)
                i += 1
            while i < plots:
                self.plots.append(0)
                i += 1
        
        def plant(self, plot_number: int) -> None:
            """Plants a tree at the given plot number."""
            self.plots[plot_number] = 1
        
        def growth(self) -> None:
            """Grows each planted tree."""
            i: int = 0
            while i < len(self.plots):
                if self.plots[i] != 0:
                    self.plots[i] += 1
                i += 1

        def harvest(self, replant: bool) -> int:
            """Harvest trees that are fully grown!"""
            total: int = 0
            i: int = 0
            while i < len(self.plots):
                if self.plots[i] >= 5:
                    total += 1
                    if replant:
                        self.plots[i] = 1
                    else: 
                        self.plots[i] = 0
                i += 1
            return total

``` -->

#### `Car` solution

```
    class Car:
        
        make: str
        model: str
        year: int
        color: str
        mileage: float
        
        def __init__(self, make: str, model: str, year: int, color: str, mileage: float):
            self.make = make
            self.model = model
            self.year = year
            self.color = color
            self.mileage = mileage
        
        def update_mileage(self, miles: float) -> None:
            self.mileage += miles
            
        def display_info(self) -> None:
            info: str = f"This car is a {self.color}, {self. year} {self.make} {self.model} with {self.mileage} miles."
            print(info)
        
    def calculate_depreciation(vehicle: Car, depreciation_rate: float) -> float:
        return vehicle.mileage * depreciation_rate

```

to practice instantiating: 

```
    my_ride: Car = Car("Honda", "CRV", "2015", "blue", 75000.00)
    my_ride.update_mileage(5000.25)
    my_ride.display_info()
    calculate_depreciation(my_ride, .01)
```


#### `HotCocoa` solution

```
    class HotCocoa:
        
        has_whip: bool
        flavor: str
        marshmallow_count: int
        sweetness: int
        
        def __init__(self, whip: bool, flavor: str, marshmallows: int, sweetness: int):
            self.has_whip = whip
            self.flavor = flavor
            self.marshmallow_count = marshmallows
            self.sweetness = sweetness
        
        def mallow_adder(self, mallows: int) -> None:
            self.marshmallow_count += mallows
            self.sweetness += (mallows * 2)
            
        def __str__(self) -> str:
            if self.has_whip:
                return f"A {self.flavor} cocoa with whip, {self.marshmallow_count} marshmallows, and level {self.sweetness} sweetness."
            else:
                return f"A {self.flavor} cocoa without whip, {self.marshmallow_count} marshmallows, and level {self.sweetness} sweetness."
            
    def order_cost(order: list[HotCocoa]) -> float:
        cost: float = 0.0
        for cocoa in order:
            if cocoa.has_whip:
                cost += 2.50
            else:
                cost += 2.00
        return cost
```

##### Instantiation

```
    my_order: HotCocoa = HotCocoa(False, "vanilla", 5, 2)

    # Add whipped cream. (Change has_whip to True.)
    my_order.has_whip = True

    # Add 2 marshmallows using mallow_adder.
    my_order.mallow_adder(2)

    # Create viktoryas_order with whip, "peppermint" flavor, 10 marshmallows, and sweetness level 2.
    viktoryas_order: HotCocoa = HotCocoa(True, "peppermint", 10, 2)

    # Calculate the cost of [my_order, viktoryas_order] by calling order_cost.
    order_cost([my_order, viktoryas_order])

    # Print out the details of my_order.
    print(my_order) # or print(str(my_order))
```

#### `TimeSpent` solution

```
    class TimeSpent:
        
        name: str
        purpose: str
        minutes: int
        
        def __init__(self, name: str, purpose: str, minutes: int):
            self.name = name
            self.purpose = purpose
            self.minutes = minutes

        def add_time(self, increase: int) -> None:
            self.minutes += increase
        
        def __add__(self, added_minutes: int) -> TimeSpent:
            return TimeSpent(self.name, self.purpose, self.minutes + added_minutes)
        
        def reset(self) -> None:
            old_value: int = self.minutes
            self.minutes = 0
            return old_value
        
        def __str__(self) -> str:
            minutes: int = self.time % 60
            hours: int = (self.time - minutes)/ 60
            return f"{self.name} has spent {hours} hours and {minutes} minutes on screen time."

    def most_by_purpose(times: list[TimeSpent], activity: str) -> str:
        max_time: int = 0
        max_name: str = ""
        for elem in times:
            if (elem.purpose == activity) and (elem.minutes > max_time):
                max_time = elem.minutes
                max_name = elem.name
        return max_name
```

## Magic Methods

### Conceptual

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

### Code-Writing

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

# Recursive Structures


Any questions that reference the `Node` class are referring to a class defined in the following way:

```py
    from __future__ import annotations

    class Node:
        value: int
        next: Node | None

        def __init__(self, val: int, next: Node | None):
            self.value = val
            self.next = next

        def __str__(self) -> str:
            rest: str
            if self.next is None:
                rest = "None"
            else:
                rest = str(self.next)
            return f"{self.value} -> {rest}"
```

## Multiple Choice

1. (Select all that apply) Which of the following properties of a recursive function will ensure that it *does not* have an infinite loop?

    a. The function calls itself in the recursive case.

    b. The recursive case progresses towards the base case.

    c. The base case returns a result directly (it does not call the function again).

    d. The base case is always reached.

    e. None of the above

2. (Fill in the blank) A linked list in python consists of one or more instances of the _____ class.

    a. `list`

    b. `int`

    c. `Node`

    d. `None`

    e. None of the above

3. (True/False) Attempting to access the `value` or `next` attribute of `None` will result in an error.

4. (True/False) There is no way to traverse to the start of a linked list that has multiple Nodes given only a reference to the last `Node`.

<details>
<summary>SOLUTIONS</summary>

1. B, C, and D. A is true of all recursive functions, but does not guarantee that there won't be an infinite loop.

2. C

3. True, attempting to access any attributes of `None` will result in an error since it has no attributes.

4. True, Nodes only know about the `Node` "in front" of them, or the next `Node`, so you cannot move backwards in a linked list.

</details>

## Code Writing

1. Write a recursive function (not a method of the `Node` class) named `recursive_range` with `start` and `end` `int` parameters that will create a linked list with the Nodes having values counting from `start` to `end`, not including `end`, either counting down (decrementing) or up (incrementing) depending on what `start` and `end` are. The function signature is below to get you started.

    `def recursive_range(start: int, end: int) -> Node | None:`

2. Write a recursive method of the `Node` class named `append` that has parameters `self` and `new_val` which is of type `int`, and this method should create a new `Node` at the end of the linked list and return `None`. In other words, the last `Node` object before this method is called will have a `next` attribute of `None`, but after this method is called, it should have a `next` attribute equal to a `Node` object with value `new_val` and `next` attribute being `None` (since that new node is now the last `Node` in the linked list).

3. Write a recursive method of the `Node` class named `get_length` that has parameters `self` and `count` which is of type `int`, which if you were to call with a `count` argument of 0, would return the length of the linked list starting with `self` (not including `None`). Hint: Use `count` to keep track of a `Node` count between function calls. How would you write this method as an *iterative* function (with no `count` parameter)?

<details>
<summary>SOLUTIONS</summary>

1. Recursive range has two base cases, and the one that is used depends on if `start` is greater than or less than `end`.

    ```py
        def recursive_range(start: int, end: int) -> Node | None:
            if start == end:
                return None
            elif start < end:
                return Node(start, recursive_range(start + 1, end))
            else:
                return Node(start, recursive_range(start - 1, end))
    ```

2. Here is one way to make the `append` method:

    ```py
        def append(self, new_val: int) -> None:
            if self.next is None:
                self.next = Node(new_val, None)
            else:
                self.next.append(new_val)
    ```

3. Here are two possibilities:

```py
    def get_length(self, count: int) -> int:
        if self.next is None:
            return count + 1
        else:
            return self.next.get_length(count + 1)
```

```py
    def get_length(self, count: int) -> int:
        count += 1
        if self.next is None:
            return count
        else:
            return self.next.get_length(count)
```

</details>

## Short Answer

1. Based on the following code snippet, what would be the output of the following lines of code given in parts 1.1-1.4?

    ```py
        from __future__ import annotations

        # Node class definition included for reference!
        class Node:
            value: int
            next: Node | None

            def __init__(self, val: int, next: Node | None):
                self.value = val
                self.next = next

            def __str__(self) -> str:
                rest: str
                if self.next is None:
                    rest = "None"
                else:
                    rest = str(self.next)
                return f"{self.value} -> {rest}"

        x: Node = Node(4, None)
        y: Node = Node(8, None)
        
        x.next = y

        z: Node = Node(16, None)

        z.next = x

        x = Node(32, None)
    ```

    1.1. `print(z.next.next.value)`

    1.2. `print(y.next)`

    1.3. `print(x)`

    1.4. `print(z)`


<details>
<summary>SOLUTIONS</summary>

1. Question 1 answers:

    1.1. `8`

    1.2. `None`

    1.3. `32 -> None`

    1.4. `16 -> 4 -> 8 -> None`

</details>


# Unit Tests

## General 
1. How do you create a test function? What identifies the function as a test? 
2. How do you create a file to write all your unit tests?  
3. What does the assert statement do?
4. Explain the difference between a use case and an edge case. Give an example of both within a function. 
5. If a function passes all of its associated unit tests, then the function is implemented correctly for all possible inputs (True/False).

[Solutions](#conceptual-solutions)

---

## Unit Test Writing and Classifying

6. Suppose you have the following function, designed to return the index of the first even number in a list.

```python
def find_even(nums: list[int]) -> int:
    idx: int = 0
    while idx < len(nums):
        if nums[idx] % 2 == 0:
            return idx
        idx += 1
    return -1
```

Fill in this unit test with a use case.

```python
def test_find_even_use_case() -> None:
    """Put code here."""
```

---

7. Suppose you have the following function, designed to calculate the sum of the elements in a list.

```python
def sum_numbers(numbers: list[int]) -> int:
    if len(numbers) == 0: 
        raise Exception("Empty list - no elements to add")
    
    total: int = numbers[0]
    for i in range(1, len(numbers)): 
        total += numbers[i]
        
    return total
```

Fill in this unit test with a use case.

```python
def test_list_sum_use_case() -> None:
    """Put code here."""
```

---

8. Suppose you have the following function, designed to determine if a number is prime.

```python
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

Fill in this unit test with a use case.

```python
def test_is_prime_use_case() -> None:
    """Put code here."""
```

---

9. Suppose you want to test that a list of dictionaries will be mutated correctly. Here's a function that mutates a list of dictionaries by adding a new key-value pair to each dictionary in the list.

```python
def add_key_to_dicts(dicts: list[dict], key: str, value: int) -> None:
    for d in dicts:
        d[key] = value
```

Fill in this unit test with a use case to verify that the list of dictionaries is mutated correctly.

```python
def test_add_key_to_dicts_use_case() -> None:
    """Put code here."""
```

---

10. Suppose you want to test that a dictionary will be mutated correctly. Here's a function that mutates a dictionary by incrementing the value of a given key by 1.

```python
def increment_dict_value(d: dict[str, int], key: str) -> None:
    if key in d:
        d[key] += 1
    else:
        d[key] = 1
```

Fill in this unit test with a use case to verify that the dictionary is mutated correctly.

```python
def test_increment_dict_value_use_case() -> None:
    """Put code here."""
```

---

11. Suppose you have the following function, designed to sum the elements in a dictionary of list values and return the key with the largest summed value.

```python
def max_sum_dict(d: dict[str, list[int]]) -> str:
    keys = []
    for key in d:
        keys.append(key)

    values_list_1 = d[keys[0]]
    values_list_2 = d[keys[1]]

    total_1 = 0
    for value in values_list_1:
        total_1 += value

    total_2 = 0
    for value in values_list_2:
        total_2 += value

    if total_1 > total_2:
        return keys[0]
    else:
        return keys[1]
```

Fill in this unit test with a use case to verify that the function returns the key with the largest summed value.

```python
def test_max_sum_dict_use_case() -> None:
    """Put code here."""
```

---

12. Write three unit tests for the following function, two testing use cases and one testing an edge case.

```py
def divide_list(input_list: list[int], divisor: int) -> list[float]:
    """Returns a new list where each value is the value from input_list divided by divisor"""
    result: list[int] = []

    for num in input_list:
        result.append(num / divisor)

    return result
```

---

13. Consider the following code snippet:

```py
def fill_list(num: int, length: int) -> list[int]:
    """Fill a list with a single value."""
    result: list[int] = []

    i: int = 0
    while i < length:
        result.append[num]
        i += 1

    return result

list_A: list[int] = fill_list(4, 19) 
list_B: list[int] = fill_list(55, -2)
list_C: list[int] = fill_list(1, 110)
```

Which function calls would be considered a use case of this function (list the associated variable name e.g. `list_A`)? Which would be considered edge cases? If there are any edge cases, what result would you get in the associated variable(s)?

# Solutions

## Conceptual Solutions

1. A test function is created just like any other Python function, but it is identified as a test by starting its name with `test_`. In frameworks like pytest, any function that starts with `test_` is automatically detected and run as a test.

2. Create a new Python file, often named `<module_name>_test.py`, in the same directory as your module. Write all your test functions in this file.

3. The assert statement checks if a condition is true. If the condition is false, an AssertionError is raised, indicating that the test has failed.

4. A use case is a typical scenario where the function is expected to work as intended. For example, in a function that sums a list, a use case would be passing a list like `[1, 2, 3]`.
An edge case is a situation where the function might struggle or behave differently, like passing an empty list `[]` to a sum function.

5. This is False, as unit tests themselves can be incorrect so all tests passing is no guarantee of correctness even for the inputs the unit tests are testing for. Even if the unit tests are correct, there can still be certain inputs that they do not test for and therefore the unit tests cannot assure you that a function will always work properly. Unit tests are a helpful tool that can work well when implemented over a wide range of test inputs, but they must be accompanied by thoughtful implementation of the original function.

## Unit Test Writing

6. Solution below: 

```python
def test_find_even_use_case() -> None:
    nums = [1, 3, 5, 4, 7]
    assert find_even(nums) == 3
```

---

7. Solution below:

```python
def test_list_sum_use_case() -> None:
    # Test case 1: Normal list of positive numbers
    assert sum_numbers([1, 2, 3, 4, 5]) == 15

    # Test case 2: List with negative numbers
    assert sum_numbers([-1, -2, -3, -4, -5]) == -15

    # Test case 3: Mixed positive and negative numbers
    assert sum_numbers([1, -1, 2, -2, 3, -3]) == 0

    # Test case 4: List with a single element
    assert sum_numbers([10]) == 10

    # Do not worry about handling the exception! 
    # That is out of the scope of the class :)
```

---

8. Solution below:

```python
def test_is_prime_use_case() -> None:
    assert is_prime(7) is True
    assert is_prime(8) is False
```

---

9. Solution below:

```python
def test_add_key_to_dicts_use_case() -> None:
    dicts = [{"a": 1}, {"b": 2}]
    add_key_to_dicts(dicts, "c", 3)
    assert dicts == [{"a": 1, "c": 3}, {"b": 2, "c": 3}]
```

---

10. Solution below: 

```python
def test_increment_dict_value_use_case() -> None:
    d = {"a": 1, "b": 2}
    increment_dict_value(d, "a")
    assert d["a"] == 2
    increment_dict_value(d, "c")
    assert d["c"] == 1
```

---

11. Solution below: 

```python
def test_max_sum_dict_use_case() -> None:
    d = {"a": [1, 2, 3], "b": [4, 5]}
    assert max_sum_dict(d) == "b"
```

12. `list_A` and `list_C` would be use cases since this is how we would expect this function to be used and `list_B` would be an edge case as this is essentially attempting to make a function call that would construct a list of negative length since our `length` argument is -2. In this edge case the result would be an empty list since we would never enter the `while` loop.

13. Note: These are just some examples of what you could test for, but they will likely not be the same as what you wrote as there are many correct answers.

    The most straightforward use case test would be ensuring that on a normal input that the output is what you expect:

    ```py
    def test_normal_divide_list() -> None:
        classes: list[int] = [110, 210, 301, 455]
        assert divide_list(classes, 10) = [11.0, 21.0, 30.1, 45.5]
    ```

    Another unit test for an edge case might be to ensure that the original list was not mutated:

    ```py
    def test_no_mutate_divide_list() -> None:
        classes: list[int] = [110, 210, 301, 455]
        divide_list(classes, 10) # We don't need to store the result
        assert classes = [110, 210, 301, 455]
    ```

    Finally, an example of an edge case for this function would be a divisor of zero, which we should expect to result in an error. We can test to ensure that an error occurs like this:

    ```py
    def test_div_zero_error_divide_list() -> None:
        classes: list[int] = [110, 210, 301, 455]
        with pytest.raises(ZeroDivisionError):
            divide_list(classes, 0)
    ```