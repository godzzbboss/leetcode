# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""

class Solution():
    def test(self, n):
        """大数问题，用字符串或者数组来存储数字"""
        number = [0] * n
        while not self.is_carry(number):
            self.print_num(number)


    def is_carry(self, number):
        "判断是否在number的最高位产生进位"
        carry = 0
        flag = False
        n = len(number)
        for i in range(n-1, -1, -1):
            num = number[i] + carry
            if i == n-1: # 判断是否是最低位
                num += 1

            if num >= 10: # 产生进位
                if i == 0: # 最高位产生进位
                    flag = True
                    return flag
                else:
                    carry = 1 # 产生进位
                    num -= 10 # 置0
                    number[i] = num
            else: # 不产生进位，直接返回
                number[i] = num
                break
        return flag

    def print_num(self, number):
        flag = 0 # 从左边数第一个不为0的位置
        for i in range(len(number)):
            if number[i] == 0:
                continue
            flag = i
            break
        s = "".join(map(str,number[flag:]))
        print(int(s))



if __name__ == "__main__":
    s = Solution()
    s.test(2)

