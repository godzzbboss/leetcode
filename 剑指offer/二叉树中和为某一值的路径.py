# -*- coding: utf-8 -*-

"""
__author__ == "BigBrother"

"""

import copy
class Solution:
    def test(self, root, target):
        path = []
        result = []


        # 如果想在递归的过程中生成最终的结果，保存结果的变量当成递归函数的参数传递
        self.find(root, target, path, result)
        return result

    def find(self, root, target, path, result):
        if not root:
            return
        path.append(root.val)
        if root.val == target and not root.left and not root.right:
            result.append(path)
        else:
            if root.left:
                path_ = copy.deepcopy(path) # !!!python里传递的是引用，所以进行递归时需要进行深拷贝，不然下次递归的结果会影响上次递归
                self.find(root.left, target-root.val, path_, result)
            if root.right:
                path_ = copy.deepcopy(path)
                self.find(root.right, target - root.val, path_, result)


if __name__ == "__main__":
    pass