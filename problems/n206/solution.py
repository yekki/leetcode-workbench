from common import Problem
from structure import ListNode


class Solution(Problem):
    def reverseList(self, head):
        if head is None:
            return None
        p = head
        q = head.next
        head.next = None
        while q:
            r = q.next
            q.next = p
            p = q
            q = r
        head = p
        return head

    def prepare_case(self, case):
        case['params'] = ListNode(case['params'])
        case['expected'] = ListNode(case['expected'])

        return case


if __name__ == '__main__':
    Solution.test(__file__)