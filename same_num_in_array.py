# -*- coding:utf-8 -*-

# 数组中重复的数字

# 在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。
# 也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，
# 那么对应的输出是第一个重复的数字2。


class Solution:
    def duplicate(self, s):
        if s is []:
            return []
        i = 0
        while i < len(s)-1:
            if s[i] in s[i+1:]:
                return s[i]
            else:
                i += 1
        return []


s = Solution()
print s.duplicate([7, 4, 2, 3, 1, 0, 2, 5, 9])
