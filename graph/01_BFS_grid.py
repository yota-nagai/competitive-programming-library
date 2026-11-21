from collections import deque


""" '#'のマスへの移動コストを 1 , それ以外の移動コストを 0 とする （移動は上下左右）"""

def bfs01(si,sj):
    dist[si][sj]=0
    dq=deque()
    dq.append((si,sj))
    done=[[False]*W for _ in range(H)]
    while len(dq)>0:
        i,j=dq.popleft()
        if done[i][j]:
            continue
        for di,dj in [[-1,0],[0,1],[1,0],[0,-1]]:
            i2,j2=i+di,j+dj
            if not (0<=i2<H and 0<=j2<W):
                continue
            if grid[i2][j2]!="#" and dist[i2][j2]>dist[i][j]:
                dq.appendleft((i2,j2))
                dist[i2][j2]=dist[i][j]
            elif grid[i2][j2]=="#" and dist[i2][j2]>dist[i][j]+1:
                dq.append((i2,j2))
                dist[i2][j2]=dist[i][j]+1
        done[i][j]=True



# ---------------------------------------------------------------------
H,W=map(int,input().split())
grid=[]
for _ in range(H):
    g=input()
    grid.append(g)

inf=10**18
dist=[[inf]*W for _ in range(H)]