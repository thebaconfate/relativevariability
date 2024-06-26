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
    vct = [
        -44321.78599591,
        -44321.60904952,
        -44321.81134293,
        -44321.7241855,
        -44321.56522732,
        -44321.80898201,
        -44321.58418848,
        -44315.26797085,
        -44321.82650764,
        -44321.28162627,
    ]
    assert maximum_ipr(
        statistics.mean(vct),
        min(vct),
        max(vct),
        len(vct),
        0.01 * len(vct),
        0.99 * len(vct),
    ) == pytest.approx(6.558537)


def test_case3():
    vct = [
        -1.05691532e08,
        -1.05657153e08,
        -1.05691617e08,
        -1.05691616e08,
        -1.05691615e08,
        -1.05691614e08,
        -1.05691613e08,
        -1.05691607e08,
        -1.05691606e08,
        -1.05639786e08,
    ]
    assert maximum_ipr(
        statistics.mean(vct),
        min(vct),
        max(vct),
        len(vct),
        0.25 * len(vct),
        0.75 * len(vct),
    ) == pytest.approx(34564.4)
