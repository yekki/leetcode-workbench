import abc
import json
import time
import click
import common


class Problem(metaclass=abc.ABCMeta):
    def __init__(self):
        pass

    def __init__(self, json_path):
        with open(json_path, 'r') as fp:
            self.samples = json.load(fp)

    @abc.abstractmethod
    def _validate(self, input, expected) -> bool:
        pass

    def _run_test(self, i):
        data = self.samples[i - 1]
        start = time.time()
        result = self._validate(data['input'], data['expected'])
        end = time.time()
        color = 'green'
        if result:
            ret = '通过'
        else:
            ret = '不通过'
            color = 'red'
        gap = (end - start) * 1000 * 1000
        click.secho(f'测试用例：{i}, 结果：{ret}，耗时: {gap:.2f}μs', fg=color)

    def validate(self, test_num: int):
        if test_num != -1:
            self._run_test(test_num)
        else:
            for i in range(1, len(self.samples) + 1):
                self._run_test(i)

    @staticmethod
    def test(filename, test_num):
        common.test(filename, test_num)
