"""Tests for Exercise 07 - Simpy."""

__author__ = "Kaki Ryan <kakiryan@cs.unc.edu>"

from pytest import mark
from exercises.ex09.Simpy import Simpy
from graders.helpers import author_is_a_valid_pid, reimport_module
import inspect

MODULE = "exercises.ex09.Simpy"


@mark.weight(0)
def test_author():
    """Simpy.py - __author__ str variable is correct PID format."""
    module = reimport_module(MODULE)
    assert author_is_a_valid_pid(module)


@mark.weight(3)
def test_part_0_simpy_constructor():
    """Simpy.py - constructor defined with correct parameters."""
    module = reimport_module(MODULE)
    sig = inspect.signature(module.Simpy.__init__)
    assert len(sig.parameters) == 2
    param_names = list(sig.parameters)
    vals = param_names[1]
    assert sig.parameters[vals].annotation == 'list[float]'


@mark.weight(2)
def test_part_1_simpy_str_signature():
    """Simpy.py - __str__ method defined with no arguments and returns a str."""
    module = reimport_module(MODULE)
    sig = inspect.signature(module.Simpy.__str__)
    assert len(sig.parameters) == 1
    assert sig.return_annotation == 'str'


@mark.weight(3)
def test_part_1_simpy_str_functionality():
    """Simpy.py - __repr__ method works as expected with all ones."""
    simp = Simpy([1.0, 1.0, 1.0])
    assert simp.__str__() == f"Simpy({simp.values})"


@mark.weight(3)
def test_part_1_simpy_str_functionality_2():
    """Simpy.py - __str__ method works as expected with random values."""
    simp = Simpy([1.0, 4.0, 5.0, -10.0, -110.0])
    assert simp.__str__() == f"Simpy({simp.values})"


@mark.weight(2)
def test_part_2_simpy_fill_signature():
    """Simpy.py - fill method has two parameters (float, int) and returns None."""
    module = reimport_module(MODULE)
    sig = inspect.signature(module.Simpy.fill)
    assert len(sig.parameters) == 3
    param_names = list(sig.parameters)
    int_param = param_names[1]
    float_param = param_names[2]
    assert sig.parameters[int_param].annotation == 'float' and sig.parameters[float_param].annotation == 'int'
    assert sig.return_annotation == 'None'


@mark.weight(3)
def test_part_2_simpy_fill_functionality_1():
    """Simpy.py - fill method works when we start with an empty list."""
    simp = Simpy([])
    simp.fill(5.0, 4)
    assert simp.values == [5.0, 5.0, 5.0, 5.0]


@mark.weight(3)
def test_part_2_simpy_fill_functionality_2():
    """Simpy.py - fill method works when our Simpy array needs to grow."""
    simp = Simpy([5.0, 5.0, 5.0, 5.0])
    simp.fill(6.0, 6)
    assert simp.values == [6.0, 6.0, 6.0, 6.0, 6.0, 6.0]


@mark.weight(3)
def test_part_2_simpy_fill_functionality_3():
    """Simpy.py - fill method works when our Simpy array needs to shrink."""
    simp = Simpy([5.0, 5.0, 5.0, 5.0])
    simp.fill(1.0, 1)
    assert simp.values == [1.0]


@mark.weight(2)
def test_part_3_simpy_arange_signature():
    """Simpy.py - arange method has three float parameters and returns None."""
    module = reimport_module(MODULE)
    sig = inspect.signature(module.Simpy.arange)
    assert len(sig.parameters) == 4
    param_names = list(sig.parameters)
    float1 = param_names[1]
    float2 = param_names[2]
    float3 = param_names[3]
    assert sig.parameters[float1].annotation == 'float' and sig.parameters[float2].annotation == 'float' and sig.parameters[float3].annotation == 'float'
    assert sig.return_annotation == 'None'


@mark.weight(3)
def test_part_3_simpy_arange_functionality_1():
    """Simpy.py - arange method works when we give positive start/stop."""
    simp = Simpy([])
    simp.arange(1.0, 5.0)
    assert simp.values == [1.0, 2.0, 3.0, 4.0]


