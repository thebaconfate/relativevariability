from relativevariability import rmssd

def test_rmssd():
    assert rmssd([1, 2, 3, 4, 5]) == 1
    assert rmssd([2,4,6,8,10,12,14,16,18,20]) == 2