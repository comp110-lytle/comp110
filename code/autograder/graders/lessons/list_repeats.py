"""remove_repeats practice CQ."""

__author__ = "Viktorya Hunanyan vhunany@unc.edu"

MODULE = "lessons.list_repeats"

def remove_repeats(inp_list: list[int]) -> None: 
    """Mutates inp_list to remove any repeating numbers.
    
    Args:
        inp_list: An arbitrary list of numbers.

    Returns:
        Should not return anything.

    Example Usage:
        a: list[int] = [4, 8, 9, 4, 2, 2, 0, 9, 7, 10]
        remove_repeats(a) return None
        print(a) a (inp_list) should be modifyied to [4, 8, 9, 2, 0, 7, 10]
    """
    idx: int = 0
    while idx < len(inp_list):  # iterate through the list
        # iterate through each number and compare
        comparing_num: int = inp_list[idx]
        iter_idx: int = idx + 1  # to avoid looping over the same zeroth idx
        while iter_idx < len(inp_list):
            if comparing_num == inp_list[iter_idx]:
                inp_list.pop(iter_idx)  # pop decreases the size of the inp_list and indices are changed
            else: 
                iter_idx += 1  # pop already allows for iteration so don't increase idx or you will jump over an index
        idx += 1

    return None


if __name__ == "__main__":
    remove_repeats([1, 2, 3])
