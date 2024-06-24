from relativevariability import data_range
import pytest


def test_range():
    assert data_range([1, 2, 3, 4, 5]) == 4
    assert data_range([110, 10, 20, 50, 200, 100, 900, 500]) == 890


def test_range_error():
    with pytest.raises(ValueError):
        data_range([1])
    with pytest.raises(ValueError):
        data_range([])
