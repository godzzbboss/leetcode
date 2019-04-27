# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""


class Solution:
    def test(self, s):
        if not s:
            return -1
        d = {}
        for item in s:
            if item not in d.keys():
                d[item] = 1
            else:
                d[item] += 1
        for idx, item in enumerate(s):
            if d[item] == 1:
                return idx

        return -1

if __name__ == "__main__":
    s = Solution()
    print(s.test("abda"))