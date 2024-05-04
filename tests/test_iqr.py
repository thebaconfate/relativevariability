from relativevariability import ipr, iqr


def test_iqr():
    data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert iqr(data_list) == ipr(data_list, 0.25, 0.75)
