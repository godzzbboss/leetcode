# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""

class LinkNode:
    def __inti__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    def deleteDuplication(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
             return None
        dummy = LinkNode("a") # 虚拟头节点
        dummy.next = head
        p = dummy
        while p.next:
            q = p.next
            while q and p.next.val == q.val: q = q.next

            if p.next.next == q:
                p = p.next
            else:
                p.next = q
        return dummy.next





if __name__ == "__main__":
    s = Solution()
    print(s.test())

