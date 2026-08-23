# N行N列のグリッドを時計回りに90°回転

def rotate_90(S):
    n=len(S)
    S_rotated=[[None]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            S_rotated[j][n-1-i]=S[i][j]
    return S_rotated

N=int(input())
S=[]
for _ in range(N):
    s=list(input())
    S.append(s)

S_rotated=rotate_90(S)
for s in S_rotated:
    print("".join(s))