from common import Problem
from structure import ListNode


class Solution(Problem):
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

    def prepare_case(self, case_no):
        data = super().prepare_case(case_no)
        params = data['params']
        params[0] = ListNode(params[0])
        params[1] = ListNode(params[1])
        data['params'] = params
        data['expected'] = ListNode(data['expected'])

        return data


if __name__ == '__main__':
    Solution.test(__file__)
