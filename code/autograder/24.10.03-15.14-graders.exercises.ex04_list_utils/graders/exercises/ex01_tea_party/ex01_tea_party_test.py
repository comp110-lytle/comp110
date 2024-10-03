"""Tests for Execise 01 - Tea Party Planner."""

__author__ = "Kris Jordan <kris@cs.unc.edu>"

import runpy
from random import randint
from pytest import CaptureFixture, mark, MonkeyPatch
from unittest.mock import patch
from graders.helpers import (
    author_is_a_valid_pid,
    set_stdin,
    reimport_module,
    assert_parameter_list,
    assert_return_type,
)


def assert_function_defined(module, fn_identifier) -> None:
    assert (
        getattr(module, fn_identifier, None) is not None
    ), f"Function {fn_identifier} is not defined"
    assert callable(
        module.tea_bags
    ), f"Identifier {fn_identifier} is not bound to a function"


MODULE = "exercises.ex01_tea_party"


@mark.weight(2)
def test_doc_string(capsys: CaptureFixture[str]):
    """Part 0. Doc String for module must be set and non-empty."""
    module = reimport_module(MODULE)
    assert getattr(module, "__doc__") is not None, "Module-level Doc String is required"
    assert len(getattr(module, "__doc__")) > 0, "Module-level Doc String is required"


@mark.weight(2)
def test_author(capsys: CaptureFixture[str]):
    """Part 0. __author__ global variable is present and correct format."""
    module = reimport_module(MODULE)
    assert author_is_a_valid_pid(module), "Valid 9-digit PID is required"


@mark.weight(2)
def test_tea_bags_defined():
    """Part 1. `tea_bags` - function is declared."""
    module = reimport_module(MODULE)
    assert_function_defined(module, "tea_bags")


@mark.weight(2)
def test_tea_bags_parameter():
    """Part 1. `tea_bags` - function has correct parameter type."""
    module = reimport_module(MODULE)
    assert_function_defined(module, "tea_bags")
    assert_parameter_list(module.tea_bags, [int])


@mark.weight(2)
def test_tea_bags_return_type():
    """Part 1. `tea_bags` - function has correct return type."""
    module = reimport_module(MODULE)
    assert_function_defined(module, "tea_bags")
    assert_return_type(module.tea_bags, int)


@mark.weight(2)
def test_tea_bags_doc_string():
    """Part 1. `tea_bags` - function has a docstring."""
    module = reimport_module(MODULE)
    assert_function_defined(module, "tea_bags")
    assert module.tea_bags.__doc__ is not None, "Docstring not defined"


rand_arg = randint(1, 1000)
rand_rv = rand_arg * 2


@mark.weight(2)
@mark.parametrize(
    "argument, expected_return_value",
    [(0, 0), (10, 20), (123, 246), (rand_arg, rand_rv)],
)
def test_tea_bags(argument, expected_return_value):
    """Part 1. `tea_bags - function calls return expected values (multiple arguments tested)."""
    module = reimport_module(MODULE)
    assert_function_defined(module, "tea_bags")
    assert (
        module.tea_bags(argument) == expected_return_value
    ), f"Expected tea_bags({argument}) to return {expected_return_value}"


@mark.weight(2)
def test_treats_defined():
    """Part 2. `treats` - function is declared."""
    module = reimport_module(MODULE)
    assert_function_defined(module, "treats")


@mark.weight(3)
def test_treats_parameter():
    """Part 2. `treats` - function has correct parameter type."""
    module = reimport_module(MODULE)
    assert_function_defined(module, "treats")
    assert_parameter_list(module.treats, [int])


@mark.weight(3)
def test_treats_return_type():
    """Part 2. `treats` - function has correct return type."""
    module = reimport_module(MODULE)
    assert_function_defined(module, "treats")
    assert_return_type(module.treats, int)


@mark.weight(2)
def test_treats_doc_string():
    """Part 2. `treats` - function has a docstring."""
    module = reimport_module(MODULE)
    assert_function_defined(module, "treats")
    assert module.treats.__doc__ is not None, "Docstring not defined"


rand_arg = randint(1, 1000)
rand_rv = round(rand_arg * 2 * 1.5)


@mark.weight(2)
@mark.parametrize(
    "argument, expected_return_value",
    [(0, 0), (1, 3), (2, 6), (3, 9), (rand_arg, rand_rv)],
)
def test_treats(argument, expected_return_value):
    """Part 2. `treats - function calls return expected values (multiple arguments tested)."""
    module = reimport_module(MODULE)
    assert_function_defined(module, "treats")
    assert (
        module.treats(argument) == expected_return_value
    ), f"Expected treats({argument}) to return {expected_return_value}"


@mark.weight(2)
def test_treats_calls_tea_bags():
    """Part 2. `treats` - must be implmented in terms of a call to `tea_bags` and use a keyword argument"""
    module = reimport_module(MODULE)
    assert_function_defined(module, "tea_bags")
    assert_function_defined(module, "treats")
    with patch("exercises.ex01_tea_party.tea_bags") as mock_tea_bags:
        module.treats(1)
        mock_tea_bags.assert_called_once_with(people=1)


@mark.weight(0.5)
def test_cost_defined():
    """Part 3. `cost` - function is declared."""
    module = reimport_module(MODULE)
    assert_function_defined(module, "cost")


@mark.weight(2.0)
def test_cost_parameter():
    """Part 3. `cost` - function has correct parameter types."""
    module = reimport_module(MODULE)
    assert_function_defined(module, "cost")
    assert_parameter_list(module.cost, [int, int])


@mark.weight(2.5)
def test_cost_return_type():
    """Part 3. `cost` - function has correct return type."""
    module = reimport_module(MODULE)
    assert_function_defined(module, "cost")
    assert_return_type(module.cost, float)


