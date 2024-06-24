# TODO: confirm this works and write tests


def maximum_ipr(
    data_mean: int | float,
    data_min: int | float,
    data_max: int | float,
    data_len: int,
    percentile_1: int | float,
    percentile_2: int | float,
) -> float:
    """Calculate the maximum Interpercentile Range (IPR) of a list of data. Returns the maximum possible value of the Interpercentile Range."""
    if data_mean == data_min or data_mean == data_max:
        return 0
    if abs(data_min) > abs(data_max):
        temp: int | float = data_min
        data_min = data_max
        data_max = temp
    if (
        data_len * data_mean
        < (percentile_2 - 1) * data_min + (data_len - percentile_2 + 1) * data_max
    ):
        return data_len * (data_mean - data_min) / (data_len - percentile_2 + 1)
    elif (
        data_len * data_mean
        <= percentile_1 * data_min + (data_len - percentile_1) * data_max
    ):
        return data_max - data_min
    else:
        return data_len * (data_max - data_mean) / percentile_1
