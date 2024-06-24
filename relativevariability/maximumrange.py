from relativevariability.maximumipr import maximum_ipr

# TODO: confirm this works and write tests

def maximum_range(data_mean, data_min, data_max, data_len):
    """Calculate the maximum range of a list of data. Returns the maximum possible value of the range."""
    return maximum_ipr(data_mean, data_min, data_max, data_len, 1, data_len)
