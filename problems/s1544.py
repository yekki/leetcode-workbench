from common import Problem


class Solution(Problem):
    def makeGood(self, s: str) -> str:
        ret = list()
        for ch in s:
            if ret and ret[-1].lower() == ch.lower() and ret[-1] != ch:
                ret.pop()
            else:
                ret.append(ch)
        return "".join(ret)

    def _validate(self, input, expected) -> tuple:
        result = self.makeGood(input)

        return result == expected, expected


if __name__ == '__main__':
    Solution.test(__file__)