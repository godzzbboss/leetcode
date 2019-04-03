# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""


class Solution():
    def test(self, root):
        if not root:
            return []
        queue = []
        result = []

        queue.append(root)
        count = 1 # 标识第几行
        while queue:
            len_level = len(queue) # 保存每一层节点个数
            sub_result = []
            for i in range(len_level):
                cur = queue.pop(0)
                sub_result.append(cur.val)
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
            if count & 1 == 1:
                result.append(sub_result)
            else:
                result.append(sub_result[::-1])
            count += 1
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.test())

