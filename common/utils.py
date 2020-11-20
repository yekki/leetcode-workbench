import sys
import importlib
import os
import click

def help():
    print('''
    使用说明：
    ./main.py [n/all]
    n: n为正整数，代表测试第几道题
    all: 测试所有题
    ''')
    exit(0)

def msgbox(msg: str, color:str):
    length = 60
    click.secho('*' * length, fg=color)
    n = ((length - len(msg)) - 1)// 2
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

def _run(n: str):
    msgbox(f'第{n}道题', color='white')
    lib = importlib.import_module(f'problems.s{n}')
    solution = lib.Solution(os.path.join(os.getcwd(), 'samples', f's{n}.json'))
    solution.validate()

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