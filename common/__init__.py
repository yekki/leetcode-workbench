import os
import click
import importlib
import time
from functools import wraps
from common.problem import Problem
from typing import List


SOLUTION_T = '''from common import Problem


class Solution(Problem):

    def _validate(self, input, expected) -> tuple:
        result = self

        return result == expected, result


if __name__ == '__main__':
    Solution.test(__file__)

'''

SAMPLES_T = '''[
  {
    "input": "",
    "expected":""
  }
]
'''

def create_p(n):
    p = os.path.join(os.getcwd(), 'problems', f'n{n}')

    if not os.path.exists(p):
        os.mkdir(p)

    f = os.path.join(p, 'solution.py')
    if not os.path.exists(f):
        with open(f, mode='w', encoding='utf-8') as file:
            file.write(SOLUTION_T)

    f = os.path.join(p, 'samples.json')
    if not os.path.exists(f):
        with open(f, mode='w', encoding='utf-8') as file:
            file.write(SAMPLES_T)

    f = os.path.join(p, 'README.md')
    if not os.path.exists(f):
        with open(f, mode='w', encoding='utf-8') as file:
            file.write('## 解题思路')

    print(f'创建新题目：{p}')

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
    p_num = os.path.dirname(filepath).split('/')[-1][1:]
    if p_num.isdigit():
        return int(p_num)
    else:
        raise ValueError(filepath)


def run(sample_file: str, test_case_num: int = -1):
    p_num = _get_num(sample_file)
    msgbox(f'第{p_num}道题', color='blue')
    lib = importlib.import_module(f'problems.n{p_num}.solution')
    solution = lib.Solution(sample_file)
    solution.validate(test_case_num)


def test(py_filepath: str, test_case_num: int = -1):
    p_num = _get_num(py_filepath)
    sample_file = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(py_filepath))), f"n{p_num}",
                               'samples.json')
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
