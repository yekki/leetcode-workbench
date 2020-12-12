import os
import click
import importlib
import time
from functools import wraps
from common.problem import Problem
from typing import List


def msgbox(msg: str, color: str) -> None:
    length = 60
    click.secho('*' * length, fg=color)
    n = ((length - len(msg)) - 1) // 2
    click.secho(' ' * n + msg + ' ' * n, fg=color)
    click.secho('*' * length, fg=color)


def get_modules(package="."):
    modules = []
    files = os.listdir(package)

    for file in files:
        if not file.startswith("__"):
            name, ext = os.path.splitext(file)
            modules.append(name)

    return modules


def _get_num(filepath: str) -> int:
    p_num = filepath.split('/')[-1].split('.')[0][1:]
    if p_num.isdigit():
        return int(p_num)
    else:
        raise ValueError(filepath)


def run(sample_file: str, test_case_num: int = -1):
    p_num = _get_num(sample_file)
    msgbox(f'第{p_num}道题', color='blue')
    lib = importlib.import_module(f'problems.s{p_num}')
    solution = lib.Solution(sample_file)
    solution.validate(test_case_num)


def test(py_filepath: str, test_case_num: int = -1):
    p_num = _get_num(py_filepath)
    sample_file = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(py_filepath))), "samples",
                               f's{p_num}.json')
    run(sample_file, test_case_num)


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
