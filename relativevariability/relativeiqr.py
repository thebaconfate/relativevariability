import math
import statistics
from typing import Union

from relativevariability import iqr
from relativevariability.maximumipr import maximum_ipr


def relative_iqr(data: list[Union[int, float]]) -> float:
    """Calculate the relative Interquartile Range (IQR) of a list of data. Returns the Interquartile Range divided by the maximum possible value of the Interquartile Range."""
    data_iqr: float = iqr(data)
    data_len: int = len(data)
    max_ipr: float = maximum_ipr(
        statistics.mean(data),
        min(data),
        max(data),
        data_len,
        math.floor(0.25 * data_len),
        math.floor(0.75 * data_len),
    )
    return data_iqr / max_ipr
