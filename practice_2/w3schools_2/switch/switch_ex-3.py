def execute(command):
    match command:
        case ["quit"]:
            print("Shut down...")

        case ["move", "left" | "right" | "up" | "down" as direction]:
            print(f"The robot is moving in the direction: {direction}")

        case ["move", int(x), int(y)]:
            print(f"The robot moves to the point with coordinates ({x}, {y})")

        case ["say", *words]:
            sentence = " ".join(words)
            print(f'Robot says: "{sentence}"')

        case _:
            print("Error: Command not recognized or invalid parameters.")


execute(["move", "up"])
execute(["move", 10, 50])
execute(["say", "Hello", "World!"])
execute(["move", "on Mars"])