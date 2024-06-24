import math
from typing import Union


def max_mssd_get_n(
    data_mean: Union[int, float],
    data_len: Union[int, float],
    data_min: Union[int, float],
    data_max: Union[int, float],
) -> dict[str, Union[int, float]]:
    if data_mean == data_min:
        n_min: Union[int, float] = data_len
        n_max = 0
        n_middle = 0
        m = 0
    elif data_mean == data_max:
        n_max: Union[int, float] = data_len
        n_min = 0
        n_middle = 0
        m = 0
    else:
        n_max: Union[int, float] = math.floor(
            (data_len * data_mean - data_len * data_min) / (data_max - data_min)
        )
        n_min = data_len - (1 + n_max)
        if n_max == 0:
            data_max = 0
        n_middle = 1
        m: Union[int, float] = (
            data_len * data_mean - n_min * data_min - n_max * data_max
        )
    return {"n_min": n_min, "n_max": n_max, "n_middle": n_middle, "middle": m}
