from common import Problem, list_eq, exec_template_methods
import math


class Solution(Problem):
    class MinStack:
        def __init__(self):
            self.stack = []
            self.min_stack = [math.inf]

        def push(self, x: int) -> None:
            self.stack.append(x)
            self.min_stack.append(min(x, self.min_stack[-1]))

        def pop(self) -> None:
            self.stack.pop()
            self.min_stack.pop()

        def top(self) -> int:
            return self.stack[-1]

        def getMin(self) -> int:
            return self.min_stack[-1]


    def exec(self, input, expected) -> tuple:
        inst = Solution.MinStack()
        result = exec_template_methods(inst, input['p1'], input['p2'])

        return list_eq(expected, result), result

    def prepare_test(self):
        self.eq = list_eq


if __name__ == '__main__':
    Solution.test(__file__)