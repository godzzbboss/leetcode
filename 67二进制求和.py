# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""


class Solution():
    # method 1
    # def test(self, a, b):
    #     carry = 0 # 进位
    #     len1 = len(a)
    #     len2 = len(b)
    #     point1 = len1 -1
    #     point2 = len2 -1
    #     result = []
    #     while(point1 >= 0 or point2 >= 0):
    #         x = a[point1] if point1 >=0 else 0
    #         y = b[point2] if point2 >= 0 else 0
    #         sum = carry + int(x) + int(y)
    #         cur = sum % 2
    #         carry = sum // 2
    #         result.insert(0, cur)
    #         point1 -= 1
    #         point2 -= 1
    #     if carry == 1:
    #         result.insert(0, carry)
    #     s = ""
    #     for i in result:
    #         s += str(i)
    #     return s

    # method 2
    def test(self, a, b):
        # 直接对2进制求和相当于先将2进制转为10进制求和，然后再将10进制变为2进制
        return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == "__main__":
    s = Solution()
    a = "111"
    b = "111"
    print(type(s.test(a,b)))

