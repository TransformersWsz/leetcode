'''
@File  : min-stack.py
@Author: Swift
@Date  : 2021/4/18 12:07
@Link  : https://leetcode-cn.com/problems/min-stack/
@Desc  : 155. 最小栈
@Method: 
'''

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.mins = []


    def push(self, val: int) -> None:
        self.data.append(val)
        if not self.mins or self.mins[-1] >= val:
            self.mins.append(val)

    def pop(self) -> None:
        item = self.data.pop()
        if item == self.mins[-1]:
            self.mins.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.mins[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()