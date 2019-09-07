# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    flag = False

    def hasPathSum(self, root, sum):
        if not root:
            return False
        self.dfs(root, sum, 0)
        return self.flag

    def dfs(self, root, sum, count):
        """
            count记录当前路径之和
        """
        # 遍历到叶节点，即找到一条路径
        if not root.left and not root.right:
            count += root.val
            if count == sum:
                self.flag = True
            return
        # 没有找到一条合法路径
        if not self.flag:
            count += root.val
            if root.left:
                self.dfs(root.left, sum, count)
            if root.right:
                self.dfs(root.right, sum, count)
            count -= root.val  # 回溯恢复现场


if __name__ == "__main__":
    pass