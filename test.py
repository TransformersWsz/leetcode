class Solution:
    def canJump(self, nums) -> bool:
        length, right_most = len(nums), 0
        for i in range(length):
            if i <= right_most:
                right_most = max(right_most, i+nums[i])
                if right_most >= length-1:
                    return True
        return False


if __name__ == '__main__':
    solution = Solution()
    nums = [3,2,1,0,4]
    res = solution.canJump(nums)
    print(res)