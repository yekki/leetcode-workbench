from common import Problem
from structure import TreeNode, Tree

#TODO
class Solution(Problem):
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        elif p is not None and q is None:
            return False
        elif q is not None and p is None:
            return False
        elif p.val!=q.val:
            return False
        else:
            l=self.isSameTree(p.left,q.left)
            r=self.isSameTree(p.right,q.right)
        return l and r#取两个结果的与

    def prepare_case(self, case):
        case['params'][0] = Tree(case['params'][0]).root
        case['params'][1] = Tree(case['params'][1]).root


if __name__ == '__main__':
    Solution.test(__file__)