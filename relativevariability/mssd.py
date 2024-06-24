import statistics
from typing import Union


def mssd(data_list: list[Union[int, float]]) -> float:
    """Calculate the Mean Squared Successive Differences (MSSD) of a list of data. Returns the average of the squared differences between successive data points."""
    data_len: int = len(data_list)
    if data_len < 2:
        raise ValueError("Data list must have at least 2 elements.")
    return statistics.mean(
        [(data_list[i] - data_list[i + 1]) ** 2 for i in range(data_len - 1)]
    )
