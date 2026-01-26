var = "Hello World" # String

n = len(var) # Length of the string

format = f"It is {var}"; print("Format:", format) # f - way of formatting strings

first_char = var[0]; print("First letter:", first_char) # indexing begins from 0

last_char = var[-1]; print("Last letter:", last_char) # last element is -1

interval = var[6:11]; print("Slice:", interval) # World

reverse = var[::-1]; print("Reversed:", reverse) # This slice reverse each word and order of the string

words = var.split(); print("List of string:", words) # This method divide the string into an array of substrings
