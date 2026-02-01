semester = input()

match semester:
    case "fall":
        print("September - December")
    case "spring":
        print("January - May")
    case _:
        print("Other")