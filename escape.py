class Escape():
    board = []
    boardsize = []

    def __init__(self):
        self.x = 0
        self.y = 0

    def make_board(self):
        self.boardsize = input().split(" ")
        for i in range(int(self.boardsize[0])):
            self.board.append(list(input()))

    def side(self):
        upper_side = "".join(self.board[0])
        lower_side = "".join(self.board[-1])

        right = []
        for i in range(int(self.boardsize[0])):
            right.append(self.board[i][0])
        right_side = "".join(right)

        left  =[]
        for i in range(int(self.boardsize[0])):
            left.append(self.board[i][int(self.boardsize[1]) - 1])
        left_side = "".join(left)

        if "#.#" in upper_side or "#.#" in lower_side or "#.#" in right_side or "#.#" in left_side:
            self.find()
        else:
            print("NO")

    def pos(self):
        for s ,new in enumerate(self.board):
            new = "".join(self.board[s])
            if "S" in new:
                self.x = new.index("S")
                self.y = s


    def find(self):
        while True:
            if self.board[self.y + 1][self.x] == ".":
                self.board[self.y + 1][self.x] = "S"
                self.y += 1
            elif self.board[self.y - 1][self.x] == ".":
                self.board[self.y - 1][self.x] = "S"
                self.y -= 1
            elif self.board[self.y][self.x + 1] == ".":
                self.board[self.y][self.x + 1] = "S"
                self.x += 1
            elif self.board[self.y][self.x - 1] == ".":
                self.board[self.y][self.x - 1] = "S"
                self.x -= 1
            else:
                if self.x == 0 or self.x == int(self.boardsize[1]) - 1:
                    print("YES")
                    break
                elif self.y == 0 or self.y == int(self.boardsize[0]) - 1:
                    print("YES")
                    break
                else:
                    print("NO")
                    break

e = Escape()
e.make_board()
e.pos()
e.side()

            
            
            
