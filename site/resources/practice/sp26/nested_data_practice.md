---
title: Nested Data Structures Practice
author:
- Benjamin Eldridge
page: lessons
template: overview
---

# Nested Data Structures Practice Problems

## Memory Diagrams

1. Diagram the following code snippet. (Note that this function assumes that the column names are different in each table, which is different from the `concat` function that you completed in EX09)

    ```py
        def combine(
            first_table: dict[str, list[str]], second_table: dict[str, list[str]]
        ) -> dict[str, list[str]]:
            """Combines two column based tables with no columns in common into one without mutation."""
            result: dict[str, list[str]] = {}

            for first_columns in first_table:
                result[first_columns] = first_table[first_columns]

            for second_columns in second_table:
                result[second_columns] = second_table[second_columns]

            return result


        some_cols: dict[str, list[str]] = {"artist": ["Charli XCX", "TOTO"], "title": ["360", "Africa"]}
        other_cols: dict[str, list[str]] = {"runtime": ["2:13", "4:55"], "streams": ["504M", "2.5B"]}

        new_cols: dict[str, list[str]] = combine(some_cols, other_cols)
    ```

2. Diagram the following code snippet.

    ```py
        def replace_all_vals(row_table: list[dict[str, str]], old_val: str, new_val: str) -> None:
            """Mutates an row-based table to change all instances of old_val in the table to be new_val."""
            for curr_row in row_table:
                for curr_col in curr_row:
                    if curr_row[curr_col] == old_val:
                        curr_row[curr_col] = new_val
            
        favorites: list[dict[str, str]] = [
            {"name": "Alice", "season": "Fall", "fruit": "apple"},
            {"name": "Bob", "season": "Spirng", "fruit": "Pear"},
            {"name": "Eve", "season": "Winter", "fruit": "apple"}
        ]

        replace_all_vals(favorites, "Spirng", "Spring")
        replace_all_vals(favorites, "apple", "Apple")
    ```

<details>
<summary>SOLUTIONS</summary>
Note that the order of the ids on the heap for nested data structures may not be as you expect or were shown in class. The "technically" correct way is to start with the innermost data structures first like in the solutions below, but for the sake of demonstration this rule has not been strictly followed in lecture (where you may have seen the outermost data structure have its id go first). We will not take off points for how you order the inner and outer data structures that make up a nested data structure, so just use whichever method makes more sense to you.

1. <img class="img-fluid" src="/static/practice-mem-diagrams/combine.png"/>

2. <img class="img-fluid" src="/static/practice-mem-diagrams/replace_all_vals.png"/>

</details>

## Code Writing

1. Write a function named `less_than_mask` with two parameters of types `dict[str, list[int]]` (`data_table`) and `int` (`threshold`) that returns a `dict[str, list[bool]]` with the same keys (column names) as the data table but the values are `True` if the associated `int` in the data table is less than the threshold, and `False` otherwise. Example terminal usage:

    <pre>
    <div class="terminal">
    >>> test_table: dict[str, list[int]] = {"hi_temp": [72, 86, 68], "lo_temp": [61, 70, 60]}
    >>> test_threshold: int = 70
    >>> mask_table: dict[str, list[int]] = less_than_mask(test_table, test_threshold)
    >>> mask_table
    {"hi_temp": [False, False, True], "lo_temp": [True, False, True]}
    </div>
    </pre>

2. Write a function called `multiply_matrix_rows` that has a single parameter `list[list[int]]` (`matrix`) where each inner list (a row) is assumed to be the same length and a return type of `None`. This function will mutate its only parameter to multiply each integer in every row *except the last row* by the value in the next row in the same position. This is easiest to understand via a a visual example, so one is provided below. The unit test should pass if the function is correctly implemented.

    ```py
        def multiply_matrix_rows(matrix: list[list[int]]) -> None:
            # You do this part!

        def test_multiply_matrix_rows_4_by_4() -> None:
            """Test multiply_matrix_rows with a 4 by 4 example matrix"""

            example_matrix: list[list[int]] = [
                [1, 2, 3, 4],
                [4, 6, 8, 10],
                [5, 7, 9, 11],
                [10, 10, 10, 10]
            ]

            multiply_matrix_rows(example_matrix)

            expected_matrix: list[list[int]] = [
                [4, 12, 24, 40],
                [20, 42, 72, 110],
                [50, 70, 90, 110],
                [10, 10, 10, 10]
            ]

            assert example_matrix == expected_matrix
    ```

<details>
<summary>SOLUTIONS</summary>

1. There may be multiple ways to implement this function, here is one possible solution:

```py
def less_than_mask(data_table: dict[str, list[int]], threshold: int) -> dict[str, list[bool]]:
    result: dict[str, list[bool]] = {}
    for column in data_table:
        mask_col: list[bool] = []
        for value in data_table[column]:
            mask_col.append(value < threshold)
        result[column] = mask_col
    return result
```

2. There may be multiple ways to implement this function, here is one possible solution:

```py
def multiply_matrix_rows(matrix: list[list[int]]) -> None:
    for row_idx in range(0, len(matrix) - 1): # Skip the last row
        for col_idx in range(0, len(matrix[row_idx])):
            matrix[row_idx][col_idx] *= matrix[row_idx + 1][col_idx] # Same column, but next row
```

</details>