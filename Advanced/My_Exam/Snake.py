def movement(territory, row, col, food_quantity, burrows):
    if territory[row][col] == "*":
        food_quantity += 1
    elif territory[row][col] == "B":
        if [row, col] in burrows:
            burrows.remove([row, col])
        territory[row][col] = "."
        row = burrows[0][0]
        col = burrows[0][1]
    return territory, row, col, food_quantity, burrows


n = int(input())
territory = [[ch for ch in input()] for x in range(n)]

burrows = []
food_count = 0
for i in range(n):
    for j in range(n):
        if territory[i][j] == "S":
            row = i
            col = j
        elif territory[i][j] == "B":
            burrows.append([i,j])
        elif territory[i][j] == "*":
            food_count += 1
food_quantity = 0
is_dead = False
is_win = False
while True:
    command = input()
    if command == "up":
        if -1 < row -1 < n:
            territory[row][col] = "."
            row -= 1
            territory, row, col, food_quantity,burrows = movement(territory, row, col, food_quantity, burrows)
        else:
            is_dead = True
    elif command == "down":
        if -1 < row + 1 < n:
            territory[row][col] = "."
            row += 1
            territory, row, col, food_quantity, burrows = movement(territory, row, col, food_quantity, burrows)
        else:
            is_dead = True
    elif command == "left":
        if -1 < col - 1 < n:
            territory[row][col] = "."
            col -= 1
            territory, row, col, food_quantity, burrows = movement(territory, row, col, food_quantity, burrows)
        else:
            is_dead = True
    elif command == "right":
        if -1 < col + 1 < n:
            territory[row][col] = "."
            col += 1
            territory, row, col, food_quantity, burrows = movement(territory, row, col, food_quantity, burrows)
        else:
            is_dead = True
    territory[row][col] = "S"
    if is_dead:
        break
    if food_quantity >= 10:
        is_win = True
        break


if is_dead:
    territory[row][col] = "."
    print("Game over!")
if is_win:
    print("You won! You fed the snake.")
print(f"Food eaten: {food_quantity}")

for i in range(n):
    for j in range(n):
        print(f"{territory[i][j]}", end="")
    print()


