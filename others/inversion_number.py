from atcoder.segtree import SegTree

N=int(input())
A=list(map(int,input().split()))

def op(x,y):
    return x+y

cnt=[0]*(N+1)

seg=SegTree(op,0,cnt)
ans=0
for i in range(N):
    l,r=A[i]+1,N
    # if l>N:
    #     seg.set(A[i],seg.get(A[i])+1)
    #     continue

    ans+=seg.prod(l,r+1)
    seg.set(A[i],seg.get(A[i])+1)

print(ans)