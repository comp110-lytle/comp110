"""Autograder for CQ, while loops practice."""

from os import path
from grading import autograde

configuration = autograde.Configuration(
    src_path="CQs/cq03_while_loops.py",
    test_path=path.dirname(path.realpath(__file__)),
    pytest_points=90.0,
    typecheck_points=10.0,
    lint_points=0.0
)

results = autograde.run(configuration)

print(results.to_json())
