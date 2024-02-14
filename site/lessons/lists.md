---
title: Lists 
author:
- Alyssa Byrnes
page: lessons
template: overview
---
# Initialize a List

Initialize an empty grocery list:

`grocery_list: list[str] = list()`

Then print the list: 

`print(grocery_list)`


# Populating a List

Now, below `grocery_list: list[str] = list()`, but *above* `print(grocery_list)`, add the following lines:

`grocery_list.append("bananas")`
`grocery_list.append("milk")`
`grocery_list.append("bread")`

# Creating An Already Populated List

`grocery_list: list[str] = ["bananas", "milk", "bread"]`

# Indexing

Now **change** `print(grocery_list)` to `print(grocery_list[1])`. 

# Modifying by Index

Now, on line 7, add the line:

`grocery_list[1] = "cereal"`


# Length

Now **change** `print(grocery_list[1])` to `print(len(grocery_list))`.

# Removing an Item 

Finally, remove something from your list by adding the following line *above* `print(len(grocery_list))`:

`grocery_list.pop(2)`


# Lists in Functions

Functions can take lists as input
~~~
    def display(input: list[str]):
        """Print a list"""
        print(input)
~~~

~~~
    def mimic(input: list[str]) -> list[str]:
        """Print a list"""
        return input
~~~

Functions can modify lists.
~~~
    def remove_first(input: list[str]):
        input.pop(0)

    remove_first(grocery_list)
    print(grocery_list)
~~~

Functions can make lists
~~~
    def create(item1: str, item2: str) -> list[str]:
        """Create list of length 2."""
        new_list: list[str] = [item1, item2]
        return new_list
    
    created_list: list[str] = create("apricots", "oranges")
~~~

