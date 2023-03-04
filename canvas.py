class Canvas:
    board = []
    order = []

    def __init__(self):
        pass

    def input_order(self):
        self.order = input().split()
        self.order = [int(o) for o in self.order]

    def make_board(self):
        for i in range(self.order[1]):
            self.board.append(list())
            for j in range(self.order[2]):
                self.board[i].append(0)

    def input_order_canvas(self):
        self.order = input().split()
        self.order = [int(o) for o in self.order]

    def do_order(self):
        if self.order[1] == self.order[3] and self.order[2] == self.order[4]:
            self.board[self.order[2]][self.order[1]] += self.order[0]

        elif self.order[2] == self.order[4]:

            y = self.order[2]

            if self.order[1] < self.order[3]:
                for x in range(self.order[1],self.order[3] + 1):
                    self.board[y][x] += self.order[0]

            elif self.order[3] < self.order[1]:
                for x in range(self.order[3],self.order[1] + 1):
                    self.board[y][x] += self.order[0]

        elif self.order[1] == self.order[3]:

            x = self.order[1]

            if self.order[2] < self.order[4]:
                for y in range(self.order[2],self.order[4] + 1):
                    self.board[y][x] += self.order[0]

            elif self.order[2] > self.order[4]:
                for y in range(self.order[4],self.order[2] + 1):
                    self.board[y][x] += self.order[0]

    def control(self):
        self.input_order()
        self.make_board()
        for i in range(self.order[0]):
            self.input_order_canvas()
            self.do_order()

        for a in self.board:
            print(*a)


c = Canvas()
c.control()
