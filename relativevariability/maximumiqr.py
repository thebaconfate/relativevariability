import math

from relativevariability.maximumipr import maximum_ipr


def maximum_iqr(
    data_mean: int | float, data_min: int | float, data_max: int | float, data_len: int
) -> float:
    """Calculate the maximum Interquartile Range (IQR) of a list of data. Returns the maximum possible value of the Interquartile Range."""
    percentile_1: int = math.floor(0.25 * data_len)
    percentile_2: int = math.floor(0.75 * data_len)
    return maximum_ipr(
        data_mean, data_min, data_max, data_len, percentile_1, percentile_2
    )
