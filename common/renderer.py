from prettytable import PrettyTable
from enum import Enum
from click import style
from .constants import TestResult


class Colour(Enum):
    TITLE_PROBLEM = 'blue'
    TITLE_METHOD = 'blue'
    TITLE_COLUMN = 'blue'
    CELL_METHOD = 'white'
    CELL_CASE_NO = 'white'
    CELL_REASON = 'white'
    CELL_TIME = 'white'
    FOOTER = 'magenta'

def colored(msg, color: Colour = None, bold: bool = True):
    if isinstance(msg, bool):
        return style('通过', fg='green', bold=bold) if msg else style('不通过', fg='red', bold=bold)
    else:
        assert color is not None
        return style(msg, fg=color.value, bold=bold)

def render_line(tb: PrettyTable, result: TestResult):
    consuming_time = f'{result.consuming_time:.2f}μs'
    tb.add_row(
        [colored(result.method, Colour.CELL_METHOD, False), colored(str(result.case_no + 1), Colour.CELL_CASE_NO, False),
         colored(result.passed, False), colored(consuming_time, Colour.CELL_TIME, False),
         colored(result.reason, Colour.CELL_REASON, False)])

def render_method(ftb: PrettyTable, method: str, results: list):
    tb = PrettyTable()

    tb.title = colored(method, Colour.TITLE_METHOD)

    tb.field_names = [colored('方法', Colour.TITLE_COLUMN), colored('用例', Colour.TITLE_COLUMN),
                      colored('结果', Colour.TITLE_COLUMN),
                      colored('用时', Colour.TITLE_COLUMN), colored('原因', Colour.TITLE_COLUMN)]

    for row in results:
        render_line(tb, row)

    ftb.add_row([tb])

class RenderType(Enum):
    TEST = 1
    SCAN = 2

class Renderer:
    def __init__(self, problem_no: int, render_type: RenderType):
        self.results = []
        self.render_type = render_type
        self.problem_no = problem_no

    def append(self, result: TestResult):
        self.results.append(result)

    @property
    def passed(self):
        for result in self.results:
            if not result.passed:
                return False

        return True

    def _render_header(self, tb: PrettyTable):
        tb.field_names = [
            '{} {}'.format(colored('题目编号：' + str(self.problem_no), Colour.TITLE_PROBLEM), colored(self.passed))]

    def _render_body(self, tb: PrettyTable):
        # format results to dict, key is method, value is result list
        data = {}
        for i in self.results:
            data.setdefault(i.method, []).append(i)

        for k, v in data.items():
            render_method(tb, k, v)

    def _render_footer(self):
        best = min(self.results, key=lambda r: r.consuming_time)
        consuming_time = f'{best.consuming_time:.2f}μs'
        if self.passed:
            result = f'最优结果：方法：{best.method}， 用例：{best.case_no + 1}， 用时：{consuming_time}'
        else:
            return None
        return colored(result, Colour.FOOTER)

    def render(self):
        results = list()

        for result in self.results:
            if result.passed and self.render_type == RenderType.SCAN:
                pass
            else:
                results.append(result)

        self.results = results

        if len(self.results) > 0:
            tb = PrettyTable()
            self._render_header(tb)
            self._render_body(tb)
            print(tb.get_string())
            if self._render_footer() is not None:
                print(self._render_footer())
