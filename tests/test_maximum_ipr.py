import pytest
from relativevariability import maximum_ipr


def test_maximum_ipr():
    assert maximum_ipr(5, 0, 10, 8, 0.25, 0.75) == pytest.approx(4.848485)
