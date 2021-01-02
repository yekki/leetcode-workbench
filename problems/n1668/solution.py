from common import Problem


class Solution(Problem):
    def maxRepeating(self, sequence: str, word: str) -> int:
        c = len(sequence)//len(word)
        ret = 0
        for i in range(c):
            if (word + i * word) in sequence:
                ret += 1

        return ret


if __name__ == '__main__':
    Solution.test(__file__)