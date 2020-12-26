from common import Problem
from structure import ListNode


class Solution(Problem):
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        p = head

        while p is not None:
            vals.append(p.val)
            p = p.next

        return vals == vals[::-1]

    def _validate(self, input, expected) -> tuple:
        result = self.isPalindrome(ListNode(input))

        return expected == result, result


if __name__ == '__main__':
    Solution.test(__file__)