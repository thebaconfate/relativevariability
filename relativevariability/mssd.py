from typing import Union
import numpy as np


def mssd(data_list: list[Union[int, float]]) -> float:
    """Calculate the Mean Squared Successive Differences (MSSD) of a list of data. Returns the average of the squared differences between successive data points."""
    if isinstance(data_list, list):
        data_list = [x if isinstance(x, (int, float)) else np.nan for x in data_list]
    elif isinstance(data_list, np.ndarray):
        data_list = [
            x if isinstance(x, (int, float)) else np.nan for x in data_list.tolist()
        ]
    else:
        raise TypeError("Data must be a list or numpy array with numbers")
    diffs = np.diff(np.array(data_list))
    diffs = diffs[~np.isnan(diffs)]
    return np.mean(diffs**2)
