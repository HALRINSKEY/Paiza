def check(j, i):
    sea[j][i] = 0

    if sea[j + 1][i]:
        check(j + 1, i)

    if sea[j - 1][i]:
        check(j - 1, i)

    if sea[j][i + 1]:
        check(j, i + 1)

    if sea[j][i - 1]:
        check(j, i - 1)

field_range = [int(a) for a in input().split(" ")]#範囲入力[x,y]
sea = []

for a in range(field_range[1]):
    l = [int(a) for a in input().split(" ")]#0 or 1の入力
    sea.append(l)

#0で囲う
sea_top = [0]
sea_top = sea_top * field_range[0]
sea_bottom = [0]
sea_bottom = sea_bottom * field_range[0]
sea.insert(0, sea_top)
sea.insert(-1, sea_bottom)

for a in range(field_range[1] + 2):
    sea[a].insert(0,0)
    sea[a].insert(-1,0)

#    print(sea[y][x])


for j in range(field_range[1] + 2):
    for i in range(field_range[0] + 2):
        if sea[j][i] == 1:
            check(j, i)

print(sea)
