import statistics
import pytest
from relativevariability import maximum_ipr


def test_maximum_ipr():
    assert maximum_ipr(5, 0, 10, 8, 0.25, 0.75) == pytest.approx(4.848485)


def test_mean_equals_min():
    assert maximum_ipr(1, 1, 10, 10, 0.25, 0.75) == pytest.approx(0)


def test_mean_equals_max():
    assert maximum_ipr(10, 1, 10, 10, 0.25, 0.75) == pytest.approx(0)


def test_abs_min_greater_than_max():
    v = [3.04144133e15, 2.43315304e15, -5.47459440e15]
    assert maximum_ipr(
        statistics.mean(v), min(v), max(v), len(v), 0.25, 0.75
    ) == pytest.approx(2.807484e15)
