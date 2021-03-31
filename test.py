# -*- coding:utf-8 -*-
class Solution:
    def qsort(self, arr, k):
        pivot = arr[0]
        low, high = 0, len(arr)-1
        while low < high:
            while low < high and arr[high] >= pivot:
                high -= 1
            arr[low] = arr[high]

            while low < high and arr[low] <= pivot:
                low += 1
            arr[high] = arr[low]
        arr[low] = pivot
        if low == k-1:
            return
        elif low < k:
            self.qsort(arr[low+1:], k-(low+1))
        else:
            self.qsort(arr[:low], k)


    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not tinput or len(tinput) == 0:
            return tinput
        if k > len(tinput):
            return []
        self.qsort(tinput, k)
        return tinput[:k]


if __name__ == '__main__':
    solution = Solution()
    arr = [4,5,1,6,2,7,3,8]
    k = 8
    res = solution.GetLeastNumbers_Solution(arr, k)
    print(res)