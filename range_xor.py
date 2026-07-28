# A^(A+1)^...^(B-1)^B の計算

def range_xor(A,B):
    # 0^1^...^X を計算（任意の偶数nについて n^(n+1)=1 が成り立つことを用いる）
    def f(X):
        if X<=0:
            return 0
        c=(X+1)//2
        if X%2==0:
            if c%2==0:
                return 0^X
            else:
                return 1^X
        else:
            if c%2==0:
                return 0
            else:
                return 1
                
    return f(A-1)^f(B)


A,B=map(int,input().split())
print(range_xor(A,B))