# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""


class Solution:
    def test(self, s):
        """翻转单词序列"""
        if len(s) <= 1:
            return s
        s = self.reverse(s, 0, len(s) - 1)
        res = []
        p1 = 0 # 一个单词的头部
        p2 = 0 # 一个单词的尾部
        # 把每一个单词翻转
        while p1 <= p2 and p2 < len(s):
            while p1 <= p2 and p2 < len(s) and s[p1] == " ":
                res.append(s[p1])
                p1 += 1
                p2 += 1
            while p1 <= p2 and p2 < len(s) and s[p2] != " ": # 找到一个单词的结尾
                p2 += 1
            s_ = self.reverse(s, p1, p2-1)
            res.extend(list(s_))
            p1 = p2

        return "".join(res)


    def reverse(self, s, start, end):
        return s[start: end+1][::-1]


if __name__ == "__main__":
    sol = Solution()
    s = "i am a student!"
    print(sol.test(s))