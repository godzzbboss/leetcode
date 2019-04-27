# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def test(self, root):
        """层次遍历每一个节点，判断以其为根的子树是否是平衡的"""
        if not root:
            return True
        queue = []
        queue.append(root)

        while queue:
            cur = queue.pop(0) # 队头出列
            if self.is_balance(cur):
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            else:
                return False

        return True

    def is_balance(self, root):
        """判断以root为根节点的子树是否是平衡二叉树"""
        if not root: # 空树也是平衡二叉树
            return True
        left_height = self.get_tree_height(root.left)
        right_height = self.get_tree_height(root.right)
        if abs(left_height - right_height) <= 1:
            return True

        return False

    def get_tree_height(self, root):
        if not root:
            return 0
        left_height = self.get_tree_height(root.left)
        right_height = self.get_tree_height(root.right)

        return max(left_height,right_height) + 1



if __name__ == "__main__":
    pass