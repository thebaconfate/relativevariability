import math
from typing import Union
from relativevariability import mssd


def rmssd(data: list[Union[int, float]]) -> float:
    """Calculate the Root Mean Squared Successive Differences (RMSSD) of a list of data. Returns the square root of the average of the squared differences between successive data points."""
    data_len: int = len(data)
    if data_len < 2:
        raise ValueError("Data list must have at least 2 elements.")
    return math.sqrt(mssd(data))
