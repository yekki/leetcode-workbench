import abc
import json


class AbstractSolution(metaclass=abc.ABCMeta):
    def __init__(self, json_path):
        with open(json_path, 'r') as fp:
            self.samples = json.load(fp)

    @abc.abstractmethod
    def _validate(self, input, expected):
        pass

    def validate(self) -> bool:
        data = self.samples

        for d in data:
            ret = self._validate(d['input'], d['expected'])
            if not ret:
                return ret
        return True
