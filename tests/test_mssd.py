import pytest

from relativevariability import mssd


def test_mssd():
    assert mssd([1, 2, 3, 4, 5]) == 1
    assert mssd([110, 10, 20, 50, 200, 100, 900, 500]) == 120500
    assert mssd([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 4


def test_mssd_error():
    with pytest.raises(ValueError):
        mssd([1])
        mssd([])
