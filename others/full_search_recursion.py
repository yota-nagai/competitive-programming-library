# https://drken1215.hatenablog.com/entry/2020/05/04/190252

# 長さNで, 各項の値が[0,M)のどれかである数列を全探索　O(M^N)

import sys
sys.setrecursionlimit(10**8)

def dfs(A):
    if len(A)==N:
        # 処理
        return
    for i in range(M):
        # 条件判定（枝刈り）があれば記述
        A.append(i)
        dfs(A)
        A.pop()


N,M=map(int,input().split())
dfs([])