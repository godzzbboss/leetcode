# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    def test(self, head):

        result = self.has_circle(head)
        if result: # 存在环
            p1 = result
            p2 = head
            while p1.val != p2.val:
                p1 = p1.next
                p2 = p2.next

            return p1

        return result

    def has_circle(self, head):
        """判断链表是否有环，无环返回None,有环返回快慢指针的相遇节点"""
        if head is None or head.next is None or head.next.next is None:
            return None
        slow = head.next
        fast = head.next.next
        while slow.val != fast.val:
            if slow.next is not None and fast.next.next is not None: # 赋值的时候先判断
                slow = slow.next
                fast = fast.next.next
            else:
                return None

        return slow


if __name__ == "__main__":
    s = Solution()
    print(s.test())

