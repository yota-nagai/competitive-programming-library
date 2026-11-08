import random

class RollingHash:
    def __init__(self,S,mod,base):
        self.n=len(S)
        self.mod=mod
        self.base=base
        self.hash=[0]*(self.n+1)
        self.power=[1]*(self.n+1)
        for i in range(self.n):
            s=ord(S[i])
            self.hash[i+1]=(self.base*self.hash[i]+s)%mod
            self.power[i+1]=(self.power[i]*self.base)%mod

    # S[l:r]（= S[l]S[l+1]...S[r-1]）のハッシュ値を返す   ※ l,r : 0-indexed
    def get(self,l,r):
        res=(self.hash[r]-self.hash[l]*self.power[r-l])%self.mod
        return res       



mod=(1<<61)-1
base=random.randint(10000,mod-2)

S=input()
RH_S=RollingHash(S,mod,base)