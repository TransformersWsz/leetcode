class Solution:
    def __init__(self):
        self.res = []

    def backtrace(self, nums, start, temp):
        length = len(nums)
        if start == length:
            self.res.append(temp)
        else:
            for i in range(start, length):
                nums[start], nums[i] = nums[i], nums[start]
                self.backtrace(nums, start + 1, temp + [nums[start]])
                nums[start], nums[i] = nums[i], nums[start]

    def permute(self, nums):
        if not nums or len(nums) == 0:
            return nums
        self.backtrace(nums, 0, [])
        return self.res


if __name__ == '__main__':
    nums = [1,2,3]
    s = Solution()
    res = s.permute(nums)
    print(res)