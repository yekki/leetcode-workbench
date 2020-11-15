from functools import wraps
import time
import click

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        gap = (end - start) * 1000 * 1000
        print('Running time: %s μs' % gap)
    return wrapper


def print_result(ret):
    if ret:
        click.secho('Passed', fg='green')
    else:
        click.secho('Not pass', fg='red')