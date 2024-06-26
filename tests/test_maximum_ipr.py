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
        -1174559.36404975,
        -1173890.54863387,
        -1173042.80477426,
        -1174782.2274112,
        -1175053.33452611,
        -1174971.7337945,
        -1174968.8788993,
        -1168536.42858289,
        -1165737.48082844,
        -1175053.3337175,
    ]
    assert maximum_ipr(
        statistics.mean(v), min(v), max(v), len(v), 0.25, 0.75
    ) == pytest.approx(7143.544)
