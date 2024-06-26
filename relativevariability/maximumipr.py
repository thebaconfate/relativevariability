def maximum_ipr(
    data_mean: int | float,
    data_min: int | float,
    data_max: int | float,
    data_len: int,
    percentile_1: int | float,
    percentile_2: int | float,
) -> float:
    """Calculate the maximum Interpercentile Range (IPR) of a list of data. Returns the maximum possible value of the Interpercentile Range. Expects the mean of the data, the minimum of the data, the max of the data. The length of the data (which obviously must be a positive integer), and the two percentiles (which must be between 0 and 1)."""
    if data_mean == data_min or data_mean == data_max:
        return 0
    if abs(data_min) > abs(data_max):
        temp: int | float = -data_min
        data_min = -data_max
        data_max = temp
        data_mean = -data_mean
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
