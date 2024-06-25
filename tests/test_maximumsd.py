import pytest
from relativevariability import maximum_sd


def test_maximum_sd():
    assert maximum_sd([1, 2, 3, 4, 5, 10]) == pytest.approx(4.535048)
