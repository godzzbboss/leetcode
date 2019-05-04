# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""


class Solution:
    def test(self, root, k):
        """中序遍历二叉树，第k个节点即为第k大节点"""
        count = 0
        return self.in_order(root, k, count)

    def in_order(self, root, k, count):
        if not root or k == 0:
            return count, None

        count, l = self.in_order(root.left, k, count) # 为什么要return count？？？
        if l:
            return count, l
        count += 1 #
        if count == k:
            return count, root

        count, r = self.in_order(root.right, k, count)
        return count, r # 注意这个地方，不管r是否为空都返回，返回空说明没找到第k个节点

if __name__ == "__main__":
    pass