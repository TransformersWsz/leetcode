'''
@File  : JZ45_扑克牌顺子.py
@Author: Swift
@Date  : 2021/4/4 17:57
@Link  : https://www.nowcoder.com/practice/762836f4d43d43ca9deb273b3de8e1f4?tpId=13&tqId=11198&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！“红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....LL不高兴了,他想了想,决定大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。LL决定去买体育彩票啦。 现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何， 如果牌能组成顺子就输出true，否则就输出false。为了方便起见,你可以认为大小王是0。
@Method: 
'''


# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers or len(numbers) == 0:
            return False
        d = {}
        minv, maxv = float("inf"), float("-inf")
        for item in numbers:
            if item != 0:
                minv = min(minv, item)
                maxv = max(maxv, item)
                if maxv - minv > len(numbers) - 1:
                    return False
            if item not in d:
                d[item] = 1
            else:
                d[item] += 1

        total = len(numbers)
        need = total
        for i in range(total):
            need_item = minv + i
            if need_item in d:
                d[need_item] -= 1
                need -= 1
        if need == 0:
            return True
        else:
            if 0 in d:
                return bool(need==d[0])
            return False

if __name__ == '__main__':
    s = Solution()
    arr = [1,3,0,5,0]
    res = s.IsContinuous(arr)
    print(res)