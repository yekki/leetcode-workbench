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

    def prepare_case(self, case):
        params = case['params']
        params[0] = ListNode(params[0])
        params[1] = ListNode(params[1])
        case['params'] = params
        case['expected'] = ListNode(case['expected'])


if __name__ == '__main__':
    Solution.test(__file__)
