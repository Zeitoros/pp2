for i in range(5):
    print(f"Step #{i}")


for i in range(1, 6):
    if i % 2 == 0:
        continue  # skip even numbers
    print(f"Odd number: {i}")


items = ["coin", "enemy", "health_pack"]

for item in items:
    if item == "coin":
        print("Add 10 pts")
    elif item == "enemy":
        pass  # TODO: add a logic for getting damage later
    elif item == "health_pack":
        print("Healing...")