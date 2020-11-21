import os
import click
import importlib
from common.problem import Problem
from config import conf


def msgbox(msg: str, color: str):
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


def run(p_num: int, test_case_num: int = -1):
    msgbox(f'第{p_num}道题', color='white')
    lib = importlib.import_module(f'problems.s{p_num}')
    solution = lib.Solution(os.path.join(conf.root_dir, 'samples', f's{p_num}.json'))
    solution.validate(test_case_num)


def test(file: str, test_case_num: int = -1):
    filename = file.split('/')[-1].split('.')[0]
    p_num = filename[1:]
    if p_num.isdigit():
        run(p_num, test_case_num)
    else:
        raise ValueError(filename)
