#!/usr/bin/env python3
# coding=utf-8
import click
import os
import importlib
from common import Problem, PROBLEMS_PATH


APP_NAME='Leetcode Workbench'
APP_VERSION = 'v1.3b'
APP_AUTHOR = 'Gary Niu'


@click.group()
def cli():
    pass


@cli.command()
def version():
    print('*' * 40)
    print(f'{APP_NAME} {APP_VERSION}, 作者：{APP_AUTHOR}')
    print('*' * 40)


@cli.command()
def count():
    p_list = os.listdir(Problem.PATH)
    p_list.sort()

    print(f'已完成题目:{len(p_list)}个')
    print(f'最后保存文件：{p_list[-1]}')


@cli.command()
@click.option('--problem', '-p', type=click.INT, help='题目编号')
def np(problem):
    Problem.create(problem)


@cli.command()
@click.option('--problem', '-p', type=click.INT, help='题目编号')
@click.option('--case', '-c', type=click.INT, default=-1, help='题目编号')
@click.option('--method', '-m', type=click.STRING, default='', help='题目编号')
def test(problem, case, method):
    lib = importlib.import_module(f'problems.n{problem}.solution')
    py_file = os.path.join(PROBLEMS_PATH, f"n{problem}", 'solution.py')
    lib.Solution.test(py_file, case, method)


@cli.command()
@click.option('--comment', '-c', type=click.STRING, default='fix update',  help='题目编号')
def commit(comment):
    os.system(f'git commit -am "{comment}"' )
    os.system('git push')


@cli.command()
def sync():
    os.system('git fetch --all')
    os.system('git reset --hard origin/main')
    os.system('git pull')


if __name__ == '__main__':
    cli()
