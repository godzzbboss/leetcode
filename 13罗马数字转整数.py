# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""


class Solution():
    def test(self, s):
        maps = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

        # 罗马数字一般小数放在大数右边，放在左边时只能放一个小的数，比如
        # 不能IIV.
        result = 0
        for i in range(len(s)-1):
            if maps[s[i]] < maps[s[i+1]]:
                result -= maps[s[i]]
            else:
                result += maps[s[i]]
        result += maps[s[len(s)-1]] # 最后一个右边没数了，所以肯定是加
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.test("IV"))

