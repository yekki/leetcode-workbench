#!/usr/bin/env python3
# coding=utf-8
import click
import os
from common import Problem

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


if __name__ == '__main__':
    cli()
