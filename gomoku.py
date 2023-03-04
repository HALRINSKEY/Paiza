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


