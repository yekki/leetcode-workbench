import abc
import json
import time
import click


class AbstractSolution(metaclass=abc.ABCMeta):
    def __init__(self):
        pass

    def __init__(self, json_path):
        with open(json_path, 'r') as fp:
            self.samples = json.load(fp)

    @abc.abstractmethod
    def _validate(self, input, expected) -> bool:
        pass

    def validate(self):
        data = self.samples

        for i, d in enumerate(data):
            start = time.time()
            ret = self._validate(d['input'], d['expected'])
            color = 'green'
            if ret:
                ret = '通过'
            else:
                ret = '不通过'
                color = 'red'

            end = time.time()
            gap = (end - start) * 1000 * 1000
            click.secho(f'测试用例：{i+1}, 结果：{ret}，耗时: {gap:.2f}μs' , fg=color)

