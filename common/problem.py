import abc
import json
import time
import click
import os
import importlib

CONSOLE_FG_INFO_COLOR = 'blue'
CONSOLE_FG_ALERT_COLOR = 'orange'
CONSOLE_FG_ERROR_COLOR = 'red'

TEMPLATE_SOLUTION = '''from common import Problem


class Solution(Problem):

    def _validate(self, input, expected) -> tuple:
        result = self

        return result == expected, result


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
    PATH = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'problems')
    FG_COLOR = 'green'

    def __init__(self, json_path):
        self.color = 'green'
        with open(json_path, 'r') as fp:
            self.samples = json.load(fp)

    def _validate(self, input, expected, method) -> tuple:
        if isinstance(input, dict):
            result = eval(f'self.{method}')(*input.values())
        else:
            result = eval(f'self.{method}')(input)

        return self.eq(result, expected), result

    def _get_methods(self):
        return [m for m in (set(dir(self)) - set(dir(Problem))) if callable(getattr(self, m))]

    def _run_test(self, test_num, method):
        data = self.samples[test_num - 1]
        start = time.time()
        result = self._validate(data['input'], data['expected'], method)
        end = time.time()
        echo = ''
        if result[0]:
            ret = '通过'
            color = CONSOLE_FG_INFO_COLOR
        else:
            ret = '不通过'
            color = CONSOLE_FG_ALERT_COLOR
            echo = f"（预期：{data['expected']}，实际：{result[1]}）"
        gap = (end - start) * 1000 * 1000
        click.secho(f'测试用例-{test_num}: 结果：{ret}{echo}，耗时: {gap:.2f} 微秒', fg=color)

    def eq(self, result, expected):
        return result == expected

    def validate(self, test_num: int):
        methods = [m for m in (set(dir(self)) - set(dir(Problem))) if callable(getattr(self, m))]
        for method in methods:
            click.secho(f'函数名 — {method}', fg=self.color)
            if test_num != -1:
                self._run_test(test_num, method)
            else:
                for i in range(1, len(self.samples) + 1):
                    self._run_test(i, method)
            click.secho('-' * 60, fg=CONSOLE_FG_INFO_COLOR)

    @staticmethod
    def test(filename, test_num=-1):

        p_num = os.path.dirname(filename).split('/')[-1][1:]

        if p_num.isdigit():
            p_num = int(p_num)
        else:
            raise ValueError(filename)

        sample_file = os.path.join(Problem.PATH, f"n{p_num}", 'samples.json')

        # message box
        msg = f'第{p_num}道题'
        click.secho('*' * 60, fg=CONSOLE_FG_INFO_COLOR)
        n = ((60 - len(msg)) - 1) // 2
        click.secho(' ' * n + msg + ' ' * n, fg=CONSOLE_FG_INFO_COLOR)
        click.secho('*' * 60, fg=CONSOLE_FG_INFO_COLOR)

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