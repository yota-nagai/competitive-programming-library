def bellman_ford(s):
    global negative_cycle
    dist[s]=0
    for n in range(N-1):
        flag=False
        for i,j,c in edge:
            if dist[i]!=10**20 and dist[i]+c<dist[j]:
                dist[j]=dist[i]+c
                previous_node[j]=i  #経路復元用
                flag=True
        if flag==False:
            return
    for i,j,c in edge:
        if dist[i]!=10**20 and dist[i]+c<dist[j]:
            negative_cycle=True
            break

#経路復元（到達不可能 or 負の閉路が存在 の場合は復元不可）
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
edge=[]
for _ in range(M):
    u,v,c=map(int,input().split())
    u-=1
    v-=1
    edge.append([u,v,c])
    edge.append([v,u,c])  #無向グラフの場合のみ

dist=[10**20]*N
negative_cycle=False  #True: (始点から到達できる範囲に)負の閉路が存在
previous_node=[-1]*N


#dist[i]!=10**20かつnegative_cycle=False　--> 始点からiへの最短距離が正しくdist[i]と求められている
