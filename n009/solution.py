from common import AbstractSolution


class Solution(AbstractSolution):

    @property
    def samples(self):
        return [
        {
            'input': 123321,
            'expected': False
        },
        {
            'input': 121,
            'expected': True
        },
        ]

    def _validate(self, input, expected):
        return expected == self.isPalindrome(input)

    def isPalindrome(self, x: int) -> bool:
        if x == 0: return True
        ret = int(str(x)[::-1]) if x > 0 else -int(str(-x)[::-1])
        return True if ret == x else False
