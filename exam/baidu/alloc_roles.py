'''
@File  : alloc_roles.py
@Author: Swift
@Date  : 2021/3/21 19:52
@Link  : 
@Desc  : [33,66,99]<==>[3,6,9,30,60,90] ==> [5,6,-1]
@Method: 
'''



def alloc(need, current):
    nl = [(item, idx) for idx, item in enumerate(need) ]
    cl = [(item, idx) for idx, item in enumerate(current)]
    nl = sorted(nl, key=lambda x:x[0])
    cl = sorted(cl, key=lambda x:x[0])
    i, j = 0, 0
    res = [-1]*len(need)
    while i < len(nl) and j < len(cl):
        if nl[i][0] <= cl[j][0]:
            res[nl[i][1]] = cl[j][1]+1
            i += 1
            j += 1
        else:
            j += 1
    return res


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n,m = list(map(int, input().strip().split()))
        need = list(map(int, input().strip().split()))
        current = list(map(int, input().strip().split()))
        res = alloc(need, current)
        print(res)