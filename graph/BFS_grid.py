from collections import deque

H,W=map(int,input().split())
sh,sw=map(int,input().split())
sh-=1
sw-=1
gh,gw=map(int,input().split())
gh-=1
gw-=1

S=[]
for _ in range(H):
    s=input()
    S.append(s)

def bfs(sh,sw):
    dq=deque()
    dq.append((sh,sw))
    dist[sh][sw]=0

    while len(dq)>0:
        i,j=dq.popleft()
        for di,dj in [[-1,0],[0,1],[1,0],[0,-1]]:
            i2,j2=i+di,j+dj
            if not (0<=i2<H and 0<=j2<W):
                continue
            if S[i2][j2]=="#":
                continue
            if dist[i2][j2]==-1:
                dist[i2][j2]=dist[i][j]+1
                dq.append((i2,j2))

dist=[[-1]*W for _ in range(H)]
bfs(sh,sw)

print(dist[gh][gw])