---
title: Lists and Dictionaries
author:
- Aneka Happer
page: resource
template: overview
---

## Lists

A __list__ is a variable (with a name) that holds many elements of the same type addressed by indices.

Here's how you make a list:

~~~ {.python .numberLines startFrom="1"}
<name>: list[<type>] = [<element1>, <element2>, <element3>, ...]
~~~

The above syntax includes declaration *and* initialization. It also includes information about the type of the array. Here's some examples:

~~~ {.python .numberLines startFrom="1"}
friends: list[str] = ["Jim", "Kevin", "Erin"]
ratings: list[int] = [7, 4, 9, 8, 3]
answers: list[bool] = [True, False, False]
~~~

Let's take a closer look at how lists work.

### What is an index?

An index is the integer used to reference each element in a list.

The first element of a list is located at index 0, the second is at index 1, and so on.

NOTE: the length of an array does not equal the last index! Lists are "zero-indexed" meaning they start counting indices at 0. So the length of our list will always be the last index + 1.

To show this, a two element list would have the first element at index 0 and the second at index 1. However, since there are 2 elements, the length of the list is 2.

### How do you access an element?

When you access an element, you can assign it to a variable to more easily access it later.

You can also change individual elements in a list without having to create an entirely new list!

Example:

~~~ {.python .numberLines startFrom="1"}
myFriends: list[str] = ["Jim", "Kevin", "Erin"]

# accessing first element in the friends list
myBestFriend: str = friends[0]

# reassigning elements in a list
myFriends[2] = "Pam"

# myFriends is now: ["Jim", "Kevin", "Pam"]
~~~

A big thing to remember is that since lists are 0-indexed, meaning the index numbers start with the first one being 0, the last index of a list is the length of the list - 1, or len(<listName>) - 1.

### Adding and removing elements from a list

Adding an element onto the end of a list is called __appending__ the element to the list. We do this by using the append() method and putting the elemnt you want to add inside append. For example: 

~~~ {.python .numberLines startFrom="1"}
myFriends: list[str] = ["Jim", "Kevin", "Erin"]
myFriends.append("Pam")

# myFriends is now: ["Jim", "Kevin", "Erin", "Pam"]
~~~

To remove the last element from a list, you can use the pop() method with no arguement. If you want to remove an element at a specific index, simply reference that index in the pop method. Here's an example of both:

~~~ {.python .numberLines startFrom="1"}
chores: list[str] = ["sweep", "laundry", "mop", "dust"]
chores.pop()
# chores is now: ["sweep", "laundry", "mop"]

chores.pop(1)
# chores is now: ["sweep", "mop"]
~~~

## Dictionaries

A __dictionary__  is a data structure available in Python which lets you organize data into "key-value" pairs. 

The basic syntax of a dictionary is shown below:

~~~ {.python .numberLines startFrom="1"}
<name>: dict[<keytype>, <valuetype>] = {
    <key1>: <value1>
    <key2>: <value2>
    ...
}
~~~

But what are keys and values exactly? Lets dive in a little deeper. 

### Keys

Put simply, a __key__ is what you look up a value by. Keys can be any *immutable* type, such as __str__, __int__, __float__, __bool__, but not __lists__ or other __dicts__ for example. Each key is uniquely paired with their corresponding value, meaning you cannot have two identical keys in your dictionary. 

### Values

The __value__ in a dictionary refers to the data being stored. Unlike keys, values can be of any type. It is possible for two values in a dictionary to be identical, provided their associated keys are different. 

### Inserting items into a dictionary 

To construct a dictionary, you can declare it and initalize it in one go as shown below: 

~~~ {.python .numberLines startFrom="1"}
favColor: dict[str, str] = {
    "Ezri": "blue"
    "Claire": "yellow"
    "Tori": "green"
}
# note: dictionaries can have different data types for their key-value pairs
# this example happens to have keys and values that are both of type str
~~~

But it's more useful to be able to add items after initializing your dictionary. To do so, reference the name of the dictionary followed by brackets surrounding whatever you want your key to be, then assign it to the corresponding value. For example,

~~~ {.python .numberLines startFrom="7"}
favColor["Kaki"] = "red"
# in this example "Kaki" is the key and "red" is the value
~~~

### Remove items from a dictionary 

Similar to __lists__, you can remove an item from a dictionary by using the *pop()* method. To indicate which item you want to remove, use the key as the arguement for pop inside the parenthesis. In addition, the pop method will return the corresponding value.

~~~ {.python .numberLines startFrom="9"}
toriColor: str = favColor.pop("Tori")
# now the favColor contains {"Ezri": "blue", "Claire": "yellow", "Kaki": "red"}
# toriColor's value is "green"
~~~

### Accessing and modifying items

To access an item in a dictionary, write the name of your dictionary followed by brackets which enclose the key for the item you want to accesss. You can change the value of an item by reassigning the key to a new value:

~~~ {.python .numberLines startFrom="13"}
favColor["Ezri"] = "purple"
# we changed the value associatetd with Ezri from "blue" to "purple"
~~~

Sometimes it can be useful to modify a value based on what is was previously, an example of this is shown below.

~~~ {.python .numberLines startFrom="1"}

points: dict[str, int] = {
    "player1": 10
    "player2": 11
    "player3": 6
}

points["player3"] = points["player3"] + 2
# now the value corresponding to player3 is 8
~~~


