from itertools import combinations
#場所に基づいた昇順で組み合わせ
list(combinations(range(5),3))

from itertools import combinations_with_replacement
#combinationsの、重複を許すバージョン
list(combinations_with_replacement(range(5),3))

from itertools import permutations
#順列
list(permutations(range(4))) #0,1,2,3の順列
A=["a","b","c"]
list(permutations(A,2)) #Aのうち2つを取り出し順列

#重複を除いた順列全探索をできる
#itertools.permutationsで全列挙してからsetを用いる方法より高速
from more_itertools import distinct_permutations

#直積
from itertools import product
A,B,C=[1,2,3],[4,5,6],[7,8,9]
list(product(A,B))
list(product(A,B,C))

#配列Aから1つ要素を選ぶのを3回繰り返し（重複順列）
list(product(A,repeat=3)) 

#配列Aから1つ要素を選ぶのを3回繰り返した結果の重複なしver.(重複組み合わせ)
from itertools import combinations_with_replacement
list(combinations_with_replacement(A,3))

from itertools import groupby
#ランレングス圧縮 (要素、そのグループの長さ)
A="aabbcc"
RLE=[(key,len(list(group))) for key,group in groupby(A)]
print(RLE)
