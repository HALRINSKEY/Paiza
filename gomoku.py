class Gomoku:
    board = []
    
    def __init__(self):
        self.x_is_ok = 0
        self.y_is_ok = 0
        self.closs_is_ok = 0

    def input_board(self):
        for i in range(5):
            self.board.append(list(input()))

    def judge(self):
        #beside
        for y in range(5):
            if self.board[y][0] == self.board[y][1] == self.board[y][2] == self.board[y][3] == self.board[y][4]:
                if self.board[y][0] != ".":
                    self.x_is_ok += 1
                    self.output(self.board[y][0])
                else:
                    continue

                
        #vertical
        for x in range(5):
            if self.board[0][x] == self.board[1][x] == self.board[2][x] == self.board[3][x] == self.board[4][x]:
                if self.board[0][x] != ".":
                    self.y_is_ok += 1
                    self.output(self.board[0][x])
                else:
                    continue

        #closs
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == self.board[3][3] == self.board[4][4] or \
            self.board[0][4] == self.board[1][3] == self.board[2][2] == self.board[3][1] == self.board[4][0]:
            if self.board[2][2] != ".":
                self.closs_is_ok += 1
                self.output(self.board[2][2])

        if self.x_is_ok == self.y_is_ok == self.closs_is_ok == 0:
            self.output("D")

    def output(self, b):
        print(b)

p1 = Gomoku()
p1.input_board()
p1.judge()

#解答例###################################################################
board = []

for i in range(5):
    board.append(input())


def row():
    result = "D"

    for line in board:
        pivot = line[0]
        count = 0

        for stone in line:
            if stone != "." and stone == pivot:
                count += 1
            else:
                break

        if count == 5:
            result = pivot
            break

    return result


def column():
    result = "D"

    for i in range(5):
        pivot = ""
        count = 0

        for j in range(5):
            if pivot == "":
                pivot = board[j][i]

            stone = board[j][i]
            if stone != "." and stone == pivot:
                count += 1
            else:
                break

        if count == 5:
            result = pivot
            break

    return result


def oblique():
    result = "D"
    direction = [True, False]

    for reverse in direction:
        pivot = ""
        count = 0

        if reverse:
            j = 0
            j_diff = 1
        else:
            j = 4
            j_diff = -1

        for i in range(5):

            stone = board[i][j]

            if pivot == "":
                pivot = stone

            if stone != "." and stone == pivot:
                count += 1

            j = j + j_diff

        if count == 5:
            result = pivot
            break

    return result


row = row()
column = column()
oblique = oblique()

if row != "D":
    print(row)
elif column != "D":
    print(column)
elif oblique != "D":
    print(oblique)
else:
    print("D")