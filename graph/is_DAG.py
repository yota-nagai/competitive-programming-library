from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

N=int(input())
G=defaultdict(list)
for _ in range(N):
    s,t=input().split()
    G[s].append(t)


def dfs(i):
    flag[i]=True
    for j in G[i]:
        if flag[j]==True:
            if finished[j]==False:
                #サイクル検出
                print("No")
                exit()
        else:
            dfs(j)
    finished[i]=True


flag=defaultdict(lambda:False)
finished=defaultdict(lambda:False)

for i in list(G.keys()):
    if not flag[i]:
        dfs(i)

print("Yes")
