'''
@File  : xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof.py
@Author: Swift
@Date  : 2021/3/13 22:44
@Link  : 
@Desc  : 
@Method: 
'''

class Solution:
    def minArray(self, numbers) -> int:
        low = 0
        high = len(numbers)-1
        if numbers[low] < numbers[high]:
            return numbers[low]
        while low < high:
            mid = (low+high) // 2
            if numbers[mid] > numbers[high]:
                low = mid+1
            elif numbers[mid] < numbers[high]:
                high = mid
            else:
                high -= 1
        return numbers[low]


if __name__ == '__main__':
    solution = Solution()
    numbers = [3,3,3,1,3]
    res = solution.minArray(numbers)
    print(res)