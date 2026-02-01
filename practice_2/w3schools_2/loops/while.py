n = int(input())
i = 0

while (i <= n):
    if (i % 2 == 0 and i != 0):  # if i is even and not equals 0
        print(i, end=" ") # print i which is even (exclude 0)
    i += 1 # incrementation

print(" ") # separator between two loops

i = 1
while i < 6:
    print(i, end=" ")
    if i == 3:
        break # loop stops when i == 3
    i += 1