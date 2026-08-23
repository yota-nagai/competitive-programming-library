from bisect import bisect_left,bisect_right

#配列Aに含まれる、Xより小さい要素の個数
def less(A,X):
    return bisect_left(A,X)

#配列Aに含まれる、X以下の要素の個数
def less_equal(A,X):
    return bisect_right(A,X)

#配列Aに含まれる、Xより大きい要素の個数
def greater(A,X):
    return len(A)-bisect_right(A,X)

#配列Aに含まれる、X以上の要素の個数
def greater_equal(A,X):
    return len(A)-bisect_left(A,X)

#配列Aに含まれる、Xと同じ要素の個数
def equal(A,X):
    return bisect_right(A,X)-bisect_left(A,X)

#配列Aの中でXは何番目の要素であるか（重複要素なし、1-indexed）
def idx_1(A,X):
    if bisect_right(A,X)-bisect_left(A,X)==0:
        return False
    return bisect_right(A,X)

#配列Aの中でXは何番目の要素であるか（重複要素なし、0-indexed）
def idx_0(A,X):
    if bisect_right(A,X)-bisect_left(A,X)==0:
        return False
    return bisect_left(A,X)
