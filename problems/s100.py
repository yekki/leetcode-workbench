from common import Problem
from structure import TreeNode

#TODO
class Solution(Problem):
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # if p is None and q is None:
        #     return True
        # if p is None and q is not None:
        #     return False
        # if p is not None and q is None:
        #     return False
        #
        # if p.val == q.val:
        #     return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False

    def _validate(self, input, expected) -> bool:
        #result = self.isSameTree(TreeNode(input['p1']), TreeNode(input['p2']))
        return True
        #return result == expected


if __name__ == '__main__':
    Solution.test(__file__)