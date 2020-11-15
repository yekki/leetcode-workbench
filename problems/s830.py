from typing import List


INPUT = 'abbxxxxzzy'
EXPECTED = [[3,6]]


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res = []
        counter = 1
        i = 0
        c = len(s) - 1

        while i < c:
            if s[i] == s[i + 1]:
                counter += 1
            else:
                if counter >= 3:
                    res.append([i - counter + 1, i])
                counter = 1
            i += 1

        if counter >= 3:
            res.append([i - counter + 1, i])

        return res
