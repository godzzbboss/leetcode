# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""


class Solution:
    def test(self, s):
        """将字符串转为整数"""
        if not self.check(s):  # 检查s是否合法
            return 0
        flag = 0  # 标记是否为负数
        sign = 0  # 标记是否有符号位
        if s[0] == "-":
            sign = 1
            flag = 1
        if s[0] == "+":
            sign = 1
        if sign:
            if flag:
                return -int(s[1:])
            else:
                return int(s[1:])
        else:
            return int(s)

    def check(self, s):
        if not s:
            return 0
        flag = 0  # 标记是否是符号位
        if s[0] in {"+", "-"}:
            flag = 1
        for i in range(flag, len(s)):
            if s[i] < "0" or s[i] > "9":
                return 0


if __name__ == "__main__":
    s = Solution()
    print(s.test("123"))