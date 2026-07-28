import sys
sys.setrecursionlimit(10**8)

N,X,Y=map(int,input().split())
X-=1
Y-=1
G=[[] for _ in range(N)]
C=set()
for _ in range(N-1):
    u,v=map(int,input().split())
    u-=1
    v-=1
    G[u].append(v)
    G[v].append(u)
    C.add((u,v))
    C.add((v,u))


def dfs(i):
    path.append(i) 
    if i==Y:
        print(*[i+1 for i in path])
        exit()
    visited[i]=True
    for j in G[i]:
        if not visited[j]:
            dfs(j)
    path.pop()

visited=[False]*N
path=[]
dfs(X)