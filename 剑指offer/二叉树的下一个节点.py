# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""


# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.father = None


class Solution:
    def Getfather(self, pnode):
        # write code here
        # 当前节点有右节点
        pnext = TreeLinkNode(None)
        pright = pnode.right
        if pright:
            while pright.left:
                pright = pright.left
            pnext = pright

        # 当前节点无有右节点
        else:
            pcurrent = pnode
            pfather = pnode.father
            # 当前节点是其父节点的左孩子
            if pfather and pfather.left == pcurrent:
                pnext = pfather
            # 当前节点是其父节点的右孩子
            else:
                while pfather and pfather.left != pcurrent:
                    pcurrent = pfather
                    pfather = pfather.father
                pnext = pfather
        return pnext