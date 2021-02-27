import os
from collections import namedtuple


TestResult = namedtuple('TestResult', ['method', 'case_no', 'passed', 'consuming_time', 'reason'])
TestCase = namedtuple('TestCase', ['case_no', 'params', 'is_multi_params', 'expected'] )

PROBLEMS_PATH = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'problems')
RUN_TEST_CASE_IGNORE_METHODS = ['eq']

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


