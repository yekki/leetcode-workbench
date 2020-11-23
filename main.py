#!/usr/bin/env python
# coding=utf-8
import click
from common import run, get_modules


@click.command()
@click.option('--pc', '-p', default=-1, type=click.INT, help='题目编号')
@click.option('--tc', '-t', default=-1, type=click.INT, help='测试用例编号')
def main(pc, tc):
    if pc == -1:
        modules = get_modules('problems')
        solutions = [int(m[1:]) for m in modules]
        solutions.sort()
        for m in solutions:
            run(m, tc)
    else:
        run(pc, tc)


if __name__ == '__main__':
    main()
