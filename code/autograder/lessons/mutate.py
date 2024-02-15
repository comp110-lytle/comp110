"""Mutating functions."""


__author__ = "720310785"


def manual_append(a: list[int], b: int) -> None:
    """Append."""
    a.append(b)
    
    
def double(a: list[int]) -> None:
    """Double."""
    i: int = 0
    while i < len(a):
        a[i] *= 2
        i += 1
        
        