# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""

import functools

class Solution:
    def test(self, array):
        if not array:
            return None
        array.sort(key=functools.cmp_to_key(self.cmp))
        array = map(str, array)
        return int("".join(array))


    def cmp(self, num1, num2):
        str1 = str(num1) + str(num2)
        str2 = str(num2) + str(num1)

        if str1 < str2:
            return -1
        elif str1 > str2:
            return 1
        else:
            return 0



if __name__ == "__main__":
    s = Solution()
    array = [4,3,2,1]
    print(s.test(array))