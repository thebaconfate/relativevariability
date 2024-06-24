import math
import statistics
from typing import Union



def maximum_var(data: list[Union[int, float]]) -> float:
    """Calculate the maximum variability of a list of data. Returns the maximum value minus the minimum value."""
    data_max: int | float = max(data)
    data_min: int | float = min(data)
    data_mean: float = statistics.mean(data)
    data_len: int = len(data)
    if data_mean == data_min or data_mean == data_max:
        return 0
    if abs(data_min) > abs(data_max):
        tmp: int | float = data_min
        data_min = data_max
        data_max = tmp
    n_max: int = math.floor(
        (data_len * data_mean - data_len * data_min) / (data_max - data_min)
    )
    n_min: int = data_len - (1 + n_max)
    if n_max == 0:
        data_max = 0
    middle: float = data_len * data_mean - n_min * data_min - n_max * data_max
    max_var: float = (
        n_min * (data_min - data_mean) ** 2
        + n_max * (data_max - data_mean) ** 2
        + (data_mean - middle) ** 2
    ) / (data_len - 1)
    return max_var
