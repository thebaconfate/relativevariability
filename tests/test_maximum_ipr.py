import pytest
from relativevariability import maximum_ipr


def test_maximum_ipr():
    assert maximum_ipr(5, 0, 10, 8, 0.25, 0.75) == pytest.approx(4.848485)

def test_mean_equals_min():
    assert maximum_ipr(1, 1, 1, 10, 0.25, 0.75) == pytest.approx(0)

def test_maximum_with_higher_abs_min_than_max_ipr():
    assert maximum_ipr(5, -11, 10, 8, 0.25, 0.75) == pytest.approx(4.848485)