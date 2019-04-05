# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""


class Solution():
    def test(self, root, target):
        """给定链表头结点和任意一个节点，在O（1）时间内删除这个节点"""
        if not root: # root为空
            return
        if root.next is None and root is target: #只有一个节点且相等
            return
        if not target: # target为空
            return root

        if target.next is None: # target为尾节点
            cur = root
            pre = None
            while cur:
                if cur is not target:
                    pre = cur
                    cur = cur.next
            pre.next = None
            return root

        cur = target.next
        target.val, cur.val = cur.val, target.val
        target.next = cur.next
        return root







if __name__ == "__main__":
    s = Solution()
    print(s.test())

