# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s = " " + s
        p = " " + p
        s_len = len(s)
        p_len = len(p)
        f = [[False] * (p_len+10) for i in range(s_len+10)] # f[i][j]表示s的前i个字符与p的前j个字符是否匹配
        f[0][0] = True
        for i in range(0, s_len):
            for j in range(1, p_len):
                if i >= 1 and (s[i] == p[j] or p[j] == "."):
                    f[i][j] = f[i][j] or f[i-1][j-1]
                if p[j] == "*":
                    if j >= 2: # *匹配0个前面字符
                        f[i][j] = f[i][j] or f[i][j-2]
                    if i >= 1 and (s[i] == p[j-1] or p[j-1] == "."):
                        f[i][j] = f[i][j] or f[i-1][j]
        return f[s_len-1][p_len-1]

s = Solution()
a = "mississippiaababmississippiaababmississippiaababmississippiaababissippiaabbmississippiaababmississippiaababmissmississippiaababmississippiaababmississippiaababmississippiaababissippiaabbmississippiaababmississippiaababmiss"
b = "mis*is*ip*.c*a*b.*mis*is*ip*.c*a*b.*mis*is*ip*.c*a*b.*mis*is*ip*.c*a*b.*is*ip*.c*a*bb.*mis*is*ip*.c*a*b.*mis*is*ip*.c*a*b.*mis*mis*is*ip*.c*a*b.*mis*is*ip*.c*a*b.*mis*is*ip*.c*a*b.*mis*is*ip*.c*a*b.*is*ip*.c*a*bb.*mis*is*ip*.c*a*b.*mis*is*ip*.c*a*b.*mis*"
print(s.isMatch(a,b))



