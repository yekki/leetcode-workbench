from common import Problem
from structure import ListNode


class Solution(Problem):
    def reverseList(self, head):
        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev

    def _validate(self, input, expected) -> tuple:
        ln = ListNode(input)
        result = self.reverseList(ln).fix_none()

        return result == ListNode(expected), result


if __name__ == '__main__':
    Solution.test(__file__)