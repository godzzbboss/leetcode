# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""
"""
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""
class Solution:
    def letterCombinations(self, digits):
        digits = list(digits)
        if not digits:
            return []
        res = [""]
        num_map = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        for d in digits:
            new_res = []
            for r in res:
                for c in num_map[int(d)]:
                    new_res.append(r+c)
            res = new_res
        return res

s = Solution()
digits = "23"
print(s.letterCombinations(digits))

