"""Helper function for ensuring no variables are used."""

import ast
import os


def assert_no_variable_assignment(file_path: str) -> bool:
    class AssignmentFinder(ast.NodeVisitor):
        def __init__(self):
            self.has_assignment = False

        def visit_Assign(self, node: ast.Assign):
            if not any(
                isinstance(target, ast.Name) and target.id == "__author__"
                for target in node.targets
            ):
                self.has_assignment = True

    if "GRADING_SUBMISSION_ROOT" in os.environ:
        file_path = f"{os.environ['GRADING_SUBMISSION_ROOT']}/{file_path}"

    with open(file_path, "r") as file:
        module_content = file.read()

    tree = ast.parse(module_content)
    finder = AssignmentFinder()
    finder.visit(tree)

    return not finder.has_assignment

