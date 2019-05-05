# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""


class Solution:
    def test(self, root, target):
        """给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和"""
        if not root:
            return False
        count = 0
        return self.dfs(root, target, count)

    def dfs(self, root, target, count):
        """前序遍历"""
        count += root.val
        if not root.left and not root.right and count == target:
            return True

        l = r = False
        if root.left:
            l = self.dfs(root.left, target, count)
        if root.right:
            r = self.dfs(root.right, target, count)
        return l or r



if __name__ == "__main__":
    pass