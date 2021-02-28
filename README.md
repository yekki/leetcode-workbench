# 快速上手
## 配置
### 配置环境变量
以ZSH为例，在~/.zshrc中添加或修改环境变量"PYTHONPATH"， 添加本程序根目录， 举例说明：

    export PYTHONPATH=/Users/gniu/Workspaces/leetcode-workbench

### 添加执行权限

    chmod +x main.py

## 使用
### 命令行模式
查看所有命令说明, 举例说明：
    
    ./main.py --help

查看单个命令帮助说明， 举例说明：

    ./main.py test --help

例如：我们测试第一道题，使用测试用例1测试方法"twoSum_3"，则命令如下：

    ./main.py test -p 1 -c 1 -m twoSum_3

### 开发模式
在每道题的solution.py类中加入：

    if __name__ == '__main__':
        Solution.test(__file__)

其中，test函数可添加参数：
- case_no: 测试用例编号
- method: 测试目标方法名

例如：我们测试第一道题，使用测试用例1测试方法"twoSum_3"，则代码如下：

problems/n1/solution.py

    if __name__ == '__main__':
        Solution.test(__file__, 1, 'twoSum_3')

