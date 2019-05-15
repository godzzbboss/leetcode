# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""


class Solution:
    def test(self, root, k):
        """中序遍历二叉树，第k个节点即为第k大节点"""
        if not root or k <= 0:
            return None
        count = 0
        return self.in_order(root, k, count)[0]

    def in_order(self, root, k, count):
        if not root or k <= 0:
            return None
        target, count = self.in_order(root.left, k, count)
        if target:
            return target, count
        count += 1
        if count == k:
            return root, count
        target, count = self.in_order(root.right, k, count)
        return target, count

if __name__ == "__main__":
    pass