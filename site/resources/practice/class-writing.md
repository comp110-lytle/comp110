---
title: Class Writing Practice Problems
author:
- David Karash
- Megan Zhang
- Alyssa Lytle
page: lessons
template: overview
---

# Questions

## Function + Method Writing With Class Objects

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

## Class Writing

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


# Solutions

## Function + Method Writing With Class Objects

### `Course` Solution

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

## Class Writing


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

### `Car` solution

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


### `HotCocoa` solution

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

#### Instantiation

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

### `TimeSpent` solution

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
