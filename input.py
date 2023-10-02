#3
size = int(input())
# 1 2 3 4
maps = [int(i) for i in input().split(" ")]
maps = list(map(int, input().split(" "))) #map()は組み込みの関数です。第1引数の関数を第2引数のリストの要素に適用します。

#2 4
#1 2 3 4
#5 6 7 8

size = [int(i) for i in input().split(" ")]
y = size[0] #2
x = size[1] #4

for i in range(y):
    maps = [int(j) for j in input().split(" ")]