import os
import json


class Config:
    def __init__(self, config_file=None):
        if config_file:
            self.path = config_file
        else:
            self.path = os.path.abspath(os.path.join(__file__, '../../config.json'))

        if not os.path.exists(self.path):
            with open(self.path, 'w') as f:
                self._data = dict()
                self._data['username'] = ''
                self._data['password'] = ''
                self._data['output_dir'] = ''
                self._data['time_interval']=0.1
                json.dump(self._data, f)
        else:
            with open(self.path, 'r') as f:
                 self._data = json.load(f)

    def update(self):
        username = input('请输入用户名:')
        password = input('请输入密码：')
        output_dir = input('请选择输出目录：')
        data = dict(username=username,
                    password=password,
                    outputDir=output_dir,
                    timeInterval=0.1)
        with open(self.path, 'w') as f:
            json.dump(data, f)

        self._data = data
        return data

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

config = Config()

if __name__ == '__main__':

    config = Config()
    print(config.username)
    #config.update()
