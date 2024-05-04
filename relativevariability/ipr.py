from typing import Union
import math


def ipr(
    data_list: list[Union[int, float]], percentile_1: float, percentile_2: float
) -> float:
    """Calculate the Interpercentile Range (IPR) of a list of data. Returns value at percentile_2 minus value at percentile_1. Swaps percentiles if percentile_1 > percentile_2. Raises ValueError if percentiles are not between 0 and 1."""
    if percentile_1 < 0 or percentile_1 > 1 or percentile_2 < 0 or percentile_2 > 1:
        raise ValueError("Percentile values must be between 0 and 1.")
    if percentile_1 > percentile_2:
        tmp: float = percentile_1
        percentile_1 = percentile_2
        percentile_2 = tmp
    data_len: int = len(data_list)
    percentile_1_idx: int = max(0, math.ceil(percentile_1 * data_len) - 1)
    percentile_2_idx: int = max(0, math.ceil(percentile_2 * data_len) - 1)
    sorted_data: list[Union[int, float]] = sorted(data_list)
    return sorted_data[percentile_2_idx] - sorted_data[percentile_1_idx]
