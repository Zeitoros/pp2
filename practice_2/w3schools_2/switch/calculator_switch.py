num1 = float(input())
num2 = float(input())
op = input()

match op:
    case "+":
        print(f"Sum: {num1} + {num2} = {num1+num2}")
    case "-":
        print(f"Diff: {num1} - {num2} = {num1-num2}")
    case "*":
        print(f"Multi: {num1} * {num2} = {num1*num2}")
    case "/":
        if (num2 == 0):
            print("Error!")
        else:
            print(f"Div: {num1} / {num2} = {num1/num2}")
    case _:
        print("...")