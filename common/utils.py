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


def _print_result(ret):
    if ret:
        click.secho('测试通过！', fg='blue')
    else:
        click.secho('测试不通过！', fg='red')


def _help() -> None:
    print('''
    使用说明：
    ./main.py [编号]
    ''')
    exit(0)


def _parse_cmd_args() -> int:
    if len(sys.argv) < 2:
        help()

    num = sys.argv[1]

    if num.isnumeric():
        num = int(num)
    else:
        help()

    return num


@timer
def run():
    num = _parse_cmd_args()
    lib = importlib.import_module(f'problems.s{num}')
    s = lib.Solution(os.path.join(os.getcwd(), 'samples', f's{num}.json'))
    _print_result(s.validate())