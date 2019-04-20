# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""


class Solution:
    def test(self, array):
        """判断array是否是二叉搜索树的后序遍历序列"""
        if not array:
            return False
        root = array[-1]
        i = 0
        while array[i] < root: # 找到第一个大于根节点的节点
            i += 1
        j = i
        while j < len(array) - 1: # 查找右子树中是否有小于root的点
            if array[j] < root:
                return False
            j += 1

        # 如果左子树不为空，检查左子树是否是二叉搜索树的后序遍历数列
        if i > 0:
            self.test(array[0:i])

        if len(array) - 1 - i: # 右子树不为空
            self.test(array[i: len(array)-1])

        return True



if __name__ == "__main__":
    pass