# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""


class Solution():
    # method 1 暴力求解，O(n^2)
    # def test(self, x):
    #     len1  = len(x)
    #     # if len1 == 1:
    #     #     return 1
    #     max_len = 0
    #     for i in range(0,len1):
    #         cur_max = 0
    #         s = set()
    #         for j in range(i,len1):
    #             if x[j] not in s:
    #                 s.add(x[j])
    #                 cur_max += 1
    #             else:
    #                 break
    #         if cur_max > max_len:
    #             max_len = cur_max
    #     return max_len

    # method 2, 滑动窗口法，O（n）
    def test(self, s):
        """给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度"""
        if not s:
            return 0
        p1, p2 = 0, 0
        d = {} # 定义一个字典用来保存每个字符的位置
        res = 0 # 保存最长子串的长度
        while p2 < len(s):
            if s[p2] not in d:
                d[s[p2]] = p2
            else:
                p1 = max(p1, d[s[p2]] + 1) # error: p1 = d[s[p2]] + 1, 这样可能会造成指针p1回溯
                d[s[p2]] = p2 # 更新s[p2]的新位置
            res = max(res, p2 - p1 + 1)
            p2 += 1
        return res






if __name__ == "__main__":
    s = Solution()
    print(s.test("bc"))

