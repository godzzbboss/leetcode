# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""


class Solution():
    def test(self, x):
        flag = 0
        if x < 0:
            flag = 1
        x = abs(x)
        result = 0
        while x > 0:
            result = result * 10 + x % 10
            x = x // 10
        result = result if flag == 0 else -result
        # 判断是否越界
        if result > 2**31 - 1 or result < -2**31:
            return 0
        return result



if __name__ == "__main__":
    s = Solution()
    print(s.test(123))

