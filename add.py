integer_set = []
answer = 0

def add():
    integer_set = input().split(" ")

    if integer_set[0] == integer_set[1]:
        return( int(integer_set[0]) * int(integer_set[1]) )
    else:
        return( int(integer_set[0]) + int(integer_set[1]) )

calc_times = int(input())

for i in range(calc_times):
    answer += add()

print(answer)