# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""
import scipy.linalg.decomp_svd
class Solution():
    def test(self, A):
        # method 1
        # if len(A) == 0:
        #     return
        # B = []
        # for i in range(len(A[0])): # 列
        #     row = []
        #     for j in range(len(A)): # 行
        #         row.append(A[j][i])
        #     B.append(row)
        # return B

        # method 2
        # rows = len(A)
        # cols = len(A[0])
        # B = [[] for i in range(cols)]
        # for i in range(rows):
        #     for j in range(cols):
        #         B[j].append(A[i][j])
        # return B

        # method 3
        return [ list(i) for i in zip(*A)]

if __name__ == "__main__":
    s = Solution()
    print(s.test([[1,2,3],[4,5,6]]))


