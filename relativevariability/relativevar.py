import statistics
from typing import Union

from relativevariability.maximumvar import maximum_var


def relative_var(data: list[Union[int, float]]) -> float:
    """Calculate the relative variance of a list of data. Returns the variance divided by the mean."""
    data_var: float = statistics.variance(data)
    max_var: float = maximum_var(data)
    return data_var / max_var
