from relativevariability import ipr
import pytest


def test_ipr():
    data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert ipr(data_list, 0, 1) == 9
    assert ipr(data_list, 0.1, 1) == 9
    assert ipr(data_list, 0.2, 1) == 8
    assert ipr(data_list, 0.3, 1) == 7
    assert ipr(data_list, 0.4, 1) == 6
    assert ipr(data_list, 0.5, 1) == 5
    assert ipr(data_list, 0.6, 1) == 4
    assert ipr(data_list, 0.7, 1) == 3
    assert ipr(data_list, 0.8, 1) == 2
    assert ipr(data_list, 0.9, 1) == 1
    assert ipr(data_list, 1, 1) == 0


def test_ipr_inverted_percentiles():
    data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert ipr(data_list, 1, 0) == 9
    assert ipr(data_list, 1, 0.1) == 9
    assert ipr(data_list, 1, 0.2) == 8
    assert ipr(data_list, 1, 0.3) == 7
    assert ipr(data_list, 1, 0.4) == 6
    assert ipr(data_list, 1, 0.5) == 5
    assert ipr(data_list, 1, 0.6) == 4
    assert ipr(data_list, 1, 0.7) == 3
    assert ipr(data_list, 1, 0.8) == 2
    assert ipr(data_list, 1, 0.9) == 1
    assert ipr(data_list, 1, 1) == 0


def test_ipr_fail():
    with pytest.raises(ValueError):
        ipr(data_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], percentile_1=-1, percentile_2=1)
