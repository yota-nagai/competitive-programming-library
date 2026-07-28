#座標圧縮

def coordinate_compression(lst,start):  # (圧縮対象の配列, 何-indexedにするか)
    lst_sort=sorted(set(lst))
    ranking={}
    rank=start
    for i in lst_sort:
        ranking[i]=rank
        # rank_to_val[rank]=i
        rank+=1
    Z=[]  
    for a in lst:
        Z.append(ranking[a])
        
    return Z


A=list(map(int,input().split()))
# rank_to_val={}
print(coordinate_compression(A,0))