#!/usr/bin/env python
# coding=utf-8
import sys
import os
import importlib
from common import print_result


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


if __name__ == '__main__':
    num = parse_cmd_args()
    lib = importlib.import_module(f'problems.s{num}')
    s = lib.Solution(os.path.join(os.getcwd(), 'samples', f'{num}.json'))
    print_result(s.validate())