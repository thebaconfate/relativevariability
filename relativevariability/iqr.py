from typing import Union
from relativevariability.ipr import ipr


def iqr(data: list[Union[int, float]]) -> float:
    """Calculate the Interquartile Range (IQR) of a list of data. Returns value at third quartile minus value at first quartile."""
    first_quartile = 0.25
    third_quartile = 0.75
    return ipr(data, first_quartile, third_quartile)
