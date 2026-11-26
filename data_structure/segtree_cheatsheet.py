"""
セグメント木（ac-library-python）チートシート   
https://github.com/not522/ac-library-python/blob/master/atcoder/segtree.py
"""
from atcoder.segtree import SegTree

A=list(map(int,input().split()))

# 区間最大値
seg=SegTree(max,-10**18,A)
# 区間最大値mx + その最小インデックスidx  ※取得: mx,idx=seg.prod(L,R) → idx=-idx / 更新: seg.set(i,(x,-i))
seg=SegTree(max,(-10**18,-10**18),[(a,-i) for i,a in enumerate(A)])  
# 区間最大値mx + その最大インデックスidx  ※取得: mx,idx=seg.prod(L,R) / 更新: seg.set(i,(x,i))
seg=SegTree(max,(-10**18,-10**18),[(a,i) for i,a in enumerate(A)]) 

# 区間最小値
seg=SegTree(min,10**18,A)
# 区間最小値mn + その最小インデックスidx  ※取得: mn,idx=seg.prod(L,R) / 更新: seg.set(i,(x,i))
seg=SegTree(min,(10**18,10**18),[(a,i) for i,a in enumerate(A)])
# 区間最小値mn + その最大インデックスidx  ※取得: mn,idx=seg.prod(L,R) → idx=-idx / 更新: seg.set(i,(x,-i))
seg=SegTree(min,(10**18,10**18),[(a,-i) for i,a in enumerate(A)])

# 区間和
seg=SegTree(lambda x,y:x+y,0,A)

# 区間積（modで割る）
mod=998244353
A=[a%mod for a in A]
seg=SegTree(lambda x,y:x*y%mod,1,A)

# 区間GCD,LCM
from math import gcd,lcm
seg=SegTree(gcd,0,A)
seg=SegTree(lcm,1,A)

# 区間AND,OR,XOR
seg=SegTree(lambda x,y:x&y,-1,A)   # AND
seg=SegTree(lambda x,y:x|y,0,A)    # OR
seg=SegTree(lambda x,y:x^y,0,A)    # XOR


### --------------------------- セグ木上の二分探索 ------------------------------- ###
L,R,x=map(int,input().split())

""" 要素の二分探索 """
# L 以上で最小のインデックス i（なければ N）       <条件>
seg=SegTree(max,-10**18,A)
seg.max_right(L,lambda p:p<x)                # A[i] >= x
seg.max_right(L,lambda p:p<=x)               # A[i] > x

seg=SegTree(min,10**18,A)
seg.max_right(L,lambda p:p>x)                # A[i] <= x
seg.max_right(L,lambda p:p>=x)               # A[i] < x

# R 以下で最大のインデックス i（なければ -1）      <条件>
seg=SegTree(max,-10**18,A)
seg.min_left(R+1,lambda p:p<x)-1             # A[i] >= x 
seg.min_left(R+1,lambda p:p<=x)-1            # A[i] > x

seg=SegTree(min,10**18,A)
seg.min_left(R+1,lambda p:p>x)-1             # A[i] <= x
seg.min_left(R+1,lambda p:p>=x)-1            # A[i] < x


""" 区間和の二分探索   ※ 前提:配列要素がすべて非負 """
seg=SegTree(lambda x,y:x+y,0,A)

# A[L]から右方向の区間和が条件を満たす最小インデックス i（なければ N）
seg.max_right(L,lambda p:p<x)                # sum(A[L],...,A[i]) >= x   ※ x>0
seg.max_right(L,lambda p:p<=x)               # sum(A[L],...,A[i]) > x    ※ x>=0

# A[R]から左方向の区間和が条件を満たす最大インデックス i（なければ -1） 
seg.min_left(R+1,lambda p:p<x)-1             # sum(A[i],...,A[R]) >= x   ※ x>0
seg.min_left(R+1,lambda p:p<=x)-1            # sum(A[i],...,A[R]) > x    ※ x>=0