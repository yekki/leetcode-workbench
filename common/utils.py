from functools import wraps
from typing import List
from click import style
from importlib import import_module
import os, time
from .constants import PROBLEMS_PATH

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
    else:
        for a in l1:
            if a not in l2:
                return False
        else:
            return True

def exec_template_methods(p_num, function_list, param_list) -> List:

    lib = import_module(f'problems.n{p_num}.solution')
    inst = eval(f'lib.Solution.{function_list[0]}')(*param_list[0])
    result = [None]
    for i, f in enumerate(function_list[1:]):
        func = getattr(inst, f)
        result.append(func(*param_list[1:][i]))

    return result

def get_problem_no(filepath):
    problem_no = os.path.dirname(filepath).split('/')[-1][1:]

    if problem_no.isdigit():
        problem_no = int(problem_no)
    else:
        error(f'错误文件名:{filepath}')
    
    return problem_no

def get_solution_clazz(filepath):
    problem_no = get_problem_no(filepath)
    return getattr(import_module(f'problems.n{problem_no}.solution'), 'Solution')

def create_solution_inst(filepath):
    clazz = get_solution_clazz(filepath)
    problem_no = get_problem_no(filepath)
    sample_file = os.path.join(PROBLEMS_PATH, f"n{problem_no}", 'samples.json')
    inst = clazz(sample_file)
    return inst
