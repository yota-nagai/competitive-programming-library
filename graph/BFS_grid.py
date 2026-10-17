from collections import deque,defaultdict

# 座標は 0-indexd で統一 #

def bfs(si,sj):
    dq=deque()
    dq.append((si,sj))
    dist[si][sj]=0
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
                previous_node[(i2,j2)]=(i,j)  # 経路復元用
                dq.append((i2,j2))

# 経路復元（到達不可能なら復元不可）
def restore_path(si,sj,gi,gj):
    path=[]  
    i,j=gi,gj
    while True:
        path.append((i,j))
        if i==si and j==sj:
            break
        i,j=previous_node[(i,j)]
    return list(reversed(path))


# ---------------------------------------------------------------------------
H,W=map(int,input().split())
si,sj=map(int,input().split())
si-=1
sj-=1
gi,gj=map(int,input().split())
gi-=1
gj-=1

S=[]
for _ in range(H):
    s=input()
    S.append(s)

dist=[[-1]*W for _ in range(H)]
previous_node=defaultdict(lambda:(-1,-1))  # 経路復元用

bfs(si,sj)