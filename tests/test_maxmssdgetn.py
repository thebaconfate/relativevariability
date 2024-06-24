from relativevariability import max_mssd_get_n
import statistics


def test_max_mssd_get_n_mean_equals_min():
    assert max_mssd_get_n(1, 50, 1, 2) == {"n_min": 50, "n_max": 0, "n_middle": 0, "middle": 0}


def test_max_mssd_get_n_mean_equals_max():
    assert max_mssd_get_n(50, 50, 1, 50) == {"n_min": 0, "n_max": 50, "n_middle": 0, "middle": 0}


def test_max_mssd_get_n():
    test_data: list[int] = [1, 2, 3, 4, 5]
    assert max_mssd_get_n(
        statistics.mean(test_data), len(test_data), min(test_data), max(test_data)
    ) == {"n_min": 2, "n_max": 2, "n_middle": 1, "middle": 3}
