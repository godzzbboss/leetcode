# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""
class TreeLinkNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def test(self, pnode):
        if pnode == None or pnode.parent == None:
            return None
        pnext = None
        if pnode.right != None: # 有右子树
            p1 = pnode.right
            while p1.left:
                p1 = p1.left
            pnext = p1
        else:
            p1 = pnode
            p2 = pnode.parent
            if p1 == p2.left:
                pnext = p2
            else:
                while p2.left != p1 and p2 != None:
                    p1 = p2
                    p2 = p2.parent
                pnext = p2
        return pnext


if __name__ == "__main__":
    pass

