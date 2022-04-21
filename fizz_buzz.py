import sys

try:
    n = int(input())

except ValueError:
    print("整数を入力してください")
    sys.exit()

if n < 1:
    print("1以上100以下の整数を入力してください")
    sys.exit()

elif n > 100:
    print("1以上100以下の整数を入力してください")
    sys.exit()

for i in range(1, n + 1):
    if (i % 3) == 0 and (i % 5) == 0:
        print("Fizz Buzz")
    elif (i % 3) == 0:
        print("Fizz")
    elif (i % 5) == 0:
        print("Buzz")
    else:
        print(i)
