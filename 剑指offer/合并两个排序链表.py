# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""

class LinkedNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    # def test(self, head1, head2):
    #     if head1 is None:
    #         return head2
    #     if head2 is None:
    #         return head1
    #
    #     # newhead = LinkedNode("")
    #     if head1.val < head2.val:
    #         newhead = head1
    #         newhead.next = self.test(head1.next, head2)
    #     else:
    #         newhead = head2
    #         newhead.next = self.test(head1, head2.next)
    #
    #     return newhead


    """
        非递归

    """

    def test(self, head1, head2):
        if head1 is None:
            return head2
        if head2 is None:
            return head1

        root = LinkedNode(-1) # 新链表的头结点
        rear = root # 尾节点
        while head1 and head2:
            if head1.val < head2.val:
                rear.next = head1
                rear = rear.next
                head1 = head1.next
            else:
                rear.next = head2
                rear = rear.next
                head2 = head2.next
        if head1 is None: # 将head2剩余部分进行链接
            rear.next = head2
        elif head2 is None: # 将head2剩余部分进行链接
            rear.next = head1
        return root






if __name__ == "__main__":
    s = Solution()
    print(s.test())