@mark.weight(2.5)
def test_cost_doc_string():
    """Part 3. `cost` - function has a docstring."""
    module = reimport_module(MODULE)
    assert_function_defined(module, "cost")
    assert module.cost.__doc__ is not None, "Docstring not defined"


rand_arg = randint(1, 1000)
rand_rv = round(rand_arg * 2 * 1.5)


@mark.weight(2.5)
@mark.parametrize(
    "tea_arg, treat_arg, expected_return_value",
    [
        (0, 0, 0.0),
        (1, 1, 1 * 0.5 + 1 * 0.75),
        (0, 1, 0.75),
        (1, 0, 0.5),
        (rand_arg, rand_arg, rand_arg * 0.5 + rand_arg * 0.75),
    ],
)
def test_cost(tea_arg, treat_arg, expected_return_value):
    """Part 3. `cost - function calls return expected values (multiple arguments tested)."""
    module = reimport_module(MODULE)
    assert_function_defined(module, "cost")
    assert (
        module.cost(tea_arg, treat_arg) == expected_return_value
    ), f"Expected cost({tea_arg}, {treat_arg}) to return {expected_return_value}"


@mark.weight(2.5)
def test_main_planner_defined():
    """Part 4. `main_planner` - function is declared."""
    module = reimport_module(MODULE)
    assert_function_defined(module, "main_planner")


@mark.weight(2.5)
def test_main_planner_parameter():
    """Part 4. `main_planner` - function has correct parameter type."""
    module = reimport_module(MODULE)
    assert_function_defined(module, "main_planner")
    assert_parameter_list(module.main_planner, [int])


@mark.weight(2.5)
def test_main_planner_return_type():
    """Part 4. `main_planner` - function has correct return type."""
    module = reimport_module(MODULE)
    assert_function_defined(module, "main_planner")
    assert_return_type(module.main_planner, None)


@mark.weight(2.5)
def test_main_planner_doc_string():
    """Part 4. `main_planner` - function has a docstring."""
    module = reimport_module(MODULE)
    assert_function_defined(module, "main_planner")
    assert module.main_planner.__doc__ is not None, "Docstring not defined"


rand_arg = randint(1, 1000)
rand_rv = round(rand_arg * 2 * 1.5)


@mark.weight(2.5)
@mark.parametrize(
    "guests, expected_output_strings",
    [
        (
            0,
            ["A Cozy Tea Party for 0 People", "Tea Bags: 0", "Treats: 0", "Cost: $0.0"],
        ),
        (
            2,
            ["A Cozy Tea Party for 2 People", "Tea Bags: 4", "Treats: 6", "Cost: $6.5"],
        ),
        (
            3,
            [
                "A Cozy Tea Party for 3 People",
                "Tea Bags: 6",
                "Treats: 9",
                "Cost: $9.75",
            ],
        ),
    ],
)
def test_main_planner(guests, expected_output_strings, capsys: CaptureFixture):
    """Part 4. `main_planner - function calls return expected values (multiple arguments tested)."""
    module = reimport_module(MODULE)
    assert_function_defined(module, "main_planner")
    module.main_planner(guests)
    output = _get_output(capsys)
    for i in range(len(expected_output_strings)):
        assert (
            expected_output_strings[i].lower() in output[i].lower()
        ), f'Printed Output: "{output[i]}" expected to find in this line "{expected_output_strings[i]}". Double check your spelling, punctuation, and spacing!'


@mark.weight(0.5)
def test_main_planner_calls_functions(capsys: CaptureFixture):
    """Part 4. `main_planner` - must be implmented in terms of a calls to other functions using keyword arguments"""
    module = reimport_module(MODULE)
    try:
        assert_function_defined(module, "main_planner")
        assert_function_defined(module, "tea_bags")
        assert_function_defined(module, "treats")
        assert_function_defined(module, "cost")
    except AssertionError:
        return True
    with patch("exercises.ex01_tea_party.tea_bags") as mock_tea_bags:
        with patch("exercises.ex01_tea_party.treats") as mock_treats:
            with patch("exercises.ex01_tea_party.cost") as mock_cost:
                module.main_planner(1)
                mock_tea_bags.assert_called()
                mock_treats.assert_called()
                mock_cost.assert_called_once()
                _ = _get_output(capsys)  # Avoids showing stdout in Gradescope


@mark.weight(5)
def test_run_as_module(capsys: CaptureFixture, monkeypatch: MonkeyPatch):
    """Part 5. Running Program Should Ask User for number of guests and call `main_planner`."""
    arg = "300"
    set_stdin(monkeypatch, [arg])

    module = reimport_module(MODULE)
    assert_function_defined(module, "main_planner")
    expected_output = [
        "A Cozy Tea Party for 300 People",
        "Tea Bags: 600",
        "Treats: 900",
        "Cost: $975.0",
    ]

    runpy.run_module(MODULE, run_name="__main__")
    output = _get_output(capsys)

    match_found = False
    for line in output:
        match_found = match_found or (line in expected_output)

    assert (
        match_found
    ), f"Run as a program, input '{arg}', was expecting to produce message '{expected_output}'. Got: '{output}'."


@mark.weight(5)
def test_does_not_use_assignment():
    """No forbidden constructs used (e.g. variable assignment)."""
    from graders.exercises.ex01_tea_party.no_variables import (
        assert_no_variable_assignment,
    )

    file = MODULE.replace(".", "/") + ".py"
    assert assert_no_variable_assignment(
        file
    ), "Variable assignment operator is not allowed in this exercise."


def _get_output(capsys):
    out, _err = capsys.readouterr()
    lines = out.split("\n")
    lines = list(filter(lambda s: s != "", lines))
    return lines
