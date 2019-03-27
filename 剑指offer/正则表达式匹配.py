# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""


class Solution():
    def test(self, s, pattern):

        return self.str_match(s, pattern, 0, 0)



    def str_match(self, s, pattern, s_start, p_start):
        s_len = len(s)
        p_len = len(pattern)

        if s_start == s_len and p_start == p_len: # 匹配成功
            return True
        if s_start != s_len and p_start == p_len:
            return False

        # pattern 的第二位为*
        if p_start + 1 < p_len and pattern[p_start + 1] == "*":
            # 第一位匹配成功
            if s_start < s_len and (s[s_start] == pattern[p_start] or pattern[p_start] == "."):
                # 此时分三种情况，*重复前面的字符0,1，多次
                return self.str_match(s, pattern, s_start, p_start+2) or self.str_match(s, pattern, s_start+1, p_start+2) or\
                       self.str_match(s, pattern, s_start+1, p_start)

            else:
                return self.str_match(s, pattern, s_start, p_start+2)

        else:
            # 第二位不为*,且第一位匹配成功
            if s_start < s_len and (s[s_start] == pattern[p_start] or pattern[p_start] == "."):
                return self.str_match(s, pattern, s_start+1, p_start+1)

        return False






if __name__ == "__main__":
    s = Solution()
    print(s.test())

