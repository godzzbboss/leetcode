# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution():
    def test(self, head, k):
        if head is None:
            return None
        # 链表长度
        length = 0
        p = head
        while p:
            length += 1
            p = p.next
        if k > length:
            return None

        p1 = head
        p2 = head
        for i in range(k): # p1先走k步
            p1 = p1.next
        while p1 and p2: # 然后一起走
            p1 = p1.next
            p2 = p2.next
        return p2


if __name__ == "__main__":
    s = Solution()
    print(s.test())

