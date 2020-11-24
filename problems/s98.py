from common import Problem


class Solution(Problem):
    def isValidBST(self, root):
        def inOrder(node):
            if not node:
                return []
            return inOrder(node.left) + [node.val] + inOrder(node.right)

        inorder = inOrder(root)

        return len(inorder) == len(set(inorder)) and inorder == sorted(inorder)

    def isValidBST_1(self, root):
        self.prev = None
        def helper(node):
            if not root:
                return True
            if not helper(root.left):
                return False
            if self.prev and self.prev.val >= root.val:
                return False
            self.prev = root
            return helper(root.right)
        return helper(root)

    def _validate(self, input, expected) -> bool:
        return expected == None

'''
public boolean isValid(TreeNode root, Integer min, Integer max) {
  if (root == null) return true;
  if (min != null && root.val <= min) return false;
  if (max != null && root.val >= max) return false;
  
  return isValid(root.left, min, root.val) && isValid(root.right, root.val, max);

'''

if __name__ == '__main__':
    Solution.test(__file__)