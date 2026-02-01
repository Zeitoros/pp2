n = int(input())
i = 0

while (i <= n):
    if (i % 2 == 0 and i != 0):  # if i is even and not equals 0
        print(i, end=" ") # print i which is even (exclude 0)
    i += 1 # incrementation