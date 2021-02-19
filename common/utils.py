import time
from functools import wraps
from typing import List
import os


def get_modules(package="."):
    modules = []
    files = os.listdir(package)

    for file in files:
        if not file.startswith("__"):
            name, ext = os.path.splitext(file)
            modules.append(name)

    return modules


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        gap = (end - start) * 1000 * 1000
        print(f'{func.__name__} 耗时: {gap:.2f} 微秒')
        return ret

    return wrapper


def list_eq(l1: List, l2: List) -> bool:
    if l1 == l2:
        return True
    else:
        for a in l1:
            if a not in l2:
                return False
        else:
            return True


def exec_template_methods(inst, function_list, param_list) -> List:
    result = [None]
    for i, f in enumerate(function_list[1:]):
        func = getattr(inst, f)
        result.append(func(*param_list[1:][i]))

    return result
