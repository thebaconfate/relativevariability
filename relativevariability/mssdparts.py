from typing import Union


def mssd_parts(x_parts: list[list[Union[int, float]]]) -> dict[str, Union[int, float]]:
    """Calculate the mean sum of squared differences for each part of the data. Expects a list of vectors."""
    n: int = 0
    output: float = 0.0
    for i in range(len(x_parts)):
        if len(x_parts[i]) > 1:
            for j in range(len(x_parts[i]) - 1):
                output += (x_parts[i][j + 1] - x_parts[i][j]) ** 2
                n += 1
    return {"mssdSum": output, "numberOfDifs": n, "mssdMean": output / n}
