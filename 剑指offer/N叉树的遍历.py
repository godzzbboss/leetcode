# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""

class TreeNode:
    def __init__(self, val, children):
        self.val = val
        self.children = children # 列表

class Solution:
    def pre_travel(self, root):
        """递归实现"""
        # if not root:
        #     return []
        # result = []
        # result.append(root.val)
        # if root.children:
        #     for i in range(len(root.children)):
        #         result.extend(self.pre_travel(root.children[i]))
        #
        # return result

        """非递归实现"""
        if not root:
            return []
        stack = []
        result = []
        stack.append(root)
        while stack:
            cur = stack.pop()
            result.append(cur.val)

            if cur.children:
                for i in range(len(cur.children)-1, -1, -1):
                    stack.append(cur.children[i])
        return result


    """
        N叉树没有中序遍历
    
    """



    def after_travel(self, root):
        """递归"""
        # if not root:
        #     return []
        # result = []
        #
        # if root.children:
        #     for i in range(len(root.children)):
        #         result.extend(self.after_travel(root.children[i]))
        #
        # result.append(root.val)
        # return result


        """非递归实现"""
        if not root:
            return []
        result = []
        stack = []
        pre = None

        stack.append(root)

        while stack:
            cur = stack[-1]
            if (not cur.children) or (pre and pre in cur.children):
                result.append(cur.val)
                pre = stack.pop()

            else:
                for i in range(len(cur.children)-1, -1, -1):
                    stack.append(cur.children[i])
        return result

    def layer_travel(self, root):
        if not root:
            return []

        queue = []
        result = []

        queue.append(root)

        while queue:
            cur = queue.pop(0)
            result.append(cur.val)

            if cur.children:
                queue.extend(cur.children)
        return result


