import abc
import json
import time
import click
import os
import importlib
from prettytable import PrettyTable


CONSOLE_FG_INFO_COLOR = 'white'
CONSOLE_FG_ALERT_COLOR = 'yellow'
CONSOLE_FG_ERROR_COLOR = 'red'
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


class Problem(metaclass=abc.ABCMeta):
    def __init__(self, json_path):
        with open(json_path, 'r') as fp:
            self.samples = json.load(fp)

    def _run_test(self, test_num, method, tb):
        data = self.samples[test_num - 1]
        start = time.perf_counter_ns()

        eq_func = self.prepare(data)

        if isinstance(data['input'], dict):
            result = eval(f'self.{method}')(*data['input'].values())
        else:
            result = eval(f'self.{method}')(data['input'])

        is_eq = eq_func(result, data['expected'])

        gap = (time.perf_counter_ns() - start)/1000

        echo = ''

        if is_eq:
            ret = click.style('通过', fg='green')
        else:
            ret = click.style('不通过', fg='red')
            echo = f"预期：{data['expected']} 实际：{result}"

        tb.add_row([f'用例-{test_num}', ret, f'{gap:.2f}', echo])

    def validate(self, test_num: int):
        methods = [m for m in (set(dir(self)) - set(dir(Problem))) if callable(getattr(self, m))]
        methods.sort()
        for method in methods:
            tb = PrettyTable()

            tb.field_names = [click.style('测试', fg='blue'), click.style('结果', fg='blue'), click.style('用时(单位：μs)', fg='blue'), click.style('原因', fg='blue')]
            if test_num != -1:
                self._run_test(test_num, method, tb)
            else:
                for i in range(1, len(self.samples) + 1):
                    self._run_test(i, method, tb)
            print(tb.get_string(title=method))
            print()

    def prepare(self, data, f=None):
        def func(a, b):
            return a == b

        if f:
            return f
        else:
            return func

    @staticmethod
    def test(filename, test_num=-1):

        p_num = os.path.dirname(filename).split('/')[-1][1:]

        if p_num.isdigit():
            p_num = int(p_num)
        else:
            raise ValueError(filename)

        sample_file = os.path.join(PROBLEMS_PATH, f"n{p_num}", 'samples.json')

        lib = importlib.import_module(f'problems.n{p_num}.solution')
        solution = lib.Solution(sample_file)

        solution.validate(test_num)

    @staticmethod
    def create(n: int):
        p = os.path.join(Problem.PATH, f'n{n}')

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