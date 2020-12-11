#!/usr/bin/env python
# coding=utf-8
import click
import os
from common import run, get_modules


@click.group()
def cli():
    pass


@cli.command()
def count():
    p_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'problems')
    c = 0
    for f in os.listdir(p_path):
        (name, ext) = os.path.splitext(f)
        if name.startswith('s') and name[1:].isdigit() and ext == '.py':
            c += 1
    print(f'已完成题目{c}个')
    # 用到的知识
    # os.path.getatime(file) 输出文件访问时间
    # os.path.getctime(file) 输出文件的创建时间
    # os.path.getmtime(file) 输出文件最近修改时间
    # 要加上最后修改时间

@cli.command()
@click.option('--pc', '-p', default=-1, type=click.INT, help='题目编号')
@click.option('--tc', '-t', default=-1, type=click.INT, help='测试用例编号')
def test(pc, tc):
    if pc == -1:
        modules = get_modules('problems')
        solutions = [int(m[1:]) for m in modules]
        solutions.sort()
        for m in solutions:
            run(m, tc)
    else:
        run(pc, tc)


if __name__ == '__main__':
    cli()
