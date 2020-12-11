#!/usr/bin/env python
# coding=utf-8
import click
import os
from common import run, get_modules


def file_filter(file):
    (name, ext) = os.path.splitext(file)
    return name.startswith('s') and name[1:].isdigit() and ext == '.py'


@click.group()
def cli():
    pass


@cli.command()
def count():
    p_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'problems')
    file_list = list(filter(file_filter, os.listdir(p_path)))
    file_list.sort(key=lambda fn: os.path.getmtime(os.path.join(p_path, fn)))
    print(f'已完成题目:{len(file_list)}个')
    print(f'最后保存文件：{file_list[-1]}')


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
