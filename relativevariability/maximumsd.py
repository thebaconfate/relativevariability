import math
from typing import Union

from relativevariability.maximumvar import maximum_var


def maximum_sd(data: list[Union[int, float]]) -> float:
    return math.sqrt(maximum_var(data))
