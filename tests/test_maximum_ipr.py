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
        -8.99558082e07,
        -1.04134412e08,
        -1.04134411e08,
        -1.04134410e08,
        -1.04134409e08,
        -1.04134408e08,
        -3.93571899e07,
        -1.12862539e08,
        -1.13954509e08,
        -1.13548355e08,
    ]
    assert maximum_ipr(
        statistics.mean(vct),
        min(vct),
        max(vct),
        len(vct),
        0.25 * len(vct),
        0.75 * len(vct),
    ) == pytest.approx(59677856)


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
