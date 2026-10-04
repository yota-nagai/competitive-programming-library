# N個の右半開区間 [l_1,r_1), [l_2,r_2), ... , [l_n,r_n) の和集合を求める   O(N log N)
# 引数：LR = [(l_1,r_1),(l_2,r_2), ... , (l_n,r_n)] 
# 返り値：統合後の区間リスト

def union_of_interval(LR):
    LR.sort()
    res=[]
    left,right=LR[0]
    for l,r in LR[1:]:
        if l<=right:
            right=max(right,r)
        else:
            res.append((left,right))
            left,right=l,r
    res.append((left,right))
    return res


N=int(input())
LR=[]
for _ in range(N):
    l,r=map(int,input().split())
    LR.append((l,r))