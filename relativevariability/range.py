from typing import Union


def range(data: list[Union[int, float]]) -> float:
    """Calculate the range of a list of data. Returns the difference between the maximum and minimum values."""
    if len(data) < 2:
        raise ValueError("Data list must have at least 2 elements.")
    return max(data) - min(data)
