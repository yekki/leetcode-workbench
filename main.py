#!/usr/bin/env python3
# coding=utf-8
import click
import os
import importlib
from common import Problem, PROBLEMS_PATH


APP_NAME='Leetcode Workbench'
APP_VERSION = 'v1.2b'
APP_AUTHOR = 'Gary Niu'


@click.group()
def cli():
    pass


@cli.command()
def version():
    print(f'{APP_NAME} {APP_VERSION}, 作者：{APP_AUTHOR}')


@cli.command()
def count():
    p_list = os.listdir(Problem.PATH)
    p_list.sort()

    print(f'已完成题目:{len(p_list)}个')
    print(f'最后保存文件：{p_list[-1]}')


@cli.command()
@click.option('--number', '-n', type=click.INT, help='题目编号')
def np(number):
    Problem.create(number)


@cli.command()
@click.option('--problem', '-p', type=click.INT, help='题目编号')
@click.option('--case', '-c', type=click.INT, default=-1, help='题目编号')
def test(problem, case):
    lib = importlib.import_module(f'problems.n{problem}.solution')
    py_file = os.path.join(PROBLEMS_PATH, f"n{problem}", 'solution.py')
    lib.Solution.test(py_file, case)


if __name__ == '__main__':
    cli()