@mark.weight(3)
def test_part_3_simpy_arange_functionality_2():
    """Simpy.py - arange method works when we give a fractional step."""
    simp = Simpy([])
    simp.arange(0.0, 1.0, 0.25)
    assert simp.values == [0.0, 0.25, 0.5, 0.75]


@mark.weight(3)
def test_part_3_simpy_arange_functionality_3():
    """Simpy.py - arange method works when we give all negative arguments."""
    simp = Simpy([])
    simp.arange(-1.0, -5.0, -1.0)
    assert simp.values == [-1.0, -2.0, -3.0, -4.0]


@mark.weight(2)
def test_part_4_simpy_sum_signature():
    """Simpy.py - sum method has no extra parameters and returns a float."""
    module = reimport_module(MODULE)
    sig = inspect.signature(module.Simpy.sum)
    assert len(sig.parameters) == 1
    assert sig.return_annotation == 'float'


@mark.weight(3)
def test_part_4_simpy_sum_functionality():
    """Simpy.py - sum method works as expected."""
    simp = Simpy([1.0, 5.0, 9.0])
    assert simp.sum() == 15.0


@mark.weight(2)
def test_part_5_simpy_add_signature():
    """Simpy.py - __add__ method defined with correct signature."""
    module = reimport_module(MODULE)
    sig = inspect.signature(module.Simpy.__add__)
    assert len(sig.parameters) == 2
    param_names = list(sig.parameters)
    param1 = param_names[1]
    assert sig.parameters[param1].annotation == 'Union[float, Simpy]' or sig.parameters[param1].annotation == 'Union[Simpy, float]'
    assert sig.return_annotation == 'Simpy'


@mark.weight(3)
def test_part_5_simpy_add_functionality1():
    """Simpy.py - __add__ method works with two Simpy objects."""
    module = reimport_module(MODULE)
    simp1 = module.Simpy([1.0, 5.0, 9.0])
    simp2: Simpy = module.Simpy([1.0, 1.0, 1.0])
    result: Simpy = simp1 + simp2
    assert result.values == [2.0, 6.0, 10.0]


@mark.weight(3)
def test_part_5_simpy_add_functionality2():
    """Simpy.py - __add__ method works with one Simpy object and a float."""
    simp1 = Simpy([1.0, 5.0, 9.0])
    result = simp1 + 2.0
    assert result.values == [3.0, 7.0, 11.0]


@mark.weight(2)
def test_part_5_simpy_pow_signature():
    """Simpy.py - __pow__ method defined with correct signature."""
    module = reimport_module(MODULE)
    sig = inspect.signature(module.Simpy.__pow__)
    assert len(sig.parameters) == 2
    param_names = list(sig.parameters)
    param1 = param_names[1]
    assert sig.parameters[param1].annotation == 'Union[float, Simpy]' or sig.parameters[param1].annotation == 'Union[Simpy, float]'
    assert sig.return_annotation == 'Simpy'


@mark.weight(3)
def test_part_5_simpy_pow_functionality1():
    """Simpy.py - __pow__ method works with two Simpy objects."""
    module = reimport_module(MODULE)
    simp1 = module.Simpy([1.0, 5.0, 9.0])
    simp2: Simpy = module.Simpy([2.0, 3.0, 1.0])
    result: Simpy = simp1 ** simp2
    assert result.values == [1.0, 125.0, 9.0]


@mark.weight(3)
def test_part_5_simpy_pow_functionality2():
    """Simpy.py - __pow__ method works with one Simpy object and a float."""
    simp1 = Simpy([1.0, 5.0, 9.0])
    result = simp1 ** 2.0
    assert result.values == [1.0, 25.0, 81.0]


@mark.weight(2)
def test_part_7_simpy_eq_signature():
    """Simpy.py - __eq__ method defined with correct signature."""
    module = reimport_module(MODULE)
    sig = inspect.signature(module.Simpy.__eq__)
    assert len(sig.parameters) == 2
    param_names = list(sig.parameters)
    param1 = param_names[1]
    assert sig.parameters[param1].annotation == 'Union[float, Simpy]' or sig.parameters[param1].annotation == 'Union[Simpy, float]'
    assert sig.return_annotation == 'list[bool]'


