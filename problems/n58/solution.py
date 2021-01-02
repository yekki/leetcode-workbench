from common import Problem


class Solution(Problem):
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split(' ')

        return len(words[len(words) - 1])


if __name__ == '__main__':
    Solution.test(__file__)