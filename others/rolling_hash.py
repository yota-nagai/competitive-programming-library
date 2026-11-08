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
        return (self.hash[r]-self.hash[l]*self.power[r-l])%self.mod

    # S[l1:r1] と S[l2:r2] を結合した文字列 S[l1]...S[r1-1]S[l2]...S[r2-1] のハッシュ値を返す   ※ l1,r1,l2,r2 : 0-indexed
    def connect(self,l1,r1,l2,r2):
        hash1=self.get(l1,r1)
        hash2=self.get(l2,r2)
        return (hash1*self.power[r2-l2]+hash2)%self.mod    



mod=(1<<61)-1
base=random.randint(10000,mod-2)

S=input()
RH_S=RollingHash(S,mod,base)