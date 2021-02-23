import abc
import json
import time
import os
import importlib
import traceback
from prettytable import PrettyTable
from collections import namedtuple
from copy import deepcopy
from click import style
from inspect import ismethod, isclass
from common.utils import exec_template_methods

DEBUG = False

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

IGNORE_METHODS = ['eq']

TestResult = namedtuple('TestResult', ['method', 'case_no', 'passed', 'consuming_time', 'reason'])


def _eq(a, b):
    return a == b


class Problem(metaclass=abc.ABCMeta):
    def __init__(self, json_path):
        self.eq = _eq
        self.result = dict()
        self.p_num = -1
        with open(json_path, 'r') as fp:
            self.samples = json.load(fp)

    # run before test begin, one test including many cases
    def prepare_test(self):
        pass

        # run before test case begin

    def prepare_case(self, case):
        pass

    def _get_case_count(self):
        return len(self.samples)

    def _get_case(self, case_no):
        if case_no < 1:
            raise ValueError(f'illegal case No: {case_no}')
        case = deepcopy(self.samples[case_no - 1])
        params = case['input']
        multi_params = False
        if isinstance(params, dict):
            params = list(params.values())
            multi_params = True

        return {'params': params, 'multi_params': multi_params, 'expected': case['expected']}

    def _run_test_case(self, case_no, method):
        case = self._get_case(case_no)
        self.prepare_case(case)
        start = time.perf_counter_ns()
        params = case['params']
        result = None

        try:
            if case['multi_params']:
                result = eval(f'self.{method}')(*params)
            else:
                result = eval(f'self.{method}')(params)
        except:
            if DEBUG:
                traceback.print_exc()

        is_eq = self.eq(result, case['expected'])
        consuming_time = (time.perf_counter_ns() - start) / 1000

        reason = '' if is_eq else f"实际：{result} 预期：{case['expected']}"

        return TestResult(case_no=case_no, passed=is_eq, consuming_time=consuming_time, reason=reason, method=method)

    def _render(self):
        case_count = -1
        for method, rows in self.result.items():
            tb = PrettyTable()
            tb.title = method
            tb.field_names = [style('测试', fg='blue'), style('结果', fg='blue'),
                              style('用时', fg='blue'), style('原因', fg='blue')]

            if case_count == -1:
                case_count = len(rows)

            for r in rows:
                passed = style('通过', fg='green') if r.passed else style('不通过', fg='red')
                consuming_time = f'{r.consuming_time:.2f}μs'
                tb.add_row([style(f'用例-{r.case_no}'), passed, consuming_time, r.reason])

            tb.align['用时(单位：μs)'] = 'r'
            print(tb.get_string())

    def _run_test(self, case_no, methods, render):
        self.prepare_test()
        result = True

        for m in methods:
            rows = []
            if case_no != -1:
                rows.append(self._run_test_case(case_no, m))
            else:
                for i in range(1, len(self.samples) + 1):
                    rows.append(self._run_test_case(i, m))
            self.result[m] = rows

            for r in rows:
                if not r.passed:
                    result = False
                    break

        if render: self._render()

        return result

    def _get_test_methods(self, method=None, ignore_methods=IGNORE_METHODS):

        if method is not None:
            return [method]

        methods = [m for m in (set(dir(self)) - set(dir(Problem))) if
                   m not in ignore_methods and ismethod(getattr(self, m))]

        if self._is_template_test():
            methods.append('run_template_methods')

        methods.sort()

        return methods

    def _is_template_test(self):
        return self._get_inner_class() is not None

    # if there is an inner class, then the solution is template method.
    def _get_inner_class(self):
        for m in (set(dir(self)) - set(dir(Problem))):
            if isclass(getattr(self, m)):
                return m
        return None

    # run template method
    def run_template_methods(self, p1, p2):
        clazz = self._get_inner_class()
        lib = importlib.import_module(f'problems.n{self.p_num}.solution')
        inst = eval(f'lib.Solution.{clazz}')()
        result = exec_template_methods(inst, p1, p2)

        return result

    @staticmethod
    def test(filename, case_no=-1, method=None, render=True):

        p_num = os.path.dirname(filename).split('/')[-1][1:]

        if p_num.isdigit():
            p_num = int(p_num)
        else:
            raise ValueError(filename)

        sample_file = os.path.join(PROBLEMS_PATH, f"n{p_num}", 'samples.json')

        lib = importlib.import_module(f'problems.n{p_num}.solution')
        solution = lib.Solution(sample_file)
        solution.p_num = p_num
        case_count = solution._get_case_count()

        methods = solution._get_test_methods(method)

        if method is not None and method not in methods:
            raise ValueError(f'函数名"{method}"不存在，请检查函数名是否拼错或者题目编号错误。')
        elif case_no > case_count:
            raise ValueError(f'侧试用例编号不存在，测试编号不能大于{case_count}。')
        else:
            return solution._run_test(case_no, methods, render)

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
