#!/usr/bin/env python
# coding=utf-8
from solutions import SolutionTestCase
import unittest
import sys


def help() -> None:
    print('''
    Help:
    ./main.py [num]
    
    num: The number of leetcode problem.
    
    For example: ./main.py 10
    ''')
    exit(0)


def parse_cmd_args() -> int:

    if len(sys.argv) < 2:
        help()

    num = sys.argv[1]

    if num.isnumeric():
        num = int(num)
    else:
        help()

    return num
    # method_list = [func for func in dir(SolutionTestCase) if callable(
    #     getattr(SolutionTestCase, func)) and func.startswith("test_")]
    #
    # count = len(method_list)
    #
    # if num > count:
    #     print(
    #         f'The num is beyond the count of test methods, there are only {count} test methods in your test case. Please check it and try again!')
    #     exit(-1)
    # else:
    #     return num


if __name__ == '__main__':
    num = parse_cmd_args()
    suite = unittest.TestSuite()
    suite.addTest(SolutionTestCase(f'test_{num}'))
    unittest.TextTestRunner().run(suite)
