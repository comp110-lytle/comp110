"""Script for testing a grader module while developing it.

The primary advantages this script has over running a grader module directly are:
    1. Run the grader module's main entrypoint and present results as a plaintext report rather than JSON.
    2. The GRADING_SOLUTION_ROOT environment variable is established as CLI argument to this script before running
       the grader module. The solution root is the path to the root directory of where a reference implementation
       of a submission for the project is stored.

Usage:
    python3 -m grading.test [grader_module]

Example:
    python3 -m grading.test comp110_graders.example
"""

__author__ = "Kris Jordan <kris@cs.unc.edu>"
__copyright__ = "Copyright 2020, Kris Jordan"
__license__ = "MIT"

import json
import importlib
import os
import subprocess
import sys
from typing import List, Tuple

PYTHON = sys.executable


def main() -> None:
    """Entrypoint of script."""
    grader_module, solution_root = _parse_args(sys.argv)
    _establish_grading_env_paths(solution_root)
    result = subprocess.run([PYTHON, "-m", grader_module], capture_output=True)
    _pretty_print(str(result.stdout, "utf-8"))


def _establish_grading_env_paths(solution_root: str) -> None:
    if "GRADING_GRADER_ROOT" not in os.environ:
        os.environ["GRADING_GRADER_ROOT"] = os.path.realpath(".")
    if "GRADING_SUBMISSION_ROOT" not in os.environ:
        os.environ["GRADING_SUBMISSION_ROOT"] = os.path.realpath(solution_root)


def _check_valid_module(argv: List[str]) -> bool:
    """Checks if input module is valid and checks for main.py file inside directory of module"""
    spec = importlib.util.find_spec(argv[1])
    if (spec is not None):
        path_to_check = os.path.join(os.getcwd(), "/".join(argv[1].split(".")))
        file_to_check = "/__main__.py"
        if os.path.isfile(f"{path_to_check}{file_to_check}"): 
            return True
        else:
            return False
    else:
        return False



def _parse_args(argv: List[str]) -> Tuple[str, str]:
    if len(argv) != 2:
        print("Usage: python3 -m comp110.grading.test [grader module]")
        sys.exit(1)
    if (not _check_valid_module(argv)):
        print(f"The module `{argv[1]}` does not appear to be a valid grader module.")
        sys.exit(1)
    return (argv[1], ".")


def _pretty_print(result_json: str) -> None:
    result = json.loads(result_json)
    passed = [test for test in result["tests"] if test["score"] == test["max_score"]]
    failed = [test for test in result["tests"] if test["score"] < test["max_score"]]

    if len(passed) > 0:
        print(f"========== PASSED {len(passed)}/{len(result['tests'])} ==========")
        for test in passed:
            if test["score"] == test["max_score"]:
                print(f"{test['score']:>4} / {test['max_score']:>4} - {test['name']}")

    if len(failed) > 0:
        print(f"========== FAILED {len(failed)}/{len(result['tests'])} ==========")
        for test in failed:
            print(f"{test['score']:>4} / {test['max_score']:>4} - {test['name']}")
            if test['output'] != "":
                output: str = test["output"]
                lines = output.splitlines()
                for line in lines:
                    print(f"  > {line}")

    print("================================")
    max_score = 0
    for test in result["tests"]:
        max_score += test["max_score"]
    percent = round(result["score"] / max_score * 100.0, 1)
    print(f"Score: {percent}% ({result['score']}/{max_score} points)")


if __name__ == "__main__":
    main()
