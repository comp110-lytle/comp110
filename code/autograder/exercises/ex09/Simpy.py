"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "7305574684"


class Simpy:
    """Create Simpy class."""

    values: list[float]

    # TODO: Your constructor and methods will go here.
    
    def __init__(self, input_values: list[float]):
        """Construct Simpy object."""
        self.values = input_values

    def __str__(self) -> str:
        """Convert Simpy object to str representation."""
        return f"Simpy({self.values})"
    
    def fill(self, fill_value: float, num_values: int) -> None:
        """Fill Simpy object values with specific number of repeat values."""
        self.values = []
        for idx in range(0, num_values):
            self.values.append(fill_value)

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill values attribute with range of values."""
        assert step != 0.0
        total: float = start
        if step > 0:
            while total < stop:
                self.values.append(total)
                total += step
        if step < 0:
            while total > stop:
                self.values.append(total)
                total += step

    def sum(self) -> float:
        """Compute and return sum of all items in values attribute."""
        total: float = 0.0
        for item in self.values:
            total += item
        return total
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overload addition."""
        if type(rhs) == Simpy:
            assert len(self.values) == len(rhs.values)
            new_simpy: Simpy = Simpy([])
            idx: int = 0
            while idx < len(self.values):
                new_simpy_value: float = self.values[idx] + rhs.values[idx]
                new_simpy.values.append(new_simpy_value)
                idx += 1
        if type(rhs) == float:
            new_simpy: Simpy = Simpy([])
            idx: int = 0
            while idx < len(self.values):
                new_simpy_value: float = self.values[idx] + rhs
                new_simpy.values.append(new_simpy_value)
                idx += 1
        return new_simpy
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overload exponentiation."""
        if type(rhs) == Simpy:
            assert len(self.values) == len(rhs.values)
            new_simpy: Simpy = Simpy([])
            idx: int = 0
            while idx < len(self.values):
                new_simpy_value: float = self.values[idx] ** rhs.values[idx]
                new_simpy.values.append(new_simpy_value)
                idx += 1
        if type(rhs) == float:
            new_simpy: Simpy = Simpy([])
            idx: int = 0
            while idx < len(self.values):
                new_simpy_value: float = self.values[idx] ** rhs
                new_simpy.values.append(new_simpy_value)
                idx += 1
        return new_simpy
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overload equality."""
        if type(rhs) == Simpy:
            assert len(self.values) == len(rhs.values)
            new: list = []
            idx: int = 0
            while idx < len(self.values):
                if self.values[idx] == rhs.values[idx]:
                    new.append(True)
                    idx += 1
                else:
                    new.append(False)
                    idx += 1

        if type(rhs) == float:
            new: list = []
            idx: int = 0
            while idx < len(self.values):
                if self.values[idx] == rhs:
                    new.append(True)
                    idx += 1
                else:
                    new.append(False)
                    idx += 1
        return new
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overload greater than."""
        if type(rhs) == Simpy:
            assert len(self.values) == len(rhs.values)
            new: list = []
            idx: int = 0
            while idx < len(self.values):
                if self.values[idx] > rhs.values[idx]:
                    new.append(True)
                    idx += 1
                else:
                    new.append(False)
                    idx += 1

        if type(rhs) == float:
            new: list = []
            idx: int = 0
            while idx < len(self.values):
                if self.values[idx] > rhs:
                    new.append(True)
                    idx += 1
                else:
                    new.append(False)
                    idx += 1
        return new
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Overload subscription."""
        if type(rhs) == int:
            ret: float = self.values[rhs]
            return self.values[rhs]
        else:
            ret: Simpy = Simpy([])
            idx: int = 0
            while idx < len(rhs):
                if rhs[idx] is True:
                    ret.values.append(self.values[idx])
                idx += 1
        return ret
