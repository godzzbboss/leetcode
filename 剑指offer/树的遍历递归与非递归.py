# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def pre_travel(self, root):
        """前序遍历"""
        if not root:
            return []
        stack = []
        result = []
        cur = root
        while cur or len(stack) != 0:
            result.append(cur.val) # 先输出
            stack.append(cur) # 再入栈
            cur = cur.left # 指向左孩子
            while cur is None and len(stack) != 0: # 如果左孩子为空，一次判断右孩子，直至找到一个不为空的右孩子
                cur = stack.pop()
                cur = cur.right
        return result



    def in_travel(self, root):
        """中序遍历"""
        if not root:
            return []
        stack = []
        result = []
        cur = root
        while cur or len(stack) != 0:  # 当cur和栈都为空时才跳出循环，第一次循环时栈为空，cur不为空；在循环的时候可能cur为空，栈不为空
            if cur.left:  # 最左节点不入栈
                stack.append(cur)
                cur = cur.left
            else:
                result.append(cur.val)  # cur的左子树为空，则输出cur
                cur = cur.right  # 并将cur指向其右子树
                while cur is None and len(stack) != 0:  # 如果当前节点的右子树为空，并且栈不为空
                    cur = stack.pop() # 指向当前节点的父节点
                    result.append(cur.val)  # 访问父节点
                    cur = cur.right # 指向父节点的右子树

        return result


    def after_travel(self, root):
        """后序遍历"""
        if not root:
            return []
        stack = []
        result = []
        pre = None # 指向上一次访问的节点
        stack.append(root)
        while len(stack) != 0:
            cur = stack[-1] # cur指向栈顶元素
            if (not cur.left and not cur.right) or \
                    (pre and (pre is cur.left or pre is cur.right)): # 左右孩子都为空或者左右孩子都已经访问过，则访问根节点
                result.append(cur.val)
                cur = stack.pop()
                pre = cur # pre指向上一个访问的节点
            else:
                if cur.right: # 右节点先入栈
                    stack.append(cur.right)
                if cur.left: # 左节点再入栈
                    stack.append(cur.left)

        return result

    def layer_travel(self, root):
        """层次遍历"""
        if not root:
            return []
        queue = []
        result = []
        queue.append(root) # 根节点入队
        while queue:
            cur = queue.pop(0) # 队列的第0个元素
            result.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)

        return result














