# N個の右半開区間 [l_1,r_1), [l_2,r_2), ... , [l_n,r_n) の和集合を求める   O(N log N)
# 引数：LR = [(l_1,r_1),(l_2,r_2), ... , (l_n,r_n)] 
# 返り値：統合後の区間リスト

def union_of_interval(LR):
    A=[]
    for l,r in LR:
        A.append((l,1))
        A.append((r,-1))
    A.sort()

    B=[A[0]]
    for i in range(1,len(A)):
        if A[i][0]==B[-1][0]:
            B[-1]=(B[-1][0],B[-1][1]+A[i][1])
        else:
            B.append(A[i])

    res=[(B[0][0],None)]
    cnt=B[0][1]
    for i in range(1,len(B)):
        if cnt+B[i][1]==0:
            res[-1]=(res[-1][0],B[i][0])
            if i<len(B)-1:
                res.append((B[i+1][0],None))
        cnt+=B[i][1]

    return res



N=int(input())
LR=[]
for _ in range(N):
    l,r=map(int,input().split())
    LR.append((l,r))