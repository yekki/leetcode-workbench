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

    def _link2list(self):
        l = []
        p = self
        while p.next is not None:
            l.append(p.val)
            p = p.next
        l.append(p.val)
        return l

    def __eq__(self, o: object) -> bool:
        return operator.eq(self._link2list(), o._link2list())


if __name__ == "__main__":
    l1 = ListNode([2, 4, 8, 12, 14])
    l2 = ListNode([2, 4, 8, 13, 14])
    print(l1 == l2)
