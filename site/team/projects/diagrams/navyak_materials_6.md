---
title: Practice Memory Diagram
author:
- Navya Katraju
page: lessons
template: overview
---


# Snippet

``` python
def add_movie(catalog: dict[str, int], name: str, runtime: int) -> None:
    catalog[name] = runtime
    print(f"Added '{name}' to your catalog.")

def lookup_runtime(catalog: dict[str, int], name: str) -> None:
    runtime: int = catalog[name]
    print(f"{name} is {runtime} minutes long.")

def main():
    my_movies: dict[str, int] = {"Clueless": 97, "Inception": 148}
    add_movie(my_movies, "Knives Out", 130)
    lookup_runtime(my_movies, "Clueless")

if __name__ == "__main__":
    main()
```

# Solution
![navyak_solution_6](navyak_solution_6.png)

*Image Description*
The Memory Diagram includes one box titled Output and below that box two columns, the left titled Stack and the right titled Heap.
The Stack includes 4 frames in the following order from top to bottom: Globals, main, add_movie, and lookup_runtime.
The Globals frame has 3 variables including add_movie, lookup_runtime, and main.
- add_movie points to a function on the Heap (lines 4-6).
- lookup_runtime points to a function on the Heap (lines 8-10).
- main points to a function on the Heap (lines 12-15).
The main frame has 3 items including the RA, RV, and a variabe named my_movies.
- The RA is defined at line 18.
- The RV is None.
- my_movies points to a dict[str, int] in the Heap
    - "Clueless", "Inception" are the keys, and 97, 148 are the values respectively.
The add_movie frame has 5 items including the RA, RV and 3 variables named catalog, name, and runtime.
- The RA is defined at line 14.
- The RV is None.
- catalog points to the same dict[str, int] in the Heap as my_movies in main.
    - There is a new key-value pair ("Knives Out": 130) added to this dictionary.
- name is "Knives Out".
- runtime is 130.
The lookup_runtime frame has 5 items including the RA, RV and 3 variables named catalog, name, and runtime.
- The RA is defined at line 15.
- The RV is None.
- catalog points to the same dict[str, int] in the Heap as catalog in add_movie.
- name is "Clueless".
- runtime is 97.

The Heap includes 3 function objects.
Output includes the 2 phrases: “Added 'Knives Out' to your catalog." and "Clueless is 97 minutes long."