from typing import Union
import math


def ipr(
    data_list: list[Union[int, float]], percentile_1: float, percentile_2: float
) -> float:
    if percentile_1 < 0 or percentile_1 > 1 or percentile_2 < 0 or percentile_2 > 1:
        raise ValueError("Percentile values must be between 0 and 1.")
    if percentile_1 > percentile_2:
        tmp: float = percentile_1
        percentile_1 = percentile_2
        percentile_2 = tmp
    data_len: int = len(data_list)
    percentile_1_idx: int = math.ceil(percentile_1 * data_len)
    percentile_2_idx: int = math.ceil(percentile_2 * data_len)
    percentile_1_idx = max(0, percentile_1_idx - 1) if percentile_1_idx > 0 else 0
    percentile_2_idx = max(0, percentile_2_idx - 1) if percentile_2_idx > 0 else 0
    print(f"percentile_1_idx: {data_list[percentile_1_idx]}")
    print(f"percentile_2_idx: {data_list[percentile_2_idx]}")
    sorted_data: list[Union[int, float]] = sorted(data_list)
    return sorted_data[percentile_2_idx] - sorted_data[percentile_1_idx]
