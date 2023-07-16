import copy

class Puzzle():
    def __init__(self):
        self.output_num = 0

    def input_list(self):
        self.list_num = int(input())
        #単語をリストに格納
        self.word_list = []
        for n in range(self.list_num):
            self.word_list.append(input())
        #リスト内の単語を並び変えたリストを作成
        self.sort_list = []
        for sl in self.word_list:
            self.sort_list.append(sorted(sl))


    def find_word(self):
        word_list_2 = copy.deepcopy(self.word_list)#組み合わせる単語用のリストを作成
        for wl1 in self.word_list:
            for wl2 in word_list_2:
                combination_word = wl1 + wl2

                for sl in self.sort_list:#ソートして比較
                    if sl == sorted(combination_word):
                        self.output_num += 1


            word_list_2.pop(0)#比較済みの組み合わせ消去



puzzle = Puzzle()
puzzle.input_list()
puzzle.find_word()
print(puzzle.output_num)