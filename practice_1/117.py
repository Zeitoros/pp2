words = input().split()

if (len(words) >= 2):
    words[0], words[1] = words[1], words[0]

print(*words)