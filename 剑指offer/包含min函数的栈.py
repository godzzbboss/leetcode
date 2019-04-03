# -*- coding: utf-8 -*-

"""
__author__ = "BigBrother"

"""


class Solution():
    stack1 = []
    stack2 = [] # 始终保存当前最小元素

    def push(self, node):
        if not self.stack1:
            self.stack1.append(node)
            self.stack2.append(node)
        else:
            if node < self.stack2[-1]:
                self.stack1.append(node)
                self.stack2.append(node)
            else:
                self.stack1.append(node)
                self.stack2.append(self.stack2[-1])

    def pop(self):
        if self.stack1 and self.stack2:
            self.stack2.pop()
            return self.stack1.pop()
        return None

    def top(self):
        if self.stack1:
            return self.stack1[-1]

    def min(self):
        if self.stack2:
            return self.stack2[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.test())

