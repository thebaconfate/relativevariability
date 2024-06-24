import math
from typing import Union

from relativevariability.maximumvar import maximum_var
# TODO: confirm this works and write tests


def maximum_sd(data: list[Union[int, float]]) -> float:
    return math.sqrt(maximum_var(data))
