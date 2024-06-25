import numpy as np
from scipy.optimize import minimize


# Function to compute LHS and RHS
def compute_lhs_rhs(args):
    _mean, _min, _max, _length, p1, p2 = args
    lhs = _length * _mean
    rhs = (p1 - 1) * _min + (_length - p1 + 1) * _max
    return lhs, rhs


# Main constraint function: LHS should be >= RHS
def main_constraint(args):
    lhs, rhs = compute_lhs_rhs(args)
    return lhs - rhs  # We want this to be >= 0


# Function to adjust min, max, and mean if necessary
def adjust_values(args):
    _mean, _min, _max, _length, p1, p2 = args
    if abs(_min) > abs(_max):
        _min, _max = _max * -1, _min * -1
        _mean = _mean * -1
    return [_mean, _min, _max, _length, p1, p2]


# Additional constraints
def additional_constraints(args):
    _mean, _min, _max, _length, p1, p2 = args
    adjusted_args = adjust_values(args)
    _mean_adj, _min_adj, _max_adj, _length_adj, p1_adj, p2_adj = adjusted_args
    return [
        _mean_adj - _min_adj - 1e-6,  # _mean > _min (adding a small tolerance)
        _max_adj - _mean_adj - 1e-6,  # _mean < _max (adding a small tolerance)
        _length_adj
        - np.round(_length_adj),  # _length should be an integer (rounding workaround)
        _length_adj - 2,  # _length >= 2
        p1_adj - 0,  # p1 >= 0
        1 - p1_adj,  # p1 <= 1
        p2_adj - 0,  # p2 >= 0
        1 - p2_adj,  # p2 <= 1
        p2_adj - p1_adj,  # p2 >= p1
    ]


# Objective function (simple, as we only need to satisfy the constraints)
def objective_function(args):
    return np.sum(args)  # Can be any function that guides the optimization


# Initial guess for the arguments
initial_guess = [1, 1, 1, 2, 0.5, 0.5]

# Define bounds for the variables if needed (optional)
bounds = [
    (None, None),  # _mean
    (None, None),  # _min
    (None, None),  # _max
    (2, None),  # _length should be >= 2
    (0, 1),  # p1
    (0, 1),  # p2
]

# Define the constraint dictionary
constraint_dict = [
    {"type": "ineq", "fun": main_constraint},
    {
        "type": "ineq",
        "fun": lambda args: additional_constraints(adjust_values(args))[0],
    },  # _mean > _min
    {
        "type": "ineq",
        "fun": lambda args: additional_constraints(adjust_values(args))[1],
    },  # _mean < _max
    {
        "type": "eq",
        "fun": lambda args: additional_constraints(adjust_values(args))[2],
    },  # _length should be an integer (rounding workaround)
    {
        "type": "ineq",
        "fun": lambda args: additional_constraints(adjust_values(args))[3],
    },  # _length >= 2
    {
        "type": "ineq",
        "fun": lambda args: additional_constraints(adjust_values(args))[4],
    },  # p1 >= 0
    {
        "type": "ineq",
        "fun": lambda args: additional_constraints(adjust_values(args))[5],
    },  # p1 <= 1
    {
        "type": "ineq",
        "fun": lambda args: additional_constraints(adjust_values(args))[6],
    },  # p2 >= 0
    {
        "type": "ineq",
        "fun": lambda args: additional_constraints(adjust_values(args))[7],
    },  # p2 <= 1
    {
        "type": "ineq",
        "fun": lambda args: additional_constraints(adjust_values(args))[8],
    },  # p2 >= p1
]

# Minimize the objective function with the constraints
result = minimize(
    objective_function,
    initial_guess,
    bounds=bounds,
    constraints=constraint_dict,
    method="SLSQP",
)

# Optimal arguments
optimal_arguments = result.x  # Ensure _length is an integer
print(f"Optimal arguments: {optimal_arguments}")
lhs, rhs = compute_lhs_rhs(optimal_arguments)
print(f"LHS: {lhs}, RHS: {rhs}")
print(f"Function value at optimal arguments: {lhs - rhs}")
