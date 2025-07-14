"""Autograder for loops practice"""

from os import path
from grading import autograde

configuration = autograde.Configuration(
    src_path="CQs/cq05_for_loops",
    test_path=path.dirname(path.realpath(__file__)),
    pytest_points=96.0,
    typecheck_points=4.0,
    lint_points=0.0
)

results = autograde.run(configuration)

print(results.to_json())
