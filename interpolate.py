from scipy.optimize import minimize


def interpolate(lst):
    _p1 = 0.25
    _p2 = 0.75
    _length = len(lst)
    _mean = sum(lst) / _length
    _min = min(lst)
    _max = max(lst)

    if _mean == _min or _mean == _max:
        raise Exception("mean == min or mean == max")
    if abs(_min) > abs(_max):
        temp = -_min
        _min = -_max
        _max = temp
        _mean = -_mean
    lhs = _length * _mean
    rhs = (_p2 - 1) * _min + (_length - _p2 + 1) * _max
    return lhs - rhs + 0.0001e-100


constraints = [{"type": "eq", "fun": interpolate}]

res = minimize(
    sum,
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    options={"disp": True, "maxiter": 10000},
    constraints=constraints,
    method="SLSQP",
)

print(res.x)
