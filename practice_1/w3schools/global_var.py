x = "there" # Global variable
def test():
    x = "World" # local variable
    print("Hello " + x)
    
test()
print("Hello " + x)


def test_2():
    global z # make the variable z global
    z = 27

test_2()
print("Number:", z)