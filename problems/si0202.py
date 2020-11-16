from common import AbstractSolution, ListNode


class Solution(AbstractSolution):
    def kthToLast(self, head: ListNode, k: int) -> int:
        l = list()
        while head is not None:
            l.append(head.val)
            head = head.next

        return l[-k]

    def _validate(self, input, expected) -> bool:
        result = self.kthToLast(ListNode(input["p1"]), input["p2"])

        return expected == result


'''
class Solution {
public:
    int kthToLast(ListNode* head, int k) {        
        ListNode* fast = head;
        ListNode* slow = head;

        while(fast != nullptr)
        {
            fast = fast->next;
            if(k == 0)
            {
                slow = slow->next;
            }
            else
            {
                k--;
            }
        }
        return slow->val;
    }
};

'''