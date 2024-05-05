from relativevariability import maxmssdgetn
import statistics


def test_maxmssdgetn_mean_equals_min():
    assert maxmssdgetn(1, 50, 1, 2) == {"n_min": 50, "n_max": 0, "n_middle": 0, "m": 0}


def test_maxmssdgetn_mean_equals_max():
    assert maxmssdgetn(50, 50, 1, 50) == {"n_min": 0, "n_max": 50, "n_middle": 0, "m": 0}


def test_maxmssdgetn():
    test_data = [1, 2, 3, 4, 5]
    assert maxmssdgetn(
        statistics.mean(test_data), len(test_data), min(test_data), max(test_data)
    ) == {"n_min": 2, "n_max": 2, "n_middle": 1, "m": 3}
