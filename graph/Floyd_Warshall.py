def floyd_warshall():
    for k in range(N):
        for x in range(N):
            for y in range(N):
                d=dist[x][k]+dist[k][y]
                if d<dist[x][y]:
                    dist[x][y]=d
                    next_node[x][y]=next_node[x][k]  #経路復元用

#経路復元（到達不可能 or 負の閉路が存在 の場合は復元不可）
def restore_path(start,goal):
    path=[]
    i=start
    while True:
        path.append(i+1)
        if i==goal:
            break
        i=next_node[i][goal]
    return path



N,M=map(int,input().split())

dist=[[10**18]*N for _ in range(N)]
next_node=[[-1]*N for _ in range(N)]  #next_node[i][j]：iからjへ行く最短経路における最初の経由地

for i in range(N):
    dist[i][i]=0

for _ in range(M):
    u,v,c=map(int,input().split())
    u-=1
    v-=1
    dist[u][v]=c
    dist[v][u]=c  #無向グラフの場合のみ
    next_node[u][v]=v 
    next_node[v][u]=u  #無向グラフの場合のみ

#floyd_warshall(start)
#dist[i][j]>=10**16ならばiからjへの到達不可能と判定
#dist[i][i]<0なら負の閉路が存在