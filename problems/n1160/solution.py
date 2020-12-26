from common import Problem
from typing import List
import collections

class Solution(Problem):
    def countCharacters(self, words: List[str], chars: str) -> int:
        ret = 0
        c1 = collections.Counter(chars)
        for i in range(len(words)):
            c2 = collections.Counter(words[i])
            for k, v in c2.items():
                if k in c1.keys() and v <= c1.get(k):
                    continue
                else:
                    break
            else:
                ret += len(words[i])
        return ret

    def _validate(self, input, expected) -> tuple:
        result = self.countCharacters_1(input['p1'], input['p2'])

        return expected == result, result


if __name__ == '__main__':
    Solution.test(__file__)