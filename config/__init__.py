import os
import json


class Config:
    def __init__(self, config_file=None):
        if config_file:
            self.path = config_file
        else:
            self.path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'config.json'))

        if not os.path.exists(self.path):
            with open(self.path, 'w') as f:
                self._data = dict()
                self._data['username'] = ''
                self._data['password'] = ''
                self._data['output_dir'] = ''
                self._data['time_interval'] = 0.1
                self._data['root_dir'] = ''
                json.dump(self._data, f)
        else:
            with open(self.path, 'r') as f:
                 self._data = json.load(f)

    @property
    def root_dir(self):
        return self._data['root_dir']

    @property
    def username(self):
        return self._data['username']

    @property
    def password(self):
        return self._data['password']

    @property
    def output_dir(self):
        return self._data['output_dir']

    @property
    def time_interval(self):
        return self._data['time_interval']


conf = Config()