@mark.weight(3)
def test_part_7_simpy_eq_functionality1():
    """Simpy.py - __eq__ method works with two Simpy objects."""
    module = reimport_module(MODULE)
    simp1 = module.Simpy([1.0, 5.0, 9.0])
    simp2: Simpy = module.Simpy([2.0, 3.0, 9.0])
    result = simp1 == simp2
    assert result == [False, False, True]


@mark.weight(3)
def test_part_7_simpy_eq_functionality2():
    """Simpy.py - __eq__ method works with one Simpy object and a float."""
    simp1 = Simpy([1.0, 2.0, 9.0])
    result = simp1 == 2.0
    assert result == [False, True, False]


@mark.weight(2)
def test_part_8_simpy_gt_signature():
    """Simpy.py - __gt__ method defined with correct signature."""
    module = reimport_module(MODULE)
    sig = inspect.signature(module.Simpy.__gt__)
    assert len(sig.parameters) == 2
    param_names = list(sig.parameters)
    param1 = param_names[1]
    assert sig.parameters[param1].annotation == 'Union[float, Simpy]' or sig.parameters[param1].annotation == 'Union[Simpy, float]'
    assert sig.return_annotation == 'list[bool]'


@mark.weight(3)
def test_part_8_simpy_gt_functionality1():
    """Simpy.py - __gt__ method works with two Simpy objects."""
    module = reimport_module(MODULE)
    simp1 = module.Simpy([1.0, 5.0, 9.0])
    simp2: Simpy = module.Simpy([2.0, 3.0, 9.0])
    result = simp1 > simp2
    assert result == [False, True, False]


@mark.weight(3)
def test_part_8_simpy_gt_functionality2():
    """Simpy.py - __gt__ method works with one Simpy object and a float."""
    simp1 = Simpy([1.0, 2.0, 9.0])
    result = simp1 > 2.0
    assert result == [False, False, True]


@mark.weight(2)
def test_part_9_simpy_getitem_signature():
    """Simpy.py - __getitem__ method defined with correct signature for part 9."""
    module = reimport_module(MODULE)
    sig = inspect.signature(module.Simpy.__getitem__)
    assert len(sig.parameters) == 2
    param_names = list(sig.parameters)
    param1 = param_names[1]
    assert sig.parameters[param1].annotation == 'int' or sig.parameters[param1].annotation == 'Union[int, list[bool]]' or sig.parameters[param1].annotation == 'Union[list[bool], int]'
    assert sig.return_annotation == 'float' or sig.return_annotation  == 'Union[float, Simpy]' or sig.return_annotation  == 'Union[Simpy, float]'


@mark.weight(3)
def test_part_9_simpy_getitem_functionality1():
    """Simpy.py - __getitem__ method works with simple usage."""
    module = reimport_module(MODULE)
    simp1 = module.Simpy([1.0, 5.0, 9.0])
    result = simp1[1]
    assert result == 5.0


@mark.weight(2)
def test_part_10_simpy_getitem_signature():
    """Simpy.py - __getitem__ method defined with correct signature for part 10."""
    module = reimport_module(MODULE)
    sig = inspect.signature(module.Simpy.__getitem__)
    assert len(sig.parameters) == 2
    param_names = list(sig.parameters)
    param1 = param_names[1]
    assert sig.parameters[param1].annotation == 'Union[int, list[bool]]' or sig.parameters[param1].annotation == 'Union[list[bool], int]'
    assert  sig.return_annotation == 'Union[float, Simpy]' or sig.return_annotation  == 'Union[Simpy, float]'


@mark.weight(3)
def test_part_10_simpy_getitem_functionality1():
    """Simpy.py - __getitem__ method works with filtering usage."""
    module = reimport_module(MODULE)
    simp1 = module.Simpy([1.0, 2.0, 5.0, 9.0])
    result = simp1[simp1 > 4.0]
    assert result.values == [5.0, 9.0]