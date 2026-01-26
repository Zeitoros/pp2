sentence = input()
target = input()
replacement = input()
var = ""

if (target in sentence):
    var = sentence.replace(target, replacement)
    print(var)
else:
    print(sentence)