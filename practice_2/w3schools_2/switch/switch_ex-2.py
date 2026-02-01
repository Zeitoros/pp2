status = 404

match status:
    case 200:
        print("OK!")
    case 400:
        print("Error request!")
    case 404:
        print("Page is not found")
    case 500 | 503:
        print("Error server")
    case _:
        print("Unknown status")