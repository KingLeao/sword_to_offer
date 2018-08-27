# -*- coding:utf-8 -*-

# 定义栈的数据结构，请在类型中实现一个能够得到栈最小元素的min函数。
# 1、思路
# 使用两个stack，一个为数据栈，另一个为辅助栈。数据栈用于存储所有数据，辅助栈用于存储最小值。
# 举个例子：
# 入栈的时候：首先往空的数据栈里压入数字3，显然现在3是最小值，我们也把最小值压入辅助栈。接下来往数据栈里压入数字4。
# 由于4大于之前的最小值，因此我们只要入数据栈，不压入辅助栈。
# 出栈的时候：当数据栈和辅助栈的栈顶元素相同的时候，辅助栈的栈顶元素出栈。否则，数据栈的栈顶元素出栈。
# 获得栈顶元素的时候：直接返回数据栈的栈顶元素。
# 栈最小元素：直接返回辅助栈的栈顶元素。


class Solution:
    def __init__(self):
        self.Data = []
        self.Min = []

    def push(self, x):
        if len(self.Min) == 0:
            self.Min.append(x)
        if self.Min[-1] > x:
            self.Min.append(x)
        self.Data.append(x)

    def pop(self):
        if self.Data[-1] == self.Min[-1]:
            self.Min.pop()
        self.Data.pop()

    def top(self):
        return self.Data[-1]

    def min(self):
        return self.Min[-1]


s = Solution()
s.push(1)
s.push(2)
s.push(3)
print s.top()
print s.min()
