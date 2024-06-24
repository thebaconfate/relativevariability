from typing import Union


def most_least(to_use: list[Union[int, float]]) -> dict[str, int]:
    """Return the index of the most and least value in a list of two values."""
    if to_use[0] > to_use[1]:
        return {"whichMost": 0, "whichLeast": 1}
    else:
        return {"whichMost": 1, "whichLeast": 0}
