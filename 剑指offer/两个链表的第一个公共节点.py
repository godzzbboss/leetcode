# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    def test(self, head1, head2):
        """先求出两个链表的长度，让长的链表先走长度差步"""
        if head1 == None or head2 == None:
            return None
        len1, len2 = 0, 0
        p1, p2 = head1, head2
        while p1:
            len1 += 1
            p1 = p1.next
        while p2:
            len2 += 1
            p2 = p2.next
        diff = abs(len1 -  len2)
        if len1 >  len2:
            while diff:
                head1 = head1.next
                diff -= 1
        else:
            while diff:
                head2 = head2.next
                diff -= 1
        while head1 and head2:
            if head1.val == head2.val:
                return head1
            head1 = head1.next
            head2 = head2.next
        return None




if __name__ == "__main__":
    s = Solution()
    print(s.test())

