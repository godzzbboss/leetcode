# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""


class Solution():
    def test(self, root):
        """返回二叉树的镜像"""
        if not root:
            return root

        root.left, root.right = root.right, root.left

        self.test(root.left)
        self.test(root.right)

        return root






if __name__ == "__main__":
    s = Solution()
    print(s.test())

