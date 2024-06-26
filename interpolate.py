import statistics
from scipy.optimize import minimize
import math


def interpolate(x):
    _length = len(x)
    _min = min(x)
    _max = max(x)
    _p1 = math.floor(0.25 * _length)
    _p2 = math.floor(0.75 * _length)
    _mean = statistics.mean(x)
    if _mean == _min or _mean == _max:
        raise ValueError("Mean is equal to min or max")
    if abs(_min) > abs(_max):
        temp = -_min
        _min = -_max
        _max = temp
        _mean = -_mean
    lhs = _length * _mean
    rhs = (_p2 - 1) * _min + (_length - _p2 + 1) * _max
    return lhs - rhs


def interpolate2(x):
    _length = len(x)
    _min = min(x)
    _max = max(x)
    _p1 = math.floor(0.25 * _length)
    _p2 = math.floor(0.75 * _length)
    _mean = statistics.mean(x)
    if _mean == _min or _mean == _max:
        raise ValueError("Mean is equal to min or max")
    if abs(_min) > abs(_max):
        temp = -_min
        _min = -_max
        _max = temp
        _mean = -_mean
    lhs = _length * _mean
    rhs = _p1 * _min + (_length - _p1) * _max
    return lhs - (rhs + 1e-6)


constraints = [
    {"type": "ineq", "fun": lambda x: interpolate(x)},
    {"type": "eq", "fun": lambda x: interpolate2(x)},
]

x0 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = minimize(
    sum, x0, constraints=constraints, method="SLSQP", options={"disp": True}
)

print(result.x)
print("interpolate", interpolate(result.x))
print("interpolate2", interpolate2(result.x))
