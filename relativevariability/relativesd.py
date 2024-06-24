import math
from typing import Union
from statistics import stdev

from relativevariability.maximumvar import maximum_var


def relative_std(data: list[Union[int, float]]) -> float:
    """Calculate the relative standard deviation of a list of data. Returns the standard deviation divided by the mean."""
    data_stdev: float = stdev(data)
    max_var: float = maximum_var(data)
    max_std: float = math.sqrt(max_var)
    return data_stdev / max_std
