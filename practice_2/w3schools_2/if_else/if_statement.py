phrase = "Hello, World!"
target = input()

if (target in phrase):
    print(f"{target} is IN \"{phrase}\"")
else:
    print(f"{target} is NOT in \"{phrase}\"")