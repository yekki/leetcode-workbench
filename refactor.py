import os
import shutil


def step_1():
    p = os.path.join(os.path.dirname(__file__), 'problems')
    for f in os.listdir(p):
        n, _ = os.path.splitext(f)
        dir = os.path.join(p, f'n{n[1:]}')
        os.mkdir(dir)
        shutil.move(os.path.join(p, f), os.path.join(dir, 'solution.py'))

    print('step 1 finished.')

def step_2():
    p = os.path.join(os.path.dirname(__file__), 'problems')
    s = os.path.join(os.path.dirname(__file__), 'samples')

    for f in os.listdir(s):
        n, _ = os.path.splitext(f)
        d = os.path.join(p, f'n{n[1:]}')
        shutil.move(os.path.join(s, f), os.path.join(d, 'samples.json'))

    print('step 2 finished.')

def step_3():
    p = os.path.join(os.path.dirname(__file__), 'problems')
    for f in os.listdir(p):
        n, _ = os.path.splitext(f)
        d = os.path.join(p, f'n{n[1:]}')
        with open(os.path.join(d, 'README.md'), mode='w', encoding='utf-8') as file:
            file.write('## 解题思路')

    print('step 3 finished.')


if __name__ == '__main__':
    pass