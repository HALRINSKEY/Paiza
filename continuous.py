#import cProfile
class RecordWoke():
    def __init__(self):
        self.working_days = []
        self.most_working_days = 0

    def input_work(self):
        num = int(input())#max10000
        for i in range(num):
            self.working_days.append(list(map(int,input().split(" "))))#max1,100000

        self.working_days.sort()

    def continuous_chk(self):
        start_day = self.working_days[0][0]
        finish_day = self.working_days[0][1]
        working_list = []
        
        for work in self.working_days:
            if work[0] in list(range(start_day, finish_day + 2)) and finish_day < work[1]:
                finish_day = work[1]#list合体1,3 + 2,5 => 1,5
            elif finish_day < work[0]:#1,5 => 7,10
                working_list.append(finish_day - start_day + 1)
                start_day = work[0]
                finish_day = work[1]
                
        working_list.append(finish_day - start_day + 1)

        return max(working_list)



r = RecordWoke()
r.input_work()
print(r.continuous_chk())    



#def main():
#    r = RecordWoke()
#    r.input_work()
#     
#    print(r.continuous_chk())
#
#cProfile.run('main()')