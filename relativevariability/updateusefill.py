def update_use_fill(to_add_max_min, to_use, to_fill, i):
    # Adjust elements in toUse and toFill based on toAddMaxMin
    for j in range(len(to_add_max_min)):
        to_use[to_add_max_min[j]] -= 1
        to_fill[i] -= 1
    return {"to_use": to_use, "to_fill": to_fill}
