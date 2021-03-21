'''
@File  : stair.py
@Author: Swift
@Date  : 2021/3/21 19:53
@Link  : 
@Desc  : 有m种跨台阶方法，但是当前步不能与前两步相同，例如1，2，1非法，1，2，3合法
@Method: 
'''

class Test(object):
    def __init__(self):
        self.count = 0

    def dfs(self, visited, current_stair, n, m):
        if current_stair == n:
            self.count += 1
        elif current_stair > n:
            return
        else:
            for steps in range(1, m+1):
                if steps not in visited:
                    if len(visited) <= 1:
                        visited.append(steps)
                        self.dfs(visited, current_stair + steps, n, m)
                        visited.pop()
                    else:
                        first = visited.pop(0)
                        visited.append(steps)
                        self.dfs(visited, current_stair+steps, n, m)
                        visited.pop()
                        visited.insert(0, first)

    def stair(self, n, m):
        visited = []
        self.dfs(visited, 0, n, m)
        return self.count


if __name__ == '__main__':
    n, m = list(map(int, input().strip().split()))
    test = Test()
    res = test.stair(n, m)
    print(res)