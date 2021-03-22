'''
@File  : test.py.py
@Author: Swift
@Date  : 2021/3/22 19:09
@Link  : 
@Desc  : 
@Method: 
'''
class Test():
    def __init__(self):
        self.res = []

    def dfs(self, arr, left, right, score):
        if left > right:
            return
        elif left == right:
            return self.res.append(score+arr[left])
        else:
            for i in range(right-left):
                lp = sum(arr[left:left+i+1])
                rp = sum(arr[left+i+1:right+1])
                if lp <= rp:
                    self.dfs(arr, left, left+i, score+lp)
                else:
                    self.dfs(arr, left+i+1, right, score+rp)

    def get_max_val(self, arr):
        left = 0
        right = len(arr)-1
        self.dfs(arr, left, right, 0)
        return max(self.res)

if __name__ == '__main__':
    t = Test()
    arr = [6, 2, 3, 4, 5, 5]
    print(t.get_max_val(arr))
