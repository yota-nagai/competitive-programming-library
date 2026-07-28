#メモ化再帰
from functools import cache
@cache
def f(n):
    if n==0:
        return 1
    else:
        return f(n//2)+f(n//3)
    
print(f(5))

#2つの要素を比較する比較関数を作り、sort()におけるソート条件として使うことができる
from functools import cmp_to_key
def compare(i,j):
    if i>j:
        return 1
    elif i<j:
        return -1
    else:
        return 0
    
A=[5,2,3,1,4]
A.sort(key=cmp_to_key(compare))
print(A)