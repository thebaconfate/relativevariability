from typing import Union


def mssd_parts(x_parts: list[list[Union[int, float]]]) -> dict[str, Union[int, float]]:
    n: int = 0
    output: int = 0
    for x_part in x_parts:
        len_x_part: int = len(x_part)
        if len_x_part > 1:
            for num in range(len_x_part - 1):
                n += 1
                output += (x_part[num + 1] - x_part[num]) ** 2
    return {"mssdSum": output, "n": n, "mssdMean": output / n}
