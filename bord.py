class Board:
    def __init__(self):
        self.board_map = []
        self.max_number = 0

    def input(self):
        self.size = input().split(" ") #3 4
        for i in range(int(self.size[0])):
            t = [int(j) for j in input().split(" ")] # 1 1 2 1
            self.board_map.append(t)



    

b = Board()
b.input()
print(b.board_map)
    