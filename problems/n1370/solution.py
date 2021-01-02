from common import Problem
import collections
import itertools


#TODO：不理解
class Solution(Problem):
    def sortString(self, s: str) -> str:
        t, result = collections.Counter(s), ""
        sort = sorted(t)
        reverse_sort = list(reversed(sort))
        while len(result) < len(s):
            for k in itertools.chain(sort, reverse_sort):
                result, t[k] = result + (k if t[k] > 0 else ""), t[k] - 1
        return result


if __name__ == '__main__':
    Solution.test(__file__)