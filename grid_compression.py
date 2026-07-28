# グリッドの圧縮
# N個の要素（重複ok）, HW-N個の"*"からなるH行W列のグリッドを圧縮（全部"*"の行・列を取り除く）
# 座標は0-indexed

from collections import defaultdict
from bisect import bisect_left

H,W,N=map(int,input().split())
rows=set()
columns=set()
grid=[]
for i in range(1,N+1):
    a,b,x=input().split()
    a=int(a)-1
    b=int(b)-1
    grid.append([a,b,x])
    rows.add(a)
    columns.add(b)

new_H,new_W=len(rows),len(columns)
rows=sorted(list(rows))
columns=sorted(list(columns))

pos=defaultdict(list)  #各要素の圧縮後の座標
for a,b,x in grid:
    pos[x].append([bisect_left(rows,a),bisect_left(columns,b)])


# 圧縮後のグリッドの作成　※巨大なグリッドだとメモリ不足になる
compressed_grid=[["*"]*new_W for _ in range(new_H)]
for k,v in pos.items():
    for pos_h,pos_w in v:
        compressed_grid[pos_h][pos_w]=k
