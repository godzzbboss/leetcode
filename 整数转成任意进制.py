# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""


class Solution():
    def test(self, x, base):
        covert_string = "0123456789ABCDEF"
        if x < base:
            return covert_string[x]
        else:
            return self.test(x//base, base) + covert_string[x % base]



if __name__ == "__main__":
    s = Solution()
    print(s.test(10,2))

