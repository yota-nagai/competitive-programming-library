H,W=map(int,input().split())
X=[]
for _ in range(H):
    x=list(map(int,input().split()))
    X.append(x)

cum=[[0]*(W+1)]
for i in range(H):
    r=[0]
    for j in range(W):
        r.append(r[-1]+cum[i][j])
    cum.append(r)

for w in range(0,W+1):
    for h in range(1,H+1):
        cum[h][w]=cum[h-1][w]+cum[h][w]

Q=int(input())
for i in range(Q):
    a,b,c,d=map(int,input().split())
    print(cum[c][d]+cum[a-1][b-1]-cum[c][b-1]-cum[a-1][d])
    

