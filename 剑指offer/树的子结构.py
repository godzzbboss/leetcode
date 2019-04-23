# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution():
    def test(self, root1, root2):
        if not root1 or not root2:
            return False
        result = False
        if root1.val == root2.val: # 根节点值相同
            result = self.is_tree1_has_tree2(root1, root2)
        if not result: # 判断tree1的左子树中是否包含tree2
            result = self.test(root1.left, root2)
        if not result: # 判断tree1的右子树中是否包含tree2
            result = self.test(root1.right, root2)

        return result

    def is_tree1_has_tree2(self, root1, root2):
        if not root2: # tree2遍历完了
            return True
        if not root1: # tree2没遍历完，tree1却遍历完了
            return False

        if root1.val != root2.val:
            return False
        # root1.val == root2.val
        return self.is_tree1_has_tree2(root1.left, root2.left) and self.is_tree1_has_tree2(root1.right, root2.right) # tree1的左子树和右子树必须包含tree2的左子树和右子树







if __name__ == "__main__":
    s = Solution()
    print(s.test())

