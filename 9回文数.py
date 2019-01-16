# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""
class Solution():

    """
        方法1最快
    """

    # method 1
    def test(self, x):
        x = str(x)
        head = 0
        tail = len(x)-1
        while(head < tail):
            if x[head] != x[tail]:
                return False
            else:
                head+=1
                tail-=1
        return True

    # method 2
    # def test(self, x):
    #     """
    #         不将其转换为字符串,而且只比较一半的数，时间复杂度为O（log10^n）,n为整数的长度
    #     :param x:
    #     :return:
    #     """
    #     if x < 0 or (x % 10 == 0 and x != 0):
    #         return False
    #     s = 0
    #     while x > s:
    #         s = s * 10 + x % 10
    #         x = x // 10
    #     return x == s or x == s // 10 # x==s当整数长度为偶数

    # method 3
    # def test(self, x):
    #     if x < 0:
    #         return False
    #     s = str(x)[::-1]
    #     return True if s == str(x) else False

    # method 4
    # def test(self, x):
    #     if x >= 0 and str(x)[::-1] == str(x):
    #         return True
    #     else:
    #         return False

if __name__ == "__main__":
    s = Solution()
    print(s.test(-121))



