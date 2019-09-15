# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""
class Solution:
    #  中心扩展法
    def longestPalindrome(self, s: str) -> str:
        if not s: return ""
        s = list(s)
        start = 0
        end = 0
        for i in range(len(s)):
            l1 = self.expand_length(s, i, i)
            l2 = self.expand_length(s, i, i + 1) # 当原字符串长度为偶数时
            l = max(l1, l2)
            if l > (end - start + 1):
                if l & 1 == 1:  # 奇数
                    start = i - (l - 1) // 2
                    end = i + (l - 1) // 2
                else:
                    start = i - (l - 2) // 2
                    end = i + (l - 2) // 2 + 1
        return "".join(s[start: end + 1])

    def expand_length(self, s, l, r):

        l_ = l
        r_ = r
        while l_ >= 0 and r_ < len(s) and s[l_] == s[r_]:
            l_ -= 1
            r_ += 1

        return r_ - l_ - 1

s = Solution()
s_ = "babad"
print(s.longestPalindrome(s_))
