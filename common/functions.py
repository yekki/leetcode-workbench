import os, time
from functools import wraps
from typing import List
from click import style
from importlib import import_module
from .constants import PROBLEMS_PATH
from .renderer import RenderType, Renderer


def error(msg):
    print(style(msg, fg='red'))
    os._exit()


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
    if l1 is None or l2 is None:
        return False

    return l1.sort() == l2.sort()


def exec_template_methods(problem_no: int, function_list: list, param_list: list) -> List:
    lib = import_module(f'problems.n{problem_no}.solution')
    inst = eval(f'lib.Solution.{function_list[0]}')(*param_list[0])
    result = [None]
    for i, f in enumerate(function_list[1:]):
        func = getattr(inst, f)
        result.append(func(*param_list[1:][i]))

    return result


def get_problem_no(filepath: str):
    if filepath is None:
        error(f'错误文件名:{filepath}')

    problem_no = os.path.dirname(filepath).split('/')[-1][1:]

    try:
        problem_no = int(problem_no)
    except:
        error(f'错误文件名:{filepath}')

    return problem_no


def get_solution_clazz(filepath: str):
    problem_no = get_problem_no(filepath)
    return getattr(import_module(f'problems.n{problem_no}.solution'), 'Solution')


def create_solution_inst(filepath: str, render_type: RenderType):
    clazz = get_solution_clazz(filepath)
    problem_no = get_problem_no(filepath)
    sample_file = os.path.join(PROBLEMS_PATH, f"n{problem_no}", 'samples.json')
    inst = clazz(sample_file, renderer=Renderer(problem_no=problem_no, render_type=render_type))
    return inst
