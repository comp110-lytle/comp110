---
title: Object Oriented Programming
author:
- Ezri White
page: resource
template: overview
---

>A __class__ is a blueprint for an object. An object's class is what defines its attributes and capabilities. Classes are made up of 3 main parts; attributes, constructors and methods.

### Definition Syntax

Syntax overview for class declaration and definition: 

~~~ {.python}
    class <class_name>:
        <attribute_name> : <attribute_type>
        <attribute_name> : <attribute_type> = <attribute_default_value>

        def __init__(self, <parameter_name> : <parameter_type>):
            self.<attribute_name> = <parameter_name>
        
        def <method_name>(self, <parameters...>) -> <return_type>:
            <method_body>
~~~

Example of class declaration:

~~~ {.python}
    class Animal:
        sound: str

        def __init__(self, noise: str):
            self.sound = noise
        
        def make_noise(self, times: int) -> None:
            for _ in range(times):
                print(self.sound)
~~~


### Creation Syntax

Initializing a composite data type requires constructing a new object. The general syntax for this is as follows:

~~~ {.python}
    <variable_name> : <class_name> = <class_name>(<constructor parameters>)
~~~

Example of object creation:

~~~ {.python}
    pig: Animal = Animal("oink")
    dog: Animal = Animal("woof")
~~~

## attributes

Classes have attributes. Each object made from a class will have all the attributes established in that class. Additionally, each attribute in a class has a specific type. So, all objects we create from a certain class will contain all attributes defined in the class, and we can customize the values within these attributes for each individual object. For example:

~~~ {.python}
    class TarHeel:
        name: str = ""
        PID: int = 0
        hatesDook: bool = true
~~~

The attributes declared inside the body of the TarHeel class are name, PID, and hatesDook. Every TarHeel object we make will have these attributes.

In this example, there are defualt values for each attribute of "", 0, true respectively. We can declare two new Tar Heels with all the default attributes as seen below:

~~~ {.python}
    student1: TarHeel = TarHeel()
    student2: TarHeel = TarHeel()
~~~

### attribute Access

To access an object's attribute, just use the name of the object followed by the dot operator (.) followed by the attribute name.

~~~ {.python}
    print(student1.PID)
    if student2.hatesDook:
        print("Go Heels!")
~~~

For instance, the code above accesses first the *PID* attribute of student1 and then the *hatesDook* attribute of student2. We would expect this to print:

~~~ {.python}
    0
    Go Heels!
~~~

### attribute Assignment

We can also use the dot operator (.) in order to reassign attributes of objects. Notice we have to specify which student we are referring to. 

~~~ {.python}
    student1: TarHeel = TarHeel()
    student1.name = "Claire"
    student1.PID = "123456789"

    student1: TarHeel  = TarHeel()
    student1.name = "Aneka"
    student1.PID = "987654321"
~~~

Now if we were to run the following:

~~~ {.python}
    print(student1.name)
    print(student2.PID)
~~~

It would output:

~~~ {.python}
    Claire
    987654321
~~~

## Constructors
Every class has a constructor. A class constructor specifies initial attributes of the class from outside of the class to create an __instance__ of the class (also called an __object__ of the class). 

A constructor is a "magic" method because it is *automagically called* when the class is called.

In Python, __methods of classes__ look very similar to functions, but they are defined inside of the class. __A constructor__ is a method that every class has, and it requires specific syntax.

### Example
Let's stick with the TarHeel example:

~~~ {.python}
    class TarHeel:
        name: str
        PID: int
        hatesDook: bool = true

        def __init__ (self, student_name: str, student_PID: int):
            self.name = student_name
            self.PID = student_PID
~~~

The constructor always begins with `def __init__ (self, parameters)` and has no return type. The body of the constructor reassigns the class's attributes to the values passed by the parameters. Let's look at how this works by construction two new TarHeel objects:

~~~ {.python}
    student3: TarHeel = TarHeel("Tori", 500500500)
    student4: TarHeel = TarHeel("Ezri", 111222333)
~~~

We can still access an object's attribute in the same way as before:

~~~ {.python}
    print(student3.name)
    if student4.hatesDook:
        print("Go Heels!")
~~~

This will output:

~~~ {.python}
    Tori
    111222333
~~~

We can still change attributes – now, student3's name is "Baller"

~~~ {.python}
    student3.name = "Baller"
~~~

But we cannot call an empty constructor.

~~~ {.python}
    student5: TarHeel = TarHeel()  # Will FAIL!
~~~

### Choosing what goes into the constructor

