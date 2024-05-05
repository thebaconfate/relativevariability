from relativevariability import range
import pytest

def test_range():
    assert range([1, 2, 3, 4, 5]) == 4
    assert range([110, 10, 20, 50, 200, 100, 900, 500]) == 890

def test_range_error():
    with pytest.raises(ValueError):
        range([1])
        range([])