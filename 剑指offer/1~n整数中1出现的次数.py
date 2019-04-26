# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""


class Solution:
    def test(self, n):
        res = []
        for i in range(n):
            res.append(str(i+1))
        res = "".join(res)
        return res.count("1", 0, len(res))


if __name__ == "__main__":
    s = Solution()
    print(s.test(3))