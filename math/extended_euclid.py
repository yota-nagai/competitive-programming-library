#ax+by=gcd(a,b)を満たすx,yを求める

def extended_euclid(a,b):
    lst=[[a,b]] #a=qb+rなる[b,r]を加えていく
    while lst[-1][1]>0:
        lst.append([lst[-1][1],lst[-1][0]%lst[-1][1]])
    
    #lstを逆からさかのぼる
    x,y=1,0
    for i in reversed(range(len(lst)-1)):
        x,y=y,x-(lst[i][0]//lst[i][1])*y

    return x,y


a,b=map(int,input().split())
print(extended_euclid(a,b))

