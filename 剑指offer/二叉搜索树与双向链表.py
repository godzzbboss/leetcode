# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

import copy

class Solution:
    """
        因为要在递归的过程中生成双向链表，所以需要有两个方法
        一个方法用来递归，一个方法用来调用包含递归的方法
        此处不用深拷贝，因为最终想要的就是最后一次递归的结果，如果深拷贝了，最终返回的是本层递归的结果，即None
    """



    def test(self, root): # root 为二叉搜索树的根节点
        dlrear = None
        dlrear = self.covert(root, dlrear)

        dlhead = dlrear

        while dlhead and dlhead.left:
            dlhead = dlhead.left

        return dlhead




    def covert(self, root, dlrear):
        if not root:
            return None

        if root.left:
            dlrear = self.covert(root.left, dlrear)

        root.left = dlrear
        if dlrear:
            dlrear.right = root
        dlrear = root

        if root.right:
            dlrear = self.covert(root.right, dlrear)

        return dlrear






if __name__ == "__main__":
    pass