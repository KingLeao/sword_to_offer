# -*- coding:utf-8 -*-

# 把只包含因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含因子7。
# 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
# 1、思路
#
# 所谓的一个数m是另一个数n的因子，是指n能被m整除，也就是n%m==0。根据丑数的定义，丑数只能被2、3和5整除。
# 根据丑数的定义，丑数应该是另一个丑数乘以2、3或者5的结果（1除外）。因此我们可以创建一个数组，
# 里面的数字是排好序的丑数，每一个丑数都是前面的丑数乘以2、3或者5得到的。
#
# 这个思路的关键问题在于怎样保证数组里面的丑数是排好序的。对乘以2而言，肯定存在某一个丑数T2，
# 排在它之前的每一个丑数乘以2得到的结果都会小于已有最大的丑数，在它之后的每一个丑数乘以乘以2得到的结果都会太大。
# 我们只需要记下这个丑数的位置，同时每次生成新的丑数的时候，去更新这个T2。对乘以3和5而言，也存在着同样的T3和T5。


class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index < 7:
            return index
        res = [1, 2, 3, 4, 5, 6]
        t2, t3, t5 = 3, 2, 1
        for i in range(6, index):
            res.append(min(res[t2] * 2, res[t3] * 3, res[t5] * 5))
            if res[t2] * 2 == res[i]:
                t2 += 1
            if res[t3] * 3 == res[i]:
                t3 += 1
            if res[t5] * 5 == res[i]:
                t5 += 1
        return res[-1]


s = Solution()
print s.GetUglyNumber_Solution(8)
