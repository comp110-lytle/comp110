"""Dictionary program for TA reference."""

__author__ = "730406615"


def invert(given: dict[str, str]) -> dict[str, str]:
    """Inverts key-value pairs."""
    new: dict[str, str] = dict()
    for key in given.keys():
        if given[key] in new:
            raise KeyError("There is a repeat value in input dictionary.")
        new[given[key]] = key
    return new


def favorite_color(given: dict[str, str]) -> str:
    """Find the most popular color value in a dictionary."""
    poll: dict[str, int] = dict()
    for key in given:
        if given[key] not in poll:
            poll[given[key]] = 0
        else:
            poll[given[key]] += 1

    favorite: str = list(poll.keys())[0]
    for key in poll:
        if poll[key] > poll[favorite]:
            favorite = key
    return favorite


def count(values: list[str]) -> dict[str, int]:
    """Get counts of each value."""
    counts: dict[str, int] = {}
    for value in values:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    return counts


def alphabetizer(alist: list[str]) -> dict[str, list[str]]:
    """Function takes in a list of words and then sorts them into a dict of list based on first letter."""
    result: dict[str, list[str]] = {}
    for item in alist:
        if item[0].lower() in result:
            result[item[0].lower()].append(item)
        else:
            result[item[0].lower()] = [item]
    return result


def update_attendance(adict: dict[str, list[str]], day: str, name: str) -> None:
    """Given dict, day, and name, adds name to corresponding day of attendance."""
    if day in adict:
        if name not in adict[day]:
            adict[day].append(name)
    else:
        adict[day] = [name]
