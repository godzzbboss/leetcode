# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""
class LinkedNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution():
    def test(self, head):
        if head == None:
            return None
        if head.next == None:
            return head
        p = head
        pre = None
        # 反转链时要一个一个的反转， 先移动pre,再移动p
        while p != None:
            t_p = p.next # 保存p.next
            p.next = pre
            pre = p
            p = t_p
        return pre


    """
        递归实现, python版本递归实现超时
    
    """
    def test(self, head):
        if head is None or head.next is None:
            return head

        result = self.test(head.next)
        head.next.next = head
        head.next = None

        return result




if __name__ == "__main__":
    s = Solution()
    print(s.test())

