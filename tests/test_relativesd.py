from relativevariability import relative_sd
import pytest

def test_relative_sd():
    assert relative_sd([1, 2, 3, 4, 5, 10]) == pytest.approx(0.7030842)