Notice that in the TarHeel constructor, we specifically initialized `name` and `PID`, but not `hatesDook`. Because all TarHeels hate dook, `hatesDook` can have a default value of `True` that does not need to be specified upon construction!

On the other hand, we know each TarHeel has a unique name and PID, so we want to specify these values in the class constructor.

### Self
What is up with this `self` keyword? Essentially, `self` is assigned to a reference of the object you are working with on the heap. If you call a method on `student3`, for example, `this` will refer to the `student3` object on the heap.

In the constructor, `self.name` references the `name` attribute of the `self` object. If we were constructing a new TarHeel object called `student6`, this would be `student6`'s `name` attribute.

## Methods
Class methods are specific funtionality written for class instances within the classes themselves. 

### Syntax

Besides the first parameter of a method being `self`, a method's syntax is the same as a function's! Method syntax is as follows:

~~~ {.python}
    def method_name(self, [params...]) -> return type:
        <method body>
~~~

### Calling a method
Once defined, a method can be called on any object of the class! To call a method, you use the __dot operator__, similar to how you access attributes of an object. Dissimilar, however, you end this call with double parentheses and any necessary arguments *besides* `self`!

General syntax is:
~~~ {.python}
    object.method_name(arguments)
~~~

Upon a method call, remember that `self` is automatically assigned to the object the method is being called on. While the method evaluates, self references the object on the heap!

### Example

Let's make a new class called Coffee:

~~~ {.python}
    class Coffee:
        """A coffee implementation."""
        customer_name: str
        size: str
        whip: bool
        espresso_shots: int

        def __init__(self, name: str, size: str):
            self.customer_name = name
            self.size = size
            self.whip = True  # assume all people want whip :)

            if self.size == "small":
                self.espresso_shots = 1
            elif self.size == "large":
                self.espresso_shots = 2
            
        def make_decaf(self) -> None:
            """Makes the coffee decaf by taking away the espresso."""
            self.espresso_shots = 0

        def call_customer(self, message: int) -> str:
            """Generates a call for the customer to grab their coffee!"""
            personal_message: str

            if message == 1:
                personal_message = "Have a great day!"
            else:
                personal_message = "Come back soon!"

            return f"Your coffee is ready, {self.name}! {personal_message}"

        def remove_whip(self) -> None:
            """Removes whip from drink."""
            whip = False
~~~

In this class, we have 4 attributes, a constructor, and 3 methods! The methods `make_decaf` and `remove_whip` mutate attributes of the object they're called upon, and the method `call_customer` returns a string unique to the object. 

Let's create some `Coffee` objects and call its methods to see what happens:

~~~ {.python}
    # creates a small coffee for Aneka with 1 cream, 1 sugar
    coffee1: Coffee = Coffee("Aneka", small, 1, 1)

    # creates a large coffee for Tori with 2 cream, 0 sugar
    coffee2: Coffee = Coffee("Tori", large, 2, 0)

    # makes Aneka's coffee decaf (have 0 espresso shots)
    coffee1.make_decaf()

    # removes whip from Tori's coffee
    coffee2.remove_whip()

    # Tori changes mind, adds back whip to Tori's coffee using direct attribute access
    coffee2.whip = True

    # generates and prints messages for the barista
    print(coffee1.call_customer(1))
    print(coffee2.call_customer(2))
~~~

These last two lines will output:

~~~ {.python}
    "Your coffee is ready, Aneka! Have a great day!"
    "Your coffee is ready, Tori! Come back soon!"
~~~

## Optional Parameters

Imagine you want to modify your Coffee class. You notice 80% of your customers order large coffees, so you want to simply your implementation to make each Coffee __default__ to large. How could you do this?

The solution to your problem is making your parameters *optional* by assigning default values to specific parameters. Let's look at our Coffee constructor. 

~~~ {.python}
    class Coffee
        # ...

        def __init__(self, name: str, size: str):
            # ...
~~~

If we want our coffee to default to large, we want to assign `size` a default value of `large`. A Coffee object can be specified to be small upon construction, but the size may also be left out to default the coffee size to large. Check out the __init__ parameters:

~~~ {.python}
    class Coffee
        # ...

        def __init__(self, name: str, size: str = "large"):
            # ...
~~~

Let's see how construction works now:

~~~ {.python}
    # creates a large coffee for Ezri
    coffee_3: Coffee = Coffee("Ezri")

    # creates a small coffee for Claire
    coffee_4: Coffee = Coffee("Claire", small)
~~~

Notice that we left out the size of Ezri's coffee upon construction... Since this argument is missing, the size variable is assigned to the default "large". Claire's coffee size is specified, so the default "large" is ignored.