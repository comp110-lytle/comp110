"""Autograder for comp110.example."""

from grading import autograde

configuration = autograde.Configuration(
    src_path="setup/failing.py",
    test_path="graders/setup/failing",  # TODO: Make this relative to current path?
    pytest_points=55.0,
    typecheck_points=15.0,
    lint_points=15.0
)

results = autograde.run(configuration)

print(results.to_json())
