from collections import deque


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self, values=None):
        if not values:
            return None
        self.root = TreeNode(values[0])
        queue = deque([self.root])
        leng = len(values)
        nums = 1
        while nums < leng:
            node = queue.popleft()
            if node:
                node.left = TreeNode(values[nums]) if values[nums] else None
                queue.append(node.left)
                if nums + 1 < leng:
                    node.right = TreeNode(values[nums+1]) if values[nums+1] else None
                    queue.append(node.right)
                    nums += 1
                nums += 1

    def bfs(self):
        ret = []
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if node:
                ret.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        return ret

    def pre_traversal(self):
        ret = []

        def traversal(head):
            if not head:
                return
            ret.append(head.val)
            traversal(head.left)
            traversal(head.right)
        traversal(self.root)
        return ret

    def in_traversal(self):
        ret = []

        def traversal(head):
            if not head:
                return
            traversal(head.left)
            ret.append(head.val)
            traversal(head.right)

        traversal(self.root)
        return ret

    def post_traversal(self):
        ret = []

        def traversal(head):
            if not head:
                return
            traversal(head.left)
            traversal(head.right)
            ret.append(head.val)

        traversal(self.root)
        return ret

    def print(self):
        # 广度优先遍历值
        ls = [self.root]
        pre_ls = []
        data = [[self.root.val]]

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
    values = [5, 1, 4, None, None, 3, 6]
    tree = Tree(values)
    print(tree.bfs())
    tree.print()