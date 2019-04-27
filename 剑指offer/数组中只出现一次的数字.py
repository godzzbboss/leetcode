# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""


class Solution:
    def test(self, array):
        """array中除了两个数字只出现一次之外，其他数字都出现两次
            思路：1.用一个字典保存每个数字出现的次数，然后找出出现次数为1的数字
        """
        if len(array) < 4:
            return []
        d = {}
        for num in array:
            if num not in d.keys():
                d[num] = 1
            else:
                d[num] += 1
        res = []
        for num in array:
            if d[num] == 1:
                res.append(num)

        return res

    """
        
    
    """




if __name__ == "__main__":
    pass