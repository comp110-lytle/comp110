---
title: Practice Memory Diagram
author:
- Viktorya
page: lessons
template: overview
---

# Snippet

```
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
        todo_list: dict[str, str] = {
            'Buy groceries': 'not done',
            'Read a book': 'done',
            'Write report': 'not done',
            'Call mom': 'done'
        }

        add_task(todo_list, 'Finish homework')

        mark_done(todo_list, 'Write report')

        print("Current to-do list:", todo_list)

    if __name__ == "__main__":
        main()
```

# Solution
*(Coming Soon)*

<!-- <img class="img-fluid" src="/static/practice-mem-diagrams/analyze_string.jpg" alt="Image Description Here"  /> -->

## Video
*(Video Coming Soon)*

## Image Description
*(Coming Soon)*