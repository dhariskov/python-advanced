heroes = {name: {} for name in input().split(", ")}

while True:
    command = input().split("-")
    if command[0] == "End":
        break
    if command[1] not in heroes[command[0]]:
        heroes[command[0]][command[1]] = int(command[2])

print("\n".join([f"{name} -> Items: {len(heroes[name])}, Cost: {sum(heroes[name].values())}" for name in heroes]))
