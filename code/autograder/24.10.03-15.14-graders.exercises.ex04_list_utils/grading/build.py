"""Build an autograder zip for deployment on Gradescope autograding.

This script creates a temporary staging directory and then:

1. Generating setup.sh for preparing Gradescope container.
2. Generating run_autograder script to run the grader module in Gradescope environment.
3. Copying the entire working directory while filtering out some files (eg: .pyc).
4. Zips the contents into a timestamped zip: {year}.{month}.{day}-{hour}.{min}-{grader_module}.zip

Usage:
    python3 -m comp110.grading.build [grader module]
"""

__author__ = "Kris Jordan <kris@cs.unc.edu>"
__copyright__ = "Copyright 2020, Kris Jordan"
__license__ = "MIT"

import os
import tempfile
import shutil
import sys
from typing import List
from jinja2 import Environment, FileSystemLoader
from .helpers import date_prefix


def main() -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        grader_module = _parse_args(sys.argv)
        generate_templates(temp_dir, grader_module)
        copy_all(temp_dir)
        zip_dir(temp_dir, date_prefix(grader_module))


def _parse_args(argv: List[str]) -> str:
    if len(argv) != 2:
        print("Usage: python -m grading.build [grader_module]", file=sys.stderr)
        sys.exit(1)
    return argv[1]


def generate_templates(target_dir: str, grader_module: str) -> None:
    templates_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "templates")
    loader = FileSystemLoader(templates_path)
    env = Environment(loader=loader)
    run_autograder = env.get_template("run_autograder")
    setup_sh = env.get_template("setup.sh")
    with open(os.path.join(target_dir, "run_autograder"), "w") as file:
        file.write(run_autograder.render(grader_module=grader_module))
    with open(os.path.join(target_dir, "setup.sh"), "w") as file:
        file.write(setup_sh.render(grader_module=grader_module))


def copy_all(target_dir: str) -> None:
    def ignore(dir: str, contents: List[str]) -> List[str]:
        deny = [
            ".git", ".vscode", "__pycache__", "*.pyc", ".DS_Store",
            ".mypy_cache", ".pytest_cache", "*.zip"
        ]

        # Ignore top-level dirs in `code/` to prevent things like our solutions from being included.
        if dir == ".":
            deny += ["exercises", "quiz", "projects", "lessons", "training", "admin"]
        
        for entry in contents:
            if entry.endswith(".pyc"):
                deny.append(entry)
        return deny

    shutil.copytree(".", target_dir, ignore=ignore, dirs_exist_ok=True)




def zip_dir(path: str, target: str) -> None:
    shutil.make_archive(target, "zip", path, ".")


if __name__ == "__main__":
    main()
