# Functional Graph : すべての頂点の出次数が 1 である有向グラフ
# 性質：各連結成分にサイクルが1つ存在


"""
与えられた Functional Graph に含まれるサイクルを全て列挙する 
[[サイクル1のパス],[サイクル2のパス],...,[サイクルkのパス]] の形で返す     k : 連結成分の個数 
※ 終点（= 始点）は含めない 
※ 0-indexed
"""
def cycle_functional(to):
    N=len(to)
    seen=[False]*N      
    finished=[False]*N  
    cycle_list=[]

    for i in range(N):
        if finished[i]:
            continue
        pos=i
        history=[]
        while True:
            seen[pos]=True
            history.append(pos)
            pos=to[pos]
            if seen[pos] and not finished[pos]:
                break
            elif finished[pos]:
                pos=-1
                break
        if pos!=-1:
            cycle=[]
            v=pos
            while True:
                cycle.append(v)
                v=to[v]
                if v==pos:
                    break
            cycle_list.append(cycle)
        for j in history:
            finished[j]=True
    
    return cycle_list 




to=list(map(int,input().split()))  # 各頂点から出る辺がどの頂点に向かうか
to=[i-1 for i in to]               # 0-indexedに 

cycle_list=cycle_functional(to)