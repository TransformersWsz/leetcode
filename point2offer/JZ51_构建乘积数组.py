'''
@File  : JZ51_构建乘积数组.py
@Author: Swift
@Date  : 2021/3/16 22:55
@Link  : https://www.nowcoder.com/practice/94a4d381a68b47b7a8bed86f2975db46?tpId=13&tqId=11204&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。（注意：规定B[0] = A[1] * A[2] * ... * A[n-1]，B[n-1] = A[0] * A[1] * ... * A[n-2];）对于A长度为1的情况，B无意义，故而无法构建，因此该情况不会存在。
@Method: 
'''

class Solution:
    def multiply(self, A):
        # write code here
        length = len(A)
        forward = [1] * (length + 1)
        backward = [1] * (length + 1)

        for idx, item in enumerate(A):
            forward[idx + 1] = forward[idx] * A[idx]

        reversed_A = A[::-1]
        for idx, item in enumerate(reversed_A):
            backward[idx + 1] = backward[idx] * A[length - idx - 1]

        res = []
        for idx in range(length):
            if idx == 0:
                res.append(backward[length - 1])
            elif idx == length - 1:
                res.append(forward[length - 1])
            else:
                res.append(forward[idx] * backward[length - 1 - idx])
        return res


if __name__ == '__main__':
    solution = Solution()
    A = [1, 2, 3, 4, 5]
    res = solution.multiply(A)
    print(res)
