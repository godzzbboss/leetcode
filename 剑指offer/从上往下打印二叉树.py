# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""


class Solution():
    def test(self, root):
        """从上往下打印二叉树，层次遍历解决"""
        if not root:
            return []
        queue = []
        result = []
        queue.append(root)

        while queue:
            cur = queue.pop(0)
            result.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return result



if __name__ == "__main__":
    s = Solution()
    print(s.test())

