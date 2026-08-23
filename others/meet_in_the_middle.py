from collections import defaultdict
N,X=map(int,input().split())

#グループAとグループBに分ける
A=[]
B=[]
for i in range(N):
    w=int(input().split())
    if i%2==0:
        A.append(w)
    else:
        B.append(w)

def has_bit(n,i):
    return (n&(1<<i)>0)

dic=defaultdict(int)
ALLB=1<<len(B)
for n in range(ALLB):
    s=0
    for i in range(N):
        if has_bit(n,i):
            s+=B[i]
    dic[s]+=1

ALLA=1<<len(A)
ans=0
for n in range(ALLA):
    s=0
    for i in range(N):
        if has_bit(n,i):
            s+=A[i]
    ans+=dic[X-s]

print(ans)

