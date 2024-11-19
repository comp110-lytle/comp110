---
title: Lists Conceptual Questions
author:
- Viktorya Hunanyan
page: lessons
template: overview
---

# Questions

### 1. Refer to the following code snippett to answer the questions below: 
```python
from __future__ import annotations

class Node:
    def __init__(self, value: list[int], next: Node | None):
        self.value = value  # A list of integers
        # Either another Node or None
        if next is None:
            self.next = None
        else:
            self.next = next
```

- 1a. Given a linked list, write a recursive function, `sum_node_values`, that calculates the total sum of all integers in the linked list. Identify the base case and recursive step by commenting your code. Below is a REPL example of how you functions should work.

<pre>
<div class="terminal">
>>> from test import Node, sum_node_values
>>> node3 = Node([7, 8, 9], None)
>>> node2 = Node([4, 5], node3)
>>> node1 = Node([1, 2, 3], node2)
>>> print("Sum of all values:", sum_node_values(node1))
Sum of all values: 39
</div>
</pre>

- 1b. Given a linked list, write a recursive function, `increment_node_values`, that increments each integer in every node's list by 1. Identify the base case and recursive step by commenting your code.

<pre>
<div class="terminal">
>>> from test import Node, increment_node_values, print_nodes
>>> node3 = Node([7, 8, 9], None)
>>> node2 = Node([4, 5], node3)
>>> node1 = Node([1, 2, 3], node2)
>>> increment_node_values(node1)
>>> print("Values after incrementing:")
Values after incrementing:
>>> print_nodes(node1)
[2, 3, 4]
[5, 6]
[8, 9, 10]
</div>
</pre>

*Note:* `print_nodes` is a function that you will define in the next part. We are using it here to show you how your list of each Node should look like after you modified each list when you called `increment_node_values`.

- 1c. Given a linked list write a recursive function, `print_nodes`, that prints the contents of all nodes in the linked list. You should add a method to the Node class definition that is responsible for printing a Node object. Identify the base case and the recursive step.
<pre>
<div class="terminal">
>>> from test import Node, print_nodes
>>> node3 = Node([7, 8, 9], None)
>>> node2 = Node([4, 5], node3)
>>> node1 = Node([1, 2, 3], node2)
>>> print("Printing each node:")
Printing each node:
>>> print_nodes(node1)
[1, 2, 3]
[4, 5]
[7, 8, 9]
</div>
</pre>

- 1d. Write code to test your functions. 

