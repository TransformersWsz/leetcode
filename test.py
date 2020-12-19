'''
@File  : test.py
@Author: Swift
@Date  : 2020/12/15 11:55
@Link  : 
@Desc  : 
@Method: 
'''


def getMaXArr(nums, i):
    if not i:
        return []
    # pop表示最多可以不要nums里几个数字，要不组成不了i位数字
    stack, pop = [], len(nums) - i
    for num in nums:
        while pop and stack and stack[-1] < num:
            pop -= 1
            stack.pop()
        stack.append(num)
    return stack[:i]


if __name__ == '__main__':
    nums = [12,24,45,1,2]
    i = 3
    res = getMaXArr(nums, i)
    print(res)