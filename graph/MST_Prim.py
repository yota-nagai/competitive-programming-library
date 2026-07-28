import heapq

N,M=map(int,input().split())
graph=[[] for _ in range(N)]
for _ in range(M):
    u,v,c=map(int,input().split())
    u-=1
    v-=1
    graph[u].append((v,c))
    graph[v].append((u,c))

marked=[False]*N
marked_cnt=0
hq=[]

for i,c in graph[0]:
    heapq.heappush(hq,(c,i))
marked[0]=True
marked_cnt+=1


cost_sum=0
while marked_cnt<N:
    c,i=heapq.heappop(hq)
    if marked[i]:
        continue
    marked[i]=True
    cost_sum+=c
    marked_cnt+=1
    for ii,cc in graph[i]:
        if marked[ii]:
            continue
        heapq.heappush(hq,(cc,ii))

print(cost_sum)