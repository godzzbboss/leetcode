# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""

class LinkNode:
    def __inti__(self, val):
        self.val = val
        self.next = None

class Solution():
    def test(self, head):
        if head is None or head.next is None:
            return head
        phead = LinkNode("a") # 创建一个头结点
        phead.next = head
        p = phead
        while p:
            while p.next and p.val != p.next.val: #找到重复元素的第一个位置
                pre = p # p的前驱
                p = p.next
            q = p
            while q and q.val == p.val: # 找到不等于p的第一个节点
                q = q.next
            if q is None:
                if p.next is None: # 说明p指向链表最后一个节点, 后面没重复元素
                    return phead.next
                else:
                    pre.next = None
                    return phead.next
            pre.next = q
            p = q


if __name__ == "__main__":
    s = Solution()
    print(s.test())

