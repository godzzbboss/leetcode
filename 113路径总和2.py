# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""


class Solution:
    def test(self, root, target):
        """给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径"""
        if not root:
            return []
        res = []
        path = []
        self.dfs(root, target, path, res)
        return res

    def dfs(self, root, target, path, res):
        """前序遍历生成结果"""
        path.append(root.val)
        if not root.left and not root.right and root.val == target:
            res.append(path)

        else:
            if root.left:
                self.dfs(root.left, target - root.val, path[:], res)
            if root.right:
                self.dfs(root.right, target - root.val, path[:], res)


if __name__ == "__main__":
    pass