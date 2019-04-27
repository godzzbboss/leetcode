# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""


class Solution:
    def test(self, s, n):
        """循环左旋转字符串n位"""
        if n <= 0 or len(s) <= 1 or n % len(s) == 0:
            return s
        s = self.reverse(s, 0, len(s) - 1)
        s1 = self.reverse(s, 0, (len(s) - n - 1) % len(s))
        s2 = self.reverse(s, (len(s) - n - 1) % len(s) + 1, len(s)-1)

        return s1 + s2


    def reverse(self, s, start, end):
        """将s的指定部分进行翻转"""
        return s[start: end+1][::-1]


if __name__ == "__main__":
    s = Solution()
    t = "abcde"
    print(s.test(t, 2))