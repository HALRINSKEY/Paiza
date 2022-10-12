times = int(input())

for i in range(times):

    year = int(input())

    if year % 4 == 0:
        if year % 100 != 0:
            print("{} is leap year".format(year))
        else:
            if year % 400 == 0:
                print("{} is leap year".format(year))
            else:
                print("{} is not a leap year".format(year))
    else:
        print("{} is not a leap year".format(year))