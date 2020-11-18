from . import AbstractSolution
from typing import List


class Solution(AbstractSolution):
    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     if not strs: return ""
    #     s1 = min(strs)
    #     s2 = max(strs)
    #     for i, x in enumerate(s1):
    #         if x != s2[i]:
    #             return s2[:i]
    #     return s1

    def longestCommonPrefix(self, strs):
        if not strs: return ""
        ss = list(map(set, zip(*strs)))
        res = ""
        for i, x in enumerate(ss):
            x = list(x)
            if len(x) > 1:
                break
            res = res + x[0]
        return res

    def _validate(self, input, expected) -> bool:
        result = self.longestCommonPrefix(input)

        return result == expected