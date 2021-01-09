import abc
import json
import time
import os
import importlib
from prettytable import PrettyTable
from copy import deepcopy
from click import style

PROBLEMS_PATH = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'problems')

TEMPLATE_SOLUTION = '''from common import Problem


class Solution(Problem):
    pass


if __name__ == '__main__':
    Solution.test(__file__)

'''

TEMPLATE_SAMPLES = '''[
  {
    "input": "",
    "expected":""
  }
]
'''

def eq(a, b):
    return a == b

class Problem(metaclass=abc.ABCMeta):
    def __init__(self, json_path, eq_func=eq):
        self.eq = eq
        with open(json_path, 'r') as fp:
            self.samples = json.load(fp)

    def get_case_count(self):
        return len(self.samples)

    def get_case(self, case_no):
        if case_no < 1:
            raise ValueError(f'illegal case No: {case_no}')
        case = deepcopy(self.samples[case_no - 1])
        params = case['input']
        if isinstance(params, dict):
            params = params.values()

        return {'params': params, 'expected': case['expected']}

    def run_test_case(self, case_no, method):
        case = self.get_case(case_no)
        start = time.perf_counter_ns()
        result = eval(f'self.{method}')(*case['params'])
        is_eq = self.eq(result, case['expected'])
        exec_time = (time.perf_counter_ns() - start) / 1000

        ret = style('通过', fg='green') if is_eq else style('不通过', fg='red')
        actual = '' if is_eq else style(f"预期：{case[1]} 实际：{result}", fg='red')

        return [f'用例-{case_no}', ret, f'{exec_time:.2f}', actual]

    def get_methods(self, method):

        if method is not None and method != '':
            return [method]

        methods = [m for m in (set(dir(self)) - set(dir(Problem))) if callable(getattr(self, m))]
        methods.sort()

        return methods

    def run_test(self, case_no, method):
        methods = self.get_methods(method)

        for m in methods:
            tb = PrettyTable()
            tb.field_names = [click.style('测试', fg='blue'), click.style('结果', fg='blue'),
                              click.style('用时(单位：μs)', fg='blue'), click.style('原因', fg='blue')]
            if case_no != -1:
                tb.add_row(self.run_test_case(case_no, m))
            else:
                for i in range(1, self.get_case_count() + 1):
                    tb.add_row(self.run_test_case(i, m))
            print(tb.get_string(title=method))
            print()

    @staticmethod
    def test(filename, case_no=-1, method='', eq_func=eq):

        p_num = os.path.dirname(filename).split('/')[-1][1:]

        if p_num.isdigit():
            p_num = int(p_num)
        else:
            raise ValueError(filename)

        sample_file = os.path.join(PROBLEMS_PATH, f"n{p_num}", 'samples.json')

        lib = importlib.import_module(f'problems.n{p_num}.solution')
        solution = lib.Solution(sample_file, eq_func)

        solution.validate(case_no, method)

    @staticmethod
    def create(n: int):
        p = os.path.join(PROBLEMS_PATH, f'n{n}')

        if n < 1:
            raise ValueError('请输入正确的题目编号')
        else:
            if not os.path.exists(p):
                os.mkdir(p)

            with open(os.path.join(p, 'solution.py'), mode='w', encoding='utf-8') as file:
                file.write(TEMPLATE_SOLUTION)

            with open(os.path.join(p, 'samples.json'), mode='w', encoding='utf-8') as file:
                file.write(TEMPLATE_SAMPLES)

            with open(os.path.join(p, 'README.md'), mode='w', encoding='utf-8') as file:
                file.write('## 解题思路')

            print(f'成功创建题目{n}')