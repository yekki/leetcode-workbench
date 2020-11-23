import operator


class ListNode:
    def __init__(self, x):
        if isinstance(x, list):
            self.val = x[0]
            p = self
            for i in x[1:]:
                node = ListNode(i)
                p.next = node
                p = p.next
        else:
            self.val = x
            self.next = None

    def __str__(self) -> str:
        output = ''

        p = self
        while p.next is not None:
            output += f'{p.val}->'
            p = p.next

        output += str(p.val)

        return output

    def __eq__(self, h2):
        p1, p2 = self, h2

        while p1 or p2:
            if p1.val != p2.val:
                return False
            else:
                p1, p2 = p1.next, p2.next

        if p1 or p2:
            return False

        return True



    # def _link2list(self):
    #     l = []
    #     p = self
    #     while p.next is not None:
    #         l.append(p.val)
    #         p = p.next
    #     l.append(p.val)
    #     return l
    #
    # def __eq__(self, o: object) -> bool:
    #     return operator.eq(self._link2list(), o._link2list())

    def fix_head(self):
        p = self
        if self.val is None:
            while p.next is not None:
                p = p.next
            p.next = ListNode(None)
        return self.next



if __name__ == "__main__":
    l1 = ListNode([2, 4, 8, 12, 14])
    l2 = ListNode([2, 4, 8, 13, 14])
    l3 = ListNode([2, 4, 8, 13, None])
    print(l1 == l2)
    print(l3)