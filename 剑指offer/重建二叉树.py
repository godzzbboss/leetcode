# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) != len(tin) or len(pre) == 0 or len(tin) == 0:
            return None
        l = len(pre)
        # 构建根节点
        root = TreeNode(pre[0])
        # 是否只有一个节点
        if len(pre) == 1:
            if tin[0] != pre[0]:
                return None
            else:
                return root
        # 找到根节点在中序序列中的位置
        # root_idx = 0
        # while tin[root_idx] != pre[0]:
        #     root_idx += 1
        root_idx = tin.index(pre[0]) # 根节点索引位置
        left_len = root_idx  # 左子树节点个数
        if left_len > 0:
            # 构建左子树
            root.left = self.reConstructBinaryTree(pre[1: 1 + root_idx], tin[0: root_idx])
        if l - left_len - 1 > 0:
            # 构建右子树
            root.right = self.reConstructBinaryTree(pre[root_idx + 1:], tin[root_idx + 1:])
        return root


if __name__ == "__main__":
    solution = Solution()
    a = [1, 2, 4, 7, 3, 5, 6, 8]
    b = [4, 7, 2, 1, 5, 3, 8, 6]
    s = solution.reConstructBinaryTree(a, b)
    print(s.right.left)
