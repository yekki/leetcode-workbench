class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self, values):
        self.root = None

        for v in values:
            self.add(v)

    def root(self):
        self.root

    def add(self, val):  # 二叉树，添加一个元素
        node = TreeNode(val=val)
        if self.root is None:
            self.root = node
            return

        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.left is None:
                cur_node.left = node
                return
            else:
                queue.append(cur_node.left)

            if cur_node.right is None:
                cur_node.right = node
                return
            else:
                queue.append(cur_node.right)

    def preorder(self, node):  # 根左右，递归
        if node is None:
            return
        print(node.val, end=' ')
        self.preorder(node.left)
        self.preorder(node.right)

    # 先序打印二叉树（非递归）
    @staticmethod
    def preorder_traverse(node):
        stack = [node]
        while stack:
            node = stack.pop()
            print(node.val, end=' ')
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

    def inorder(self, node):  # 左根右，递归
        if node is None:
            return
        self.inorder(node.left)
        print(node.val, end=' ')
        self.inorder(node.right)

    def postorder(self, node):  # 左根右，递归
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.val, end=' ')

    # 求二叉树节点个数
    def tree_node_count(self, node):
        if node is None:
            return 0
        nums = self.tree_node_count(node.left)
        nums += self.tree_node_count(node.right)
        return nums + 1

    # 二叉树的最大深度
    @staticmethod
    def btree_depth(node):
        if node is None:
            return 0
        ldepth = Tree.btree_depth(node.left)
        rdepth = Tree.btree_depth(node.right)
        return max(ldepth, rdepth) + 1

    def print(self):
        # 广度优先遍历值
        ls = [self.root]
        pre_ls = []
        data = [[self.root.val]]
        ret = ''

        while ls:
            cur = ls.pop(0)
            if not ls:
                data.append([])
                ls.extend(pre_ls)
            data[-1].extend([cur.left.val if cur.left else None, cur.right.val if cur.right else None])
            pre_ls.extend([cur.left, cur.right])
        data.append([])
        while pre_ls:
            cur = pre_ls.pop(0)
            data[-1].extend([cur.left.val if cur.left else None, cur.right.val if cur.right else None])

        # 阶梯序数
        span_list = []
        for i in range(len(data)):
            if span_list:
                span_list.append(span_list[-1] * 2 + 1)
            else:
                span_list.append(1)

        # 最合适的span长度
        span = 0
        for line_idx, val_list in enumerate(data):
            formatted_val_list = []
            for i, val in enumerate(val_list):
                str_val = str(val) if val is not None else ""
                span = span if span >= len(str_val) else len(str_val)
                if line_idx == 0:
                    formatted_val_list.append(str_val)
                else:
                    formatted_val_list.append(str_val)
            data[line_idx] = formatted_val_list
        c_span = span + 2

        # 格式化
        char_val_print_list = []
        formatted_val_print_list = []
        for line_idx, formatted_val_list in enumerate(data):
            char_val_list = [''] * len(formatted_val_list)
            for i, formatted_val in enumerate(formatted_val_list):
                two_space_formatted_val = ' ' * c_span if not formatted_val else ' ' + formatted_val + ' '
                formatted_val_list[i] = two_space_formatted_val
                if formatted_val:
                    if i % 2 == 0:
                        # 左侧节点
                        char = ' ' * (len(two_space_formatted_val) - 1) + '/'
                    else:
                        # 右侧节点
                        char = '\\' + ' ' * (len(two_space_formatted_val) - 1)
                    char_val_list[i] = char
                else:
                    char_val_list[i] = ' ' * c_span
            if line_idx != 0:
                char_val_print_list.append(char_val_list)
            formatted_val_print_list.append(formatted_val_list)

        # 打印
        center_length = span_list[-1] * c_span
        for line_idx, formatted_val_list in enumerate(formatted_val_print_list):
            num = span_list[-1 * line_idx - 1]
            mid_span = " " * (c_span * num)
            formatted_val_str = mid_span.join(formatted_val_list)
            print(formatted_val_str.center(center_length, " "))
            if line_idx < len(char_val_print_list):
                num = span_list[-1 * line_idx - 1 - 1]
                mid_span = " " * c_span * num
                char_val_str = mid_span.join(char_val_print_list[line_idx])
                print(char_val_str.center(center_length, " "))


if __name__ == '__main__':
    values = [5, 1, 4,None, None, 3, 6]
    tree = Tree(values)
    tree.print()