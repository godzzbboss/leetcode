# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""


class Solution():
    def test(self, push_array, pop_array):
        if len(push_array) != len(pop_array):
            return False

        if not push_array and not pop_array:
            return True

        stack = []
        p1 = 0 # 指向push_array的指针
        p2 = 0 # 指向pop_array的指针
        push_len = len(push_array)
        pop_len = len(pop_array)

        while p1 < push_len and p2 < pop_len:
            while p1 < push_len and p2 < pop_len:
                if push_array[p1] == pop_array[p2]: # 如果两个序列的值相等
                    p1 += 1
                    p2 += 1
                else:
                    stack.append(push_array[p1]) # 入栈，直到找到一个和p2指向的值相同的元素
                    p1 += 1

        while stack and p2 < pop_len: # 上面的循环肯定p1走的快，所以此时p2可能小于pop_len
            if stack[-1] == pop_array[p2]: # 如果栈顶元素等于p2指向的元素
                stack.pop()
            p2 += 1

        if stack: # stack不为空
            return False
        return True





if __name__ == "__main__":
    s = Solution()
    push_array = [1,2,3,4,5]
    pop_array = [4,3,5,1,2]
    print(s.test(push_array, pop_array))

