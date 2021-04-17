'''
@File  : yong-liang-ge-zhan-shi-xian-dui-lie-lcof.py
@Author: Swift
@Date  : 2021/4/17 15:54
@Link  : https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/
@Desc  : 剑指 Offer 09. 用两个栈实现队列
@Method: 
'''

class CQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def appendTail(self, value: int) -> None:
        self.s1.append(value)

    def deleteHead(self) -> int:
        if self.s2:
            return self.s2.pop()
        else:
            if not self.s1:
                return -1
            else:
                while self.s1:
                    item = self.s1.pop()
                    self.s2.append(item)
                return self.s2.pop()


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()