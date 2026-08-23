#2つの正の整数の最大公約数(gcd)
A,B=map(int,input().split())
while A!=0 and B!=0:
    if A>B:
        A%=B
    else:
        B%=A
if A==0:
    print(B)
else:
    print(A)


#N個の正の整数の最大公約数(gcd)
N=int(input())
A=list(map(int,input().split()))
for i in range(N-1):
    while A[i]!=0 and A[i+1]!=0:
        if A[i]>A[i+1]:
            A[i]%=A[i+1]
        else:
            A[i+1]%=A[i]
    if A[i]!=0:
        A[i+1]=A[i]
print(A[N-1])


"""
最小公倍数(lcm)を最大公約数(gcd)から求める
lcm=(A*B)//gcd
"""