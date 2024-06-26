import statistics
import pytest
from relativevariability import maximum_ipr


def test_maximum_ipr():
    assert maximum_ipr(5, 0, 10, 8, 0.25, 0.75) == pytest.approx(4.848485)


def test_mean_equals_min():
    assert maximum_ipr(1, 1, 10, 10, 0.25, 0.75) == pytest.approx(0)


def test_mean_equals_max():
    assert maximum_ipr(10, 1, 10, 10, 0.25, 0.75) == pytest.approx(0)


def test_abs_min_greater_than_abs_max():
    assert maximum_ipr(5, -20, 10, 10, 0.25, 0.75) == pytest.approx(4.878049)


def test_case2():
    v = [
        -1204988.6026813,
        -1204988.60313556,
        -1204988.6037683,
        -1204988.60367774,
        -1204988.60367732,
        -1204988.60376828,
        -1204988.60362847,
        -1204988.60356019,
        -1204988.60338437,
        -1204988.60340467,
    ]
    assert maximum_ipr(
        statistics.mean(v), min(v), max(v), len(v), 0.25, 0.75
    ) == pytest.approx(0.0007681172)
