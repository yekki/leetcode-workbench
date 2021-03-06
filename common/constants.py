import os
from collections import namedtuple


TestResult = namedtuple('TestResult', ['problem_no', 'method', 'case_no', 'passed', 'consuming_time', 'reason'])
TestCase = namedtuple('TestCase', ['case_no', 'params', 'is_multi_params', 'expected'] )

PROBLEMS_PATH = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'problems')
RUN_TEST_CASE_IGNORE_METHODS = ['eq']
BASE_URL = 'https://leetcode-cn.com/problems'

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


# _ansi_colors = {
#     "black": 30,
#     "red": 31,
#     "green": 32,
#     "yellow": 33,
#     "blue": 34,
#     "magenta": 35,
#     "cyan": 36,
#     "white": 37,
#     "reset": 39,
#     "bright_black": 90,
#     "bright_red": 91,
#     "bright_green": 92,
#     "bright_yellow": 93,
#     "bright_blue": 94,
#     "bright_magenta": 95,
#     "bright_cyan": 96,
#     "bright_white": 97,
# }