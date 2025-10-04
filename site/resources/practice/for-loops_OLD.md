---
title: For Loops Questions
author:
- Alyssa Lytle
- Megan Zhang
- David Karash
page: lessons
template: overview
---

# Questions

## Conceptual

1.1 Rewrite the following code snippet with same functionality using a `for ... in` loop.
1.2 Rewrite the following code snippet with same functionality using a `for ... in range(...)` loop.

```
    stats: list[int] = [7, 8, 9]
    index: int = 0
    total: int = 100
    while index < len(stats):
        total -= stats[index]
        index += 1
```

2. Can you iterate through an object using a for loop while also modifying it (removing or adding elements)?

[Solutions](#conceptual-solutions)

# Solutions

## Conceptual Solutions


1.1
```
    stats: list[int] = [7, 8, 9]
    total: int = 100
    for elem in stats:
        total -= elem
```

1.2
```
    stats: list[int] = [7, 8, 9]
    total: int = 100
    for index in range(0, len(stats)):
        total -= stats[index]
```

2. No, generally you cannot safely iterate through an object (like a list or dictionary) while simultaneously modifying it by adding or removing elements during the iteration. Doing so can lead to unexpected behavior or errors like the `RuntimeError: dictionary changed size during iteration`. When you iterate over an object, Python keeps track of the size and structure of that object. If you modify it (e.g., by adding or removing elements), this can disrupt the iteration process because the underlying data structure changes during traversal.

Removing elements: Can cause the iteration to skip items or crash because the index or key you're iterating over might no longer exist.
Adding elements: Can lead to the same type of issue, as the size of the object changes unexpectedly, leading to errors.

Take for example this code: 

```python
    def add_task(todo_list, task):
        task_found: bool = False
        for existing_task in todo_list:
            if existing_task == task:
                task_found = True

            if not task_found:
                todo_list[task] = 'not done'

    def mark_done(todo_list, task):
        for existing_task in todo_list:
            if existing_task == task:
                todo_list[existing_task] = 'done'

    def main():
        todo_list: dict[str, str] = {'Buy groceries': 'not done', 'Read a book': 'done', 'Write report': 'not done', 'Call mom': 'done'}

        add_task(todo_list, 'Finish homework')

        mark_done(todo_list, 'Write report')

        print("Current to-do list:", todo_list)

    if __name__ == "__main__":
        main()
```