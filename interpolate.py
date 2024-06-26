from concurrent.futures import thread
import datetime
import statistics
from scipy.optimize import minimize
import math
import random
import sys
import multiprocessing


def interpolate(data, margin=True):
    data_max: int | float = max(data)
    data_min: int | float = min(data)
    data_mean: float = statistics.mean(data)
    data_len: int = len(data)
    if data_mean == data_min or data_mean == data_max:
        raise ValueError("data_mean cannot be equal to data_min or data_max")
    if abs(data_min) > abs(data_max):
        tmp: int | float = data_min
        data_min = data_max
        data_max = tmp
    return (data_len * data_mean - data_len * data_min) / (data_max - data_min)


constraints = [{"type": "eq", "fun": lambda x: interpolate(x)}]


def threaded_attempt(counter, lock, stop, stop_lock, res):
    while True:
        x0 = [random.uniform(-sys.maxsize, sys.maxsize) for _ in range(3)]
        result = minimize(
            interpolate,
            x0,
            constraints=constraints,
            method="SLSQP",
        )
        with lock:
            counter.value += 1
            if counter.value % 100_000 == 0:
                print("counter", counter.value)
        with stop_lock:
            if interpolate(result.x) < 1:
                stop.value = True
                for r in result.x:
                    res.append(r)
                print("interpolate", interpolate(result.x, False))
                break
            elif stop.value:
                break


if __name__ == "__main__":
    multiprocessing.freeze_support()
    counter = multiprocessing.Value("i", 0)
    lock = multiprocessing.Lock()
    stop = multiprocessing.Value("b", False)
    stop_lock = multiprocessing.Lock()
    res = multiprocessing.Array("f", [])
    threads = [
        multiprocessing.Process(
            target=threaded_attempt, args=(counter, lock, stop, stop_lock, res)
        )
        for _ in range(12)
    ]
    for i in threads:
        i.start()
    for i in threads:
        i.join()
    print("res", res)
    print("ctr", counter.value)
