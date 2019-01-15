# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""
class Solution():
    def sort_array_by_parity(self, array):
        if len(array) == 0:
            return
        else:
            even = [i for i in array if i % 2 == 0]
            odd = [i for i in array if i % 2 == 1]
            A = [n for i in zip(even, odd) for n in i ]
            return A

if __name__ == "__main__":
    test = Solution()
    print(test.sort_array_by_parity([1,2,4,5]))

