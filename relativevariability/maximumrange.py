from relativevariability.maximumipr import maximum_ipr


def maximum_range(data_mean, data_min, data_max, data_len):
    return maximum_ipr(data_mean, data_min, data_max, data_len, 1, data_len)
