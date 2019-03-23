# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""


class Solution():
    # method 1 暴力求解，O(n^3)
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
    def test(self, x):
        pass




if __name__ == "__main__":
    s = Solution()
    print(s.test("bc"))

