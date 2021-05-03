'''
@File  : implement-stack-using-queues.py
@Author: Swift
@Date  : 2021/5/3 20:38
@Link  : https://leetcode-cn.com/problems/implement-stack-using-queues/
@Desc  : 225. 用队列实现栈
@Method: 
'''

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = []
        self.q2 = []


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.pop(0))
        self.q1, self.q2 = self.q2, self.q1


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q1.pop(0)


    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q1[0]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.q1



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()