[Solution to question 1](#solution-to-question-1)

### 2. Refer to the following code snippett to answer the questions below: 
```python
from __future__ import annotations

class BinaryTreeNode:
    def __init__(self, value: int, left: BinaryTreeNode | None, right: BinaryTreeNode | None):
        self.value = value  # Integer value of the node
        if left is None:
            self.left = None
        else:
            self.left = left
        
        if right is None:
            self.right = None
        else:
            self.right = right
```

- 2a. Given the following instantiations, draw a picture of what your Binary Tree looks like: 
```python
# Create a binary tree manually
node4 = BinaryTreeNode(4, None, None)
node5 = BinaryTreeNode(5, None, None)
node2 = BinaryTreeNode(2, node4, node5)
node3 = BinaryTreeNode(3, None, None)
root = BinaryTreeNode(1, node2, node3)
```

- 2b. Implement a recursive function named `sum_tree_values`. This function should accept a binary tree (or None) as input and return the total sum of all the values in the trees. 
- 2c. Create a recursive function called `increment_tree_value`s. The function should take a binary tree (or None) as input and increment the value of each node in the tree by 1. It should not return anything. 
- 2d. Draw a picture of what the your binary tree looks like after step 2c. 

[Solution to question 2](#solution-to-question-2)

# Solutions

## 1. Solutions to each part of question 1 are below: {#solution-to-question-1}
- 1a. Code below: 
```python
def sum_node_values(head: Node | None) -> int:
    if head is None:  # Base case
        return 0

    # Recursive step: Sum the elements of the current node and the sum of the rest of the list
    current_sum = 0
    for value in head.value:
        current_sum += value
    return current_sum + sum_node_values(head.next)
```

- 1b. Code below: 
```python
def increment_node_values(head: Node | None) -> None:
    if head is None:  # Base case
        return None
    
    # Recursive step: Increment each value in the current node
    for i in range(len(head.value)):  # Manually increment each element
        head.value[i] += 1
    increment_node_values(head.next)  # Process the next node
```

- 1c. Code below: 
```python
from __future__ import annotations

class Node:
    def __init__(self, value: list[int], next: Node | None):
        self.value = value  # A list of integers
        # Either another Node or None
        if next is None:
            self.next = None
        else:
            self.next = next

    def __str__(self) -> str:  # Magic method to print a Node object
        return str(self.value)

def print_nodes(head: Node | None) -> None:
    if head is None:  # Base case
        return None
    
    # Recursive step: Print the current node and then the rest of the list
    print(head)  # Use the __str__ method to get the string representation
    print_nodes(head.next)
```

- 1d. Code below: 
```python
# All code combined together, solution to 1d is underneath print_nodes definition
from __future__ import annotations

class Node:
    def __init__(self, value: list[int], next: Node | None):
        self.value = value  # A list of integers
        # Either another Node or None
        if next is None:
            self.next = None
        else:
            self.next = next

    def __str__(self) -> str:
        return str(self.value)  # Use Python's built-in str() for the list representation

def sum_node_values(head: Node | None) -> int:
    if head is None:  # Base case
        return 0

    # Recursive step: Sum the elements of the current node and the sum of the rest of the list
    current_sum = 0
    for value in head.value:  # Manually sum the list in the current node
        current_sum += value
    return current_sum + sum_node_values(head.next)

def increment_node_values(head: Node | None) -> None:
    if head is None:  # Base case
        return
    
    # Recursive step: Increment each value in the current node
    for i in range(len(head.value)):  # Manually increment each element
        head.value[i] += 1
    increment_node_values(head.next)  # Process the next node

def print_nodes(head: Node | None) -> None:
    if head is None:  # Base case
        return
    
    # Recursive step: Print the current node and then the rest of the list
    print(head)  # Use the __str__ method to get the string representation
    print_nodes(head.next)

# Solution for 1d: 

# Create a linked list manually
node3 = Node([7, 8, 9], None)
node2 = Node([4, 5], node3)
node1 = Node([1, 2, 3], node2)

# 1a: Sum all values in the nodes
print("Sum of all values:", sum_node_values(node1))

# 1b: Increment all values in the nodes
increment_node_values(node1)
print("Values after incrementing:")
print_nodes(node1)

# 1c: Print each node
print("Printing each node:")
print_nodes(node1)
```

## 2. Solutions to each part of question 2 are below: {#solution-to-question-2}
- 2a. Picture below. 
*Note* This is just a visual representation of what your binary tree looks like and is not what is actually represented in memory. Your picture might look different but should be somewhat similar. 

<img class="img-fluid" src="/static/practice-problems/binarytreeinitial.jpg" alt=" " />


- 2b. Code below: 

```python
def sum_tree_values(root: BinaryTreeNode | None) -> int:
    if root is None:  # Base case: If the node is None, return 0
        return 0

    # Recursive step: Sum the value of the current node, plus the sum of the left and right subtrees
    return root.value + sum_tree_values(root.left) + sum_tree_values(root.right)
```

- 2c. Code below: 

```python
def increment_tree_values(root: BinaryTreeNode | None) -> None:
    if root is None:  # Base case: If the node is None, do nothing
        return None

    # Recursive step: Increment the current node's value
    root.value += 1

    # Recursively increment the values in the left and right subtrees
    increment_tree_values(root.left)
    increment_tree_values(root.right)
```

- 2d. Picture below. 
*Note* This is just a visual representation of what your binary tree looks like and is not what is actually represented in memory. Your picture might look different but should be somewhat similar. 

<img class="img-fluid" src="/static/practice-problems/binarytreeafteraddingone.jpg" alt=" " />
