# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""


class Solution():
    # def test(self, root):
    #     """递归"""
    #     if not root:
    #         return True
    #     return self.compare_left_right(root.left, root.right)
    #
    #
    # def compare_left_right(self, root1, root2):
    #     if not root1 and not root2: # 都为空
    #         return True
    #     if not root1 or not root2: # 有一个为空
    #         return False
    #
    #     if root1.val != root2.val: # 值不相等
    #         return False
    #
    #     result = self.compare_left_right(root1.left, root2.right) and self.compare_left_right(root1.right, root2.left)
    #
    #     return result

    def test(self, root):
        """非递归"""
        if not root:
            return True
        queue = []
        queue.append(root)
        result = True
        while queue and result:
            len_level = len(queue)  # 保存每一层的节点个数
            result = self.is_equal(queue[:len_level], queue[:len_level][::-1])
            for i in range(len_level):  # 保存下一层节点
                cur = queue.pop(0)
                if not cur:
                    continue
                queue.append(cur.left)
                queue.append(cur.right)
        return result

    def is_equal(self, list1, list2):
        """判断两个节点列表的值是否相等"""
        result = True
        for i in range(len(list1)):
            if (not list1[i] and list2[i]) or (not list2[i] and list1[i]):
                result = False
                break
            if not list1[i] and not list2[i]:
                continue
            if list1[i].val != list2[i].val:
                result = False
                break

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.test())

