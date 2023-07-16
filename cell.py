a_cell = int(input())
bc = input().split(" ")
time = int(input())

b_cell_num = int(bc[0])#b細胞に分裂する数
c_cell_num = int(bc[1])#c細胞に分裂する数

b_cell = 0
c_cell = 0
c_to_a = 0

for t in range(time):
    #c細胞の分裂
    c_to_a = int(c_cell / 2)
    c_cell -= int(c_cell / 2)
    #a細胞の分裂
    b_cell += int(a_cell / 2) * b_cell_num
    c_cell += int(a_cell / 2) * c_cell_num
    a_cell -= int(a_cell / 2)
    #c細胞から分裂してきたa細胞
    a_cell += c_to_a

print(a_cell)
print(b_cell)
print(c_cell)