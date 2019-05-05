# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution():
    # method1
    # def test(self, l1, l2):
    #     if not (l1 and l2):  # l1,l2都为空
    #         return
    #     q = l1
    #     p = l2
    #     result = ListNode(-1)  # 头结点
    #     k = result # 尾插法
    #     carry = 0  # 进位
    #     while q or p:
    #         x = q.val if q else 0  # 如果q不为空，将x赋值为q的值，否则为0
    #         y = p.val if p else 0
    #         sum = x + y + carry
    #         carry = sum // 10 # 更新进位，两个数相加，进位最大为1
    #         cur_val = sum % 10
    #         cur = ListNode(cur_val)
    #         k.next = cur # 将结果插入到result后
    #         k = k.next
    #         if q : q = q.next
    #         if p : p = p.next
    #     if carry == 1:
    #         k.next = ListNode(carry)
    #     return result.next

    # method2
    """
        当一个链表遍历完之后应该只遍历一个链表，而method1增加操作执行次数

    """
    def test(self, l1, l2):
        if not (l1 and l2):  # l1,l2都为空
            return
        q = l1
        p = l2
        result = ListNode(-1)  # 头结点
        k = result
        carry = 0  # 进位
        while q and p:
            x = q.val
            y = p.val
            sum = x + y + carry
            carry = sum // 10 # 更新进位，两个数相加，进位最大为1
            cur_val = sum % 10
            cur = ListNode(cur_val)
            k.next = cur # 将结果插入到result后
            k = k.next
            q = q.next
            p = p.next
        while p:
            y = p.val
            sum = y + carry
            carry = sum // 10
            cur_val = sum % 10
            cur = ListNode(cur_val)
            k.next = cur  # 将结果插入到result后
            k = k.next
            p = p.next
        while q:
            x = q.val
            sum = x + carry
            carry = sum // 10
            cur_val = sum % 10
            cur = ListNode(cur_val)
            k.next = cur  # 将结果插入到result后
            k = k.next
            q = q.next
        if carry == 1:
            k.next = ListNode(carry)
        return result.next


if __name__ == "__main__":
    pass
