from common import Problem
from structure import Tree, TreeNode

#TODO
class Solution(Problem):
    def isValidBST(self, root: TreeNode) -> bool:
        def inOrder(node):
            if not node:
                return []
            return inOrder(node.left) + [node.val] + inOrder(node.right)

        inorder = inOrder(root)

        return len(inorder) == len(set(inorder)) and inorder == sorted(inorder)

    def _validate(self, input, expected) -> tuple:
        tree = Tree(input)
        result = self.isValidBST(tree.root)
        return expected == result, result


if __name__ == '__main__':
    Solution.test(__file__)