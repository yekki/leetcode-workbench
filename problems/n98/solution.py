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

    def prepare_case(self, case_no):
        data = self.get_case(case_no)
        data['params'] = Tree(data['params'])

        return data


if __name__ == '__main__':
    Solution.test(__file__)