#!/usr/bin/env python3
# coding=utf-8
import os, click
from common import Problem, PROBLEMS_PATH, get_solution_clazz


APP_NAME='Leetcode Workbench'
APP_VERSION = 'v1.8b'
APP_AUTHOR = 'Gary Niu'

@click.group()
def cli():
    pass


@cli.command(help='查看应用说明')
def version():
    print('*' * 40)
    print(f'{APP_NAME} {APP_VERSION}, 作者：{APP_AUTHOR}')
    print('*' * 40)

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
@click.option('--details', '-d', is_flag=True, help='是否显示详情')
def scan(details):
    p_list = os.listdir(PROBLEMS_PATH)
    error_count = 0

    for p in p_list:
        py_file = os.path.join(PROBLEMS_PATH, f'{p}', 'solution.py')
        is_success = get_solution_clazz(py_file).test(py_file, for_scan=True, is_render=details)
        if not is_success:
            error_count += 1

    print(f'完成题目总数：{len(p_list)}, 出错题目数量：{error_count}')

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