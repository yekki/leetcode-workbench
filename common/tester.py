import time, traceback, json
from prettytable import PrettyTable
from click import style
from copy import deepcopy
from .constants import TestResult
from .utils import exec_template_methods, get_problem_no

class Tester:
    def __init__(self, json_path):
        with open(json_path, 'r') as fp:
            self.samples = json.load(fp)

        self.cases = list()
        self.methods = list()
        self.results = dict()
        self.problem_no = get_problem_no(json_path)
        self.eq = lambda a, b: a == b

        for case_no, case in enumerate(self.samples):
            params = case['input']
            is_multi_params = False
            if isinstance(params, dict):
                params = list(params.values())
                is_multi_params = True

            self.cases.append({'case_no': case_no, 'params': params, 'is_multi_params': is_multi_params, 'expected': case['expected'], 'actual': None, 'method': None} )

    def prepare_test(self):
        pass

    def prepare_case(self, case):
        pass

    def post_case(self, case):
        pass

    def run_template_methods(self, p1, p2):
        result = exec_template_methods(self.problem_no, p1, p2)
        return result

    def run_case(self, case_no, method, for_scan):
        case = deepcopy(self.cases[case_no])
        self.prepare_case(case)
        start = time.perf_counter_ns()
        params = case['params']
        case['method'] = method

        try:
            if case['is_multi_params']:
                case['actual'] = eval(f'self.{method}')(*params)
            else:
                case['actual'] = eval(f'self.{method}')(params)
        except:
            if not for_scan:
                traceback.print_exc()

        self.post_case(case)

        is_eq = self.eq(case['actual'], case['expected'])

        consuming_time = (time.perf_counter_ns() - start) / 1000
        reason = '' if is_eq else f"实际：{case['actual']} 预期：{case['expected']}"

        return TestResult(case_no=case_no, passed=is_eq, consuming_time=consuming_time, reason=reason, method=method)

    def run_cases(self, case_no, method, for_scan):
        ret = list()
        is_success = True
        if case_no == -1:
            for no in range(len(self.cases)):
                result = self.run_case(no, method, for_scan)
                if not result.passed:
                    is_success = False
                ret.append(result)
        else:
            result = self.run_case(case_no, method, for_scan)
            if not result.passed:
                is_success = False
            ret.append(self.run_case(case_no, method, for_scan))

        self.results[method] = ret

        return is_success

    def run_test(self, case_no, method, for_scan, is_render):
        # hook method
        self.prepare_test()
        is_success = True
        if method is None:
            for m in self.methods:
                if not self.run_cases(case_no, m, for_scan):
                    is_success = False
        else:
            if self.run_cases(case_no, method, for_scan):
                is_success = False

        if is_render:
            self.render(for_scan)

        return is_success

    def is_test_success(self):
        for row in self.results.values():
            for t in row:
                if not t.passed:
                    return False

        return True

    def render(self, for_scan):
        frame = PrettyTable()
        frame.title = f'题目编号：{self.problem_no}'
        frame.field_names = ['执行结果：' + style('成功', fg='blue')] if self.is_test_success() else ['执行结果：' + style('失败', fg='red')]

        for method, rows in self.results.items():
            tb = PrettyTable()
            tb.title = method
            tb.field_names = [style('测试', fg='blue'), style('结果', fg='blue'),
                              style('用时', fg='blue'), style('原因', fg='blue')]

            for row in rows:
                passed = style('通过', fg='green') if row.passed else style('不通过', fg='red')
                consuming_time = f'{row.consuming_time:.2f}μs'
                tb.add_row([style(f'用例-{row.case_no}'), passed, consuming_time, row.reason])

            tb.align['用时(单位：μs)'] = 'r'
            frame.add_row([tb])
        if for_scan:
            if not self.is_test_success():
                print(frame.get_string())
        else:
            print(frame.get_string())
