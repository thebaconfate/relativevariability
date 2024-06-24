from typing import Union
from statistics import stdev, mean
from maximumvar import 


def relative_sd(data: list[Union[int, float]]) -> float:
    """Calculate the relative standard deviation of a list of data. Returns the standard deviation divided by the mean."""
    data_mean: float = mean(data)
    data_stdev: float = stdev(data)
    max_var = 
    return data_stdev / data_mean