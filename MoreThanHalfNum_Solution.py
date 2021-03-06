# -*- coding:utf-8 -*-

# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
# 由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
# 1、思路
# 数组中有一个数字出现的次数超过数组长度的一半，也就是说它出现的次数比其他所有数字出现次数的和还要多。
# 因此我们可以考虑在遍历数组的时候保存两个值：一个是数组的一个数字，一个是次数。当我们遍历到下一个数字的时候，
# 如果下一个数字和我们之前保存的数字相同，则次数加1；如果下一个数字和我们之前保存的数字不同，则次数减1。如果次数为零，
# 我们需要保存下一个数字，并把次数设为1。由于我们要找的数字出现的次数比其他所有数字出现的次数之和还要多，
# 那么要找的数字肯定是最后一次把次数设为1时对应的数字。


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        result = numbers[0]
        times = 1
        for i in range(1, len(numbers)):
            if times == 0:
                result = numbers[i]
                times = 1
            elif result == numbers[i]:
                times += 1
            else:
                times -= 1
        times = 0
        for i in range(len(numbers)):
            if numbers[i] == result:
                times += 1
        return result if times > len(numbers) // 2 else None


s = Solution()
print s.MoreThanHalfNum_Solution([1, 2, 3, 2, 2, 2, 5, 4, 2])
