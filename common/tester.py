import time, traceback, json
from copy import deepcopy
from .constants import TestResult
from .functions import exec_template_methods, get_problem_no


class Tester:
    def __init__(self, json_path: str):
        with open(json_path, 'r') as fp:
            self.samples = json.load(fp)

        self.cases = list()
        self.methods = list()
        self.renderer = None
        self.problem_no = get_problem_no(json_path)
        self.eq = lambda a, b: a == b

        for case_no, case in enumerate(self.samples):
            params = case['input']
            is_multi_params = False
            if isinstance(params, dict):
                params = list(params.values())
                is_multi_params = True

            self.cases.append({'case_no': case_no, 'params': params, 'is_multi_params': is_multi_params,
                               'expected': case['expected'], 'actual': None, 'method': None} )

    def prepare_test(self):
        pass

    def prepare_case(self, case: dict):
        pass

    def post_case(self, case: dict):
        pass

    def run_template_methods(self, p1: list, p2: list):
        result = exec_template_methods(self.problem_no, p1, p2)
        return result

    def run_case(self, case_no: int, method: str):
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
            if not self.results.ignore_error:
                traceback.print_exc()

        self.post_case(case)

        is_eq = self.eq(case['actual'], case['expected'])

        consuming_time = (time.perf_counter_ns() - start) / 1000
        reason = '' if is_eq else f"实际：{case['actual']} 预期：{case['expected']}"

        return TestResult(problem_no=self.problem_no, case_no=case_no, passed=is_eq, consuming_time=consuming_time, reason=reason, method=method)

    def run_cases(self, case_no: int, method: str):
        if case_no == -1:
            for no in range(len(self.cases)):
                self.renderer.append(self.run_case(no, method))
        else:
            self.renderer.append(self.run_case(case_no, method))

    def run_test(self, case_no: int, method: str):
        # hook method
        self.prepare_test()
        if method is None:
            for m in self.methods:
                self.run_cases(case_no, m)
        else:
            self.run_cases(case_no, method)

        self.renderer.render()

        return self.renderer.passed