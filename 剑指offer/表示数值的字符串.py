# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""


class Solution():
    def test(self, s):
        hasE = False # 是否含有e,E
        decimal = False # 是否含有小数点
        sign = False # 是否含有正负号

        if len(s) == 0:
            return False
        for i in range(len(s)):
            if s[i] == "e" or s[i] == "E":
                if hasE: return False # 一个数中只能含一个e
                if i == len(s) - 1: return False # e出现在字符串最后
                hasE = True
            elif s[i] == "+" or s[i] == "-":
                if sign and s[i-1] != "e" and s[i-1] != "E": # 正负号第二次出现必须在e后
                    return False
                if not sign and i > 0 and s[i-1] != "e" and s[i-1] != "E": # 正负号第一次出现必须在开头，或者e后
                    return False
                sign = True
            elif s[i] == ".":
                if decimal: return False # 小数点不能出现两次
                if hasE: return False # 不能出现在e后
                decimal = True
            elif s[i] < "0" or s[i] > "9":
                return False

        return True




if __name__ == "__main__":
    s = Solution()
    print(s.test("-.123"))

