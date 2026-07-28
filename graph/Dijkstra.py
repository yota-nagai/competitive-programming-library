import heapq

def dijkstra(s):
    dist[s]=0
    hq=[]
    heapq.heappush(hq,[0,s])
    done=[False]*N
    while len(hq)>0:
        d,i=heapq.heappop(hq)
        if done[i]:
            continue
        done[i]=True
        for (j,c) in graph[i]:
            if dist[j]==-1 or dist[j]>dist[i]+c:
                dist[j]=dist[i]+c
                previous_node[j]=i  #経路復元用
                heapq.heappush(hq,(dist[j],j))

#経路復元（到達不可能なら復元不可）
def restore_path(start,goal):
    path=[]
    i=goal
    while True:
        path.append(i+1)
        if i==start:
            break
        i=previous_node[i]
    return list(reversed(path))



N,M=map(int,input().split())
graph=[[] for _ in range(N)]
for _ in range(M):
    u,v,c=map(int,input().split())
    u-=1
    v-=1
    graph[u].append((v,c))
    graph[v].append((u,c))  #無向グラフの場合のみ

dist=[-1]*N
previous_node=[-1]*N

#start,goalを1-indexedで受け取る
#start-=1
#goal-=1
#dijkstra(start)
#*restore_path(start,goal)

#dist[i]=-1ならばiへの到達不可能