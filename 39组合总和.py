# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""


class Solution:

    def combinationSum(self, candidates, target):
        if not candidates:
            return []
        res = []

        def dfs(candidates, target, path):
            # 找到一条路径
            if target == sum(path):
                temp = sorted(path)
                if temp not in res:
                    res.append(temp)
                return

            if sum(path) < target :
                for i in range(len(candidates)):
                    path_ = path.copy()
                    path_.append(candidates[i])
                    dfs(candidates, target, path_)

        dfs(candidates, target, [])
        return res

if __name__ == "__main__":
    s = Solution()
    candidates = [8,7,4,3]
    target = 11
    print(s.combinationSum(candidates, target))