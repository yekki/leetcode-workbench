class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __init__(self, values):
        self.val = TreeNode([values[0]])
        self.left = None if values[1] is None else TreeNode(values[1])
        self.right = None if values[1] is None else TreeNode(values[2])

class Bitree:
    def __init__(self, root=None):
        self.root: int = root

    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False

    def pre_order(self, treenode):
        if treenode is None:
            return

        print(treenode.val)
        self.pre_order(treenode.left)
        self.pre_order(treenode.right)

    def in_order(self, treenode):

        if treenode is None:
            return

        self.in_order(treenode.left)
        print(treenode.val)
        self.in_order(treenode.right)

    def post_order(self,treenode):

        if treenode is None:
            return

        self.post_order(treenode.left)
        self.post_order(treenode.right)
        print(treenode.val)


if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2, n1)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5, n3, n4)
    n6 = TreeNode(6, n2, n5)
    n7 = TreeNode(7, n6)
    n8 = TreeNode(8)
    root = TreeNode('root', n7, n8)

    bt = Bitree(root)
    print('preOrder......')
    print(bt.pre_order(bt.root))
    print('inOrder......')
    print(bt.in_order(bt.root))
    print('postOrder.....')
    print(bt.post_order(bt.root))
