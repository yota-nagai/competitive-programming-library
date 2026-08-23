H,W,N=map(int,input().split())
cum=[[0]*(W+1) for _ in range(H+1)]
for _ in range(N):
    a,b,c,d=map(int,input().split())
    a-=1
    b-=1
    c-=1
    d-=1
    cum[a][b]+=1
    cum[c+1][d+1]+=1
    cum[c+1][b]-=1
    cum[a][d+1]-=1

for h in range(0,H+1):
    for w in range(1,W+1):
        cum[h][w]=cum[h][w-1]+cum[h][w]
for w in range(0,W+1):
    for h in range(1,H+1):
        cum[h][w]=cum[h-1][w]+cum[h][w]

for i in range(0,H):
    print(*cum[i][0:W])
    