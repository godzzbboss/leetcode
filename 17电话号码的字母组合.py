# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""
"""
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""
class Solution:
    # def letterCombinations(self, digits):
    #     digits = list(digits)
    #     if not digits:
    #         return []
    #     res = [""]
    #     num_map = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    #     for d in digits:
    #         new_res = []
    #         for r in res:
    #             for c in num_map[int(d)]:
    #                 new_res.append(r+c)
    #         res = new_res
    #     return res

    """用dfs来做"""
    num_map = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    res = [""]
    def letterCombinations(self, digits):
        if not digits:
            return []
        self.dfs(digits, 0)
        return self.res

    def dfs(self, digits, u):
        if u == len(digits):
            return
        new_res = []
        for r in self.res:
            for c in self.num_map[int(digits[u])]:
                new_res.append(r + c)
        self.res = new_res
        self.dfs(digits, u+1)



s = Solution()
digits = "23"
print(s.letterCombinations(digits))

