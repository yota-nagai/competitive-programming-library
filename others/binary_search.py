from bisect import bisect_left,bisect_right

# ※ 配列 A は昇順ソート済みであることが前提


# --------------------------  インデックス取得  ----------------------------------

# A_i >= X であるインデックス i のうち最小のもの（存在しなければ None）を返す
def min_ge_idx(A,X):
    res=bisect_left(A,X)
    if res==len(A):
        res=None
    return res

# A_i > X であるインデックス i のうち最小のもの（存在しなければ None）を返す
def min_gt_idx(A,X):
    res=bisect_right(A,X)
    if res==len(A):
        res=None
    return res

# A_i <= X であるインデックス i のうち最大のもの（存在しなければ None）を返す
def max_le_idx(A,X):
    res=bisect_right(A,X)-1
    if res==-1:
        res=None
    return res

# A_i < X であるインデックス i のうち最大のもの（存在しなければ None）を返す
def max_lt_idx(A,X):
    res=bisect_left(A,X)-1
    if res==-1:
        res=None
    return res
        

# 配列 A において, 値が L 以上 R 以下となる区間を返す
# インデックスの半開区間 [l,r) で返す （区間が存在しなければ l = r）
def range_idx(A,L,R):
    l=bisect_left(A,L)
    r=bisect_right(A,R)
    return l,r



# -----------------------------  要素取得  ----------------------------------------

# 配列 A に含まれる, X 以上の数のうち最小のもの（存在しなければ None）を返す
def min_ge_val(A,X):
    idx=bisect_left(A,X)
    if idx==len(A):
        return None
    return A[idx]

# 配列 A に含まれる, X より大きい数のうち最小のもの（存在しなければ None）を返す
def min_gt_val(A,X):
    idx=bisect_right(A,X)
    if idx==len(A):
        return None
    return A[idx]

# 配列 A に含まれる, X 以下の数のうち最大のもの（存在しなければ None）を返す
def max_le_val(A,X):
    idx=bisect_right(A,X)-1
    if idx==-1:
        return None
    return A[idx]

# 配列 A に含まれる, X より小さい数のうち最大のもの（存在しなければ None）を返す
def max_lt_val(A,X):
    idx=bisect_left(A,X)-1
    if idx==-1:
        return None
    return A[idx]


# 配列 A に含まれる要素のうち, X に最も近い（差の絶対値が最小）ものを返す
# 結果をリストに入れて返す（結果が2つある場合は2つとも入れる）
def closest_vals(A,X):
    if len(A)==0:
        return None
    idx=bisect_left(A,X)
    if idx==0:
        return [A[0]]
    if idx==len(A):
        return [A[-1]]
    left_val=A[idx-1]
    right_val=A[idx]
    if X-left_val<right_val-X:
        return [left_val]
    elif X-left_val>right_val-X:
        return [right_val]
    else:
        return [left_val,right_val]



# ----------------------------  要素数カウント  -----------------------------------

# 配列 A に含まれる, X 以上の要素の個数を返す
def count_ge(A,X):
    return len(A)-bisect_left(A,X)

# 配列 A に含まれる, X より大きい要素の個数を返す
def count_gt(A,X):
    return len(A)-bisect_right(A,X)

# 配列 A に含まれる, X 以下の要素の個数を返す
def count_le(A,X):
    return bisect_right(A,X)

# 配列 A に含まれる, X より小さい要素の個数を返す
def count_lt(A,X):
    return bisect_left(A,X)


# 配列 A に 値 X が含まれているか（True / False）を返す
def is_exist(A,X):
    idx=bisect_left(A,X)
    return idx<len(A) and A[idx]==X

# 配列 A に含まれる, 値 X の個数を返す
def count_val(A,X):
    return bisect_right(A,X)-bisect_left(A,X)

# 配列 A に含まれる, L 以上 R 以下の要素の個数を返す
def count_range(A,L,R):
    return bisect_right(A,R)-bisect_left(A,L)