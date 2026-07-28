# 二部グラフ判定 #

import sys
sys.setrecursionlimit(10**8)

def dfs(i,c):
    global flag
    color[i]=c
    for j in graph[i]:
        if color[j]!=None:
            if color[j]==c:
                flag=False
                return
            else:
                continue
        if c==0:
            dfs(j,1)
        else:
            dfs(j,0)
    
# sを含む連結成分について判定
def is_bipartite(s):
    dfs(s,0)
    return flag


N,M=map(int,input().split())
graph=[[] for _ in range(N)]
for _ in range(M):
    a,b=map(int,input().split())
    a-=1
    b-=1
    graph[a].append(b)
    graph[b].append(a)

color=[None]*N
for i in range(N):
    if color[i]==None:
        flag=True
        if not is_bipartite(i):
            print("No")
            exit()

print("Yes")
