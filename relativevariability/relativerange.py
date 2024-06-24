import statistics
from typing import Union
from relativevariability.maximumipr import maximum_ipr
from relativevariability.range import data_range


def relative_range(data: list[Union[int, float]]) -> float:
    d_range: float = data_range(data)
    data_len: int = len(data)
    max_ipr: float = maximum_ipr(
        statistics.mean(data), min(data), max(data), data_len, 1, data_len
    )
    return d_range / max_ipr
