

class ListNode:
    def __init__(self, x=None):
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

    def to_list(self):
        p = self
        l = []
        while p:
            l.append(p.val)
            p = p.next

        return l

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

    '''
    Background: If input is 5->4->3->2->1->None, the reversed result should be: None->1->2->3->4->5, 
    but the expected result should be: 1->2->3->4->5->None
    
    This function to fix this issue 
    '''
    def fix_none(self):
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
    l4 = ListNode([1, 2, None])
    l5 = ListNode([1, 2, 3, 4, 5, None])
    print(l1 == l2)
    print(l3)
    print(l4.to_list())
    print(l5)