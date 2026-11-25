"""
セグメント木（ac-library-python）チートシート   
https://github.com/not522/ac-library-python/blob/master/atcoder/segtree.py
"""
from atcoder.segtree import SegTree

A=list(map(int,input().split()))


# 区間最大値
seg=SegTree(max,-10**18,A)

# 区間最小値
seg=SegTree(min,10**18,A)

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