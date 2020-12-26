#!/usr/bin/env python3
# coding=utf-8
import click
import os
from common import run, get_modules, create_p

APP_NAME='Leetcode Workbench'
APP_VERSION = 'v1.0b'
APP_AUTHOR = 'Gary Niu'

@click.group()
def cli():
    pass

@cli.command()
def version():
    print(f'{APP_NAME} {APP_VERSION}, 作者：{APP_AUTHOR}')

@cli.command()
def count():
    p_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'problems')
    p_list = os.listdir(p_path)
    p_list.sort()

    print(f'已完成题目:{len(p_list)}个')
    print(f'最后保存文件：{p_list[-1]}')


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

@cli.command()
@click.option('--number', '-n', type=click.INT, help='题目编号')
def np(number):
    create_p(number)


if __name__ == '__main__':
    cli()
