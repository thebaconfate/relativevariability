from relativevariability import maximum_var
import pytest


def test_maxvar():
    assert maximum_var([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == pytest.approx(22.5)


def test_maxvar_1():
    assert maximum_var([0, 1]) == pytest.approx(0.5)

def test_maxvar_negs():
    assert maximum_var([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == pytest.approx(22.5)

def test_maxvar_negs_unordered():
    assert maximum_var([-1, 6, 8, -6, -10, 9, 2, 6, 2]) == pytest.approx(84.69444)