# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""


class Solution:
    def test(self, array, n):
        """
            一个无限的整数数组[1,2,3,4,....], 找出其第n位数，比如[1,2,3,4,5,6,7,8,9,10,11],
            第10位数为1，第11位数为0

        """
        if not array:
            return -1
        if n < 10:
            return n
        digits = 1 # 从一位数开始
        while True:
            if n <= self.helper1(digits) * digits: # 在digits位数中寻找
                start_num = 10 ** (digits - 1) # digits位数的开始数字
                num = start_num + ( n + digits - 1) // digits - 1 #（n+i-1）//i表示 n/i 向上取整, 第n位数在num中
                for i in range(digits - n % digits): # 比如第n位数字为1234的第2位数，1234->12, 然后对10取余 
                    num //= 10
                return num % 10
            else:
                n -= self.helper1(digits) * digits
                digits += 1

    def helper1(self, digits):
        """统计digits位数共有多少个"""
        if digits == 1:
            return 9
        else:
            return 9 * 10 ** (digits - 1)

if __name__ == "__main__":
    array = [i for i in range(1, 17)]
    s = Solution()
    print(s.test(array,8))
