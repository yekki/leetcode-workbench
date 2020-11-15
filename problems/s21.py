from common import AbstractSolution
from common import ListNode

class Solution(AbstractSolution):
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        p = head

        while (l1 is not None) and (l2 is not None):
            if l1.val > l2.val:
                p.next = l2
                l2 = l2.next
            else:
                p.next = l1
                l1 = l1.next
            p = p.next

        if l1 is None:
            p.next = l2
        if l2 is None:
            p.next = l1

        return head.next

    def _validate(self, input, expected) -> bool:
        l1 = ListNode(input['p1'])
        l2 = ListNode(input['p2'])
        result = self.mergeTwoLists(l1, l2)

        return ListNode(expected) == result

