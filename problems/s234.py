from . import AbstractSolution, ListNode


class Solution(AbstractSolution):
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        p = head

        while p is not None:
            vals.append(p.val)
            p = p.next

        return vals == vals[::-1]


    def _validate(self, input, expected) -> bool:
        result = self.isPalindrome(ListNode(input))

        return expected == result