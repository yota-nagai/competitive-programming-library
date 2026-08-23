N=int(input())
A=[[list(map(int,input().split())) for _ in range(N)] for _ in range(N)]

#3次元累積和
cum=[[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        for k in range(N):
            cum[i+1][j+1][k+1]=(
                cum[i+1][j+1][k]
               +cum[i+1][j][k+1]
               +cum[i][j+1][k+1]
               -cum[i+1][j][k]
               -cum[i][j+1][k]
               -cum[i][j][k+1]
               +cum[i][j][k]
               +A[i][j][k]
            )

Q=int(input())
for _ in range(Q):
    lx,rx,ly,ry,lz,rz=map(int,input().split())
    lx-=1
    ly-=1
    lz-=1
    ans=(
        cum[rx][ry][rz]
       +cum[rx][ly][lz]
       +cum[lx][ry][lz]
       +cum[lx][ly][rz]
       -cum[rx][ry][lz]
       -cum[rx][ly][rz]
       -cum[lx][ry][rz]
       -cum[lx][ly][lz]
    )

    print(ans)