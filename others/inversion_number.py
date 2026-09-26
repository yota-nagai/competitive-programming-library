from atcoder.segtree import SegTree

# 転倒数(i<j かつ lst[i]>lst[j] を満たす組(i,j)の数）を求める
# 隣接swapによる配列のソート（バブルソート）の交換回数に一致

# ※配列の各要素は 0 以上 len(lst) 以下であることが前提

def inversion_number(lst):
    cnt=[0]*(len(lst)+1)
    seg=SegTree(lambda x,y:x+y,0,cnt)
    ans=0
    for i in range(len(lst)):
        l,r=lst[i]+1,len(lst)
        ans+=seg.prod(l,r+1)
        seg.set(lst[i],seg.get(lst[i])+1)
    return ans