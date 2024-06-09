"""Autograder for remove_repeats function created in vhunany.py file."""

import os
from grading.autograde import Configuration, run

results = run(Configuration(
   src_path="lessons/list_repeats.py",
   test_path=os.path.dirname(os.path.realpath(__file__)),
   pytest_points=70.0,
   typecheck_points=15.0,
   lint_points=15.0
))

print(results.to_json())