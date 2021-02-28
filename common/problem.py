import os

from inspect import ismethod, isclass
from .tester import Tester
from .utils import error, create_solution_inst, get_problem_no
from .constants import RUN_TEST_CASE_IGNORE_METHODS, PROBLEMS_PATH, TEMPLATE_SOLUTION, TEMPLATE_SAMPLES


class Problem(Tester):
    def __init__(self, json_path):
        super().__init__(json_path)

        self.methods = [m for m in (set(dir(self)) - set(dir(Problem))) if
                        m not in RUN_TEST_CASE_IGNORE_METHODS and ismethod(getattr(self, m))]
        self.methods.sort()

        for method in self.methods:
            if isclass(getattr(self, method)):
                self.methods = ['run_template_methods']

    @staticmethod
    def test(filepath, case_no=-1, method=None, for_scan=False, is_render=True):
        inst = create_solution_inst(filepath)

        case_count = len(inst.cases)

        if method is not None and method not in inst.methods:
            error(f'函数名"{method}"不存在，请检查函数名是否拼错或者题目编号错误。')

        if case_no > case_count:
            error(f'侧试用例编号不存在，测试编号不能大于{case_count}。')

        return inst.run_test(case_no=case_no, method=method, for_scan=for_scan, is_render=is_render)

    @staticmethod
    def create(n: int):
        p = os.path.join(PROBLEMS_PATH, f'n{n}')

        if n < 1:
            error('请输入正确的题目编号')
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