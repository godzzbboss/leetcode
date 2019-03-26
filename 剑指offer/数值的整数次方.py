# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""


class Solution():
    # def test(self, base, exponent):
    #     return base ** exponent

    def test(self, base, exponent):
        """快速幂"""
        if base == 0 and exponent < 0:
            return -1
        if exponent == 0:
            return 1
        count = 0
        result = 1
        flag = 0
        if exponent < 0:
            flag = 1
        exponent = abs(exponent)

        while exponent and count < 32:
            if exponent & 1 == 1:
                result *= base
            exponent = exponent >> 1
            base *= base
            count += 1
        if flag == 1:
            result = 1 / result
        return result




if __name__ == "__main__":
    s = Solution()
    print(s.test(2,-5))

