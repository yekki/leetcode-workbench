#!/usr/bin/env python3
# coding=utf-8
import click
import os
import importlib
from prettytable import PrettyTable
from common import Problem, PROBLEMS_PATH


APP_NAME='Leetcode Workbench'
APP_VERSION = 'v1.6b'
APP_AUTHOR = 'Gary Niu'

@click.group()
def cli():
    pass


@cli.command(help='查看应用信息')
def version():
    print('*' * 40)
    print(f'{APP_NAME} {APP_VERSION}, 作者：{APP_AUTHOR}')
    print('*' * 40)


@cli.command(help='查看完成题目数')
def count():
    p_list = os.listdir(PROBLEMS_PATH)
    p_list.sort()

    print(f'已完成题目:{len(p_list)}个')
    print(f'最后保存文件：{p_list[-1]}')


@cli.command(help='创建新题目')
@click.option('--problem', '-p', type=click.INT, help='题目编号')
def np(problem):
    Problem.create(problem)


@cli.command(help='执行测试')
@click.option('--problem', '-p', default=-1, type=click.INT, help='题目编号')
@click.option('--case', '-c', type=click.INT, default=-1, help='测试用例编号')
@click.option('--method', '-m', type=click.STRING, default=None, help='测试用例方法名')
@click.option('--error', '-e', type=click.BOOL, default=True, help='只显示未通过测试题目')
def test(problem, case, method, error):
    if problem == -1:
        p_list = os.listdir(PROBLEMS_PATH)
        result = dict()
        for p in p_list:
            lib = importlib.import_module(f'problems.{p}.solution')
            py_file = os.path.join(PROBLEMS_PATH, f'{p}', 'solution.py')
            result[p] = lib.Solution.test(py_file, case, method, False)

        tb = PrettyTable()
        tb.title = click.style('总体情况', fg='blue')
        tb.field_names = [click.style('题目号', fg='blue'), click.style('测试结果', fg='blue')]
        for k, v in result.items():
            passed = click.style('通过', fg='green') if v else click.style('不通过', fg='red')
            if error:
                if not v:
                    tb.add_row([k, passed])
            else:
                tb.add_row([k, passed])
        print(tb.get_string())
    else:
        try:
            lib = importlib.import_module(f'problems.n{problem}.solution')
            py_file = os.path.join(PROBLEMS_PATH, f'n{problem}', 'solution.py')
            lib.Solution.test(py_file, case, method)
        except:
            print(f'题目{problem}您还没做呢！')


@cli.command(help='提交当前更新到github')
@click.option('--comment', '-c', type=click.STRING, default='fix update', help='提交信息')
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