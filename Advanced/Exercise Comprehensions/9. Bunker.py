bunker = {name: {} for name in input().split(", ")}

for _ in range(int(input())):
    command = input().split(" - ")
    qq = command[2].split(";")
    quantity = qq[0].replace("quantity:", "")
    quality = qq[1].replace("quality:", "")
    bunker[command[0]][command[1]] = int(quantity),int(quality)


print(f'Count of items: {sum([bunker[food][q][0] for food in bunker for q in bunker[food]])}')
result =(sum([bunker[food][q][1] for food in bunker for q in bunker[food]])) / len(bunker)
print(f"Average quality: {result:.2f}")
print("\n".join([f"{food} -> {', '.join(bunker[food])}" for food in bunker]))
