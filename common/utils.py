from functools import wraps
import time
import click
import sys
import importlib
import os


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        gap = (end - start) * 1000 * 1000
        click.secho('耗时: %sμs' % gap, fg='white')
    return wrapper


def print_result(n, result):
    if result:
        click.secho(f'第{n}道题测试通过！', fg='green')
    else:
        click.secho(f'第{n}道题不测试通过！', fg='red')


def help() -> None:
    print('''
    使用说明：
    ./main.py [n/all]
    n: n为正整数，代表测试第几道题
    all: 测试所有题
    ''')
    exit(0)


def get_modules(package="."):
    modules = []
    files = os.listdir(package)

    for file in files:
        if not file.startswith("__"):
            name, ext = os.path.splitext(file)
            modules.append(name)

    return modules

#TODO: timer should be div by the count of tests
@timer
def _run(n: str) -> None:
    lib = importlib.import_module(f'problems.s{n}')
    s = lib.Solution(os.path.join(os.getcwd(), 'samples', f's{n}.json'))
    print_result(n, s.validate())


def run():
    arg = sys.argv[1]

    if arg == 'all':
        modules = get_modules('problems')
        for m in modules:
            _run(m[1:])
    elif arg == 'help':
        help()
    else:
        _run(arg)