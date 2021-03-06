#!/usr/bin/env python3
# coding=utf-8
import os, click
from prettytable import PrettyTable
from common import Problem, RenderType, PROBLEMS_PATH, Colour, colored, get_solution_clazz


APP_NAME='Leetcode Workbench'
APP_VERSION = 'v2.0b'
APP_AUTHOR = 'Gary Niu'
APP_AUTHOR_EMAIL = 'gary.niu@gmail.com'

@click.group()
def cli():
    pass

@cli.command(help='查看应用说明')
def version():
    tb = PrettyTable()
    tb.field_names = [f'{APP_NAME} {APP_VERSION}']
    tb.add_row([f'作者：{APP_AUTHOR} 联系方式：{APP_AUTHOR_EMAIL}'])
    print(tb.get_string())

@cli.command(help='创建新题目')
@click.option('--problem', '-p', type=click.INT, help='题目编号')
def np(problem):
    Problem.create(problem)


@cli.command(help='执行测试')
@click.option('--problem', '-p', required=True, type=click.INT, help='题目编号')
@click.option('--case', '-c', type=click.INT, default=-1, help='测试用例编号')
@click.option('--method', '-m', type=click.STRING, default=None, help='测试用例方法名')
def test(problem, case, method):
    py_file = os.path.join(PROBLEMS_PATH, f'n{problem}', 'solution.py')
    clazz = get_solution_clazz(py_file)
    clazz.test(py_file, case, method)

@cli.command(help='扫描所有题目情况')
def scan():
    error_count = 0
    passed_count = 0
    for p in os.listdir(PROBLEMS_PATH):
        py_file = os.path.join(PROBLEMS_PATH, f'{p}', 'solution.py')
        if get_solution_clazz(py_file).test(filepath=py_file, render_type=RenderType.SCAN):
            passed_count += 1
        else:
            error_count += 1

    print(colored(msg=f'您有{passed_count}道题通过测试，{error_count}道题未测试通过！', color=Colour.FOOTER))


@cli.command(help='提交当前更新到github')
@click.option('--comment', '-c', type=click.STRING, default='fix update', help='本次提交备注说明')
def commit(comment):
    os.system(f'git commit -am "{comment}"' )
    os.system('git push')


@cli.command(help='用github代码覆盖本地代码')
def sync():
    os.system('git fetch --all')
    os.system('git reset --hard origin/main')
    os.system('git pull')


if __name__ == '__main__':
    cli()