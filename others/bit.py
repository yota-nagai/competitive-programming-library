N=int(input())

#bit全探索
def has_bit(n,i):
    return (n&(1<<i)>0)

ALL=1<<N
for n in range(ALL):
    for i in range(N):
        if has_bit(n,i):
            #集合nに要素iが含まれるときに行う処理
        


#ビットごとのOR |
#ビットごとのAND &
#ビットごとのXOR ^  2つのうちちょうど一方が1であれば1,そうでなければ0


#bit全探索　3**Nバージョン
for n in range(3**N):
    for i in range(N):
        if n//(3**i)%3==1:
            #####
        elif n//(3**i)%3==2:
            #####

