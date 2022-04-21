def decoration(s):
    for i in range(s + 2):
        print("+", end = "")

    print("")

s = input()
n = len(s)

decoration(n)
print("+{}+".format(s))
decoration(n)
