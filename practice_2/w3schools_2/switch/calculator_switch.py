while True:
    command = input("Введите команду: ").lower().split()

    match command:
        case ["exit" | "quit" | "выход" | "q"]:
            print("Shut down...")
            break

        case ["add", x, y]:
            print(f"Result: {float(x) + float(y)}")

        case ["sub", x, y]:
            print(f"Result: {float(x) - float(y)}")

        case ["mult", x, y]:
            print(f"Result: {float(x) * float(y)}")

        case ["div", _, "0"]:
            print("Error: Division by zero is impossible!")

        case ["div", x, y]:
            print(f"Result: {float(x) / float(y)}")

        case []:
            continue

        case _:
            print("Error!")