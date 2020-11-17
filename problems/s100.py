from common import AbstractSolution
from structure.tree_node import TreeNode


class Solution(AbstractSolution):
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p is None and q is not None:
            return False
        if p is not None and q is None:
            return False

        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False

    #TODO bug
    def _validate(self, input, expected) -> bool:
        result = self.isSameTree(TreeNode(input['p1']), TreeNode(input['p2']))

        return result == expected