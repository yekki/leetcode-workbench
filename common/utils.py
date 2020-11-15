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
        click.secho(f'第{n}道题测试通过！', fg='blue')
    else:
        click.secho('第{n}道题不测试通过！', fg='red')


def help() -> None:
    print('''
    使用说明：
    ./main.py [n/all]
    n: n为正整数，代表测试第几道题
    all: 测试所有题
    ''')
    exit(0)


def parse_cmd_args() -> int:
    if len(sys.argv) < 2:
        help()

    num = sys.argv[1]

    if num == 'all':
        return -1 # -1 代表all

    if num.isnumeric():
        num = int(num)
    else:
        help()

    return num


def get_modules(package="."):
    modules = []
    files = os.listdir(package)

    for file in files:
        if not file.startswith("__"):
            name, ext = os.path.splitext(file)
            modules.append(name)

    return modules


@timer
def _run(n: int) -> None:
    lib = importlib.import_module(f'problems.s{n}')
    s = lib.Solution(os.path.join(os.getcwd(), 'samples', f's{n}.json'))
    print_result(n, s.validate())


def run():
    ret = parse_cmd_args()

    if ret == -1:
        modules = get_modules('problems')
        for m in modules:
            _run(int(m[1:]))
    else:
        _run(ret)