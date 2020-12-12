from common import Problem
from structure import ListNode


class Solution(Problem):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        node = dummy
        carry = 0

        while l1 or l2 or carry != 0:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            carry, rem = divmod(carry, 10)
            node.next = ListNode(rem)
            node = node.next

        return dummy.next

    def _validate(self, input, expected) -> tuple:
        l1 = input['p1']
        l2 = input['p2']
        e = ListNode(expected)
        result = self.addTwoNumbers(ListNode(l1), ListNode(l2))

        return result == e, result


if __name__ == '__main__':
    Solution.test(__file__)
