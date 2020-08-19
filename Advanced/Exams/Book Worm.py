worm = input()
n = int(input())
field = [[ch for ch in input()] for x in range(n)]
m = int(input())

for i in range(n):
    for j in range(n):
        if field[i][j] == "P":
            row = i
            col = j

for i in range(m):
    command = input()
    if command == "up":
        if -1 < row - 1 < n:
            field[row][col] = "-"
            row -= 1
            if field[row][col].isalpha():
                worm += field[row][col]
                field[row][col] = "P"
        else:
            if len(worm) > 0:
                worm = worm[:-1]
    elif command == "down":
        if -1 < row + 1 < n:
            field[row][col] = "-"
            row += 1
            if field[row][col].isalpha():
                worm += field[row][col]
                field[row][col] = "P"
        else:
            if len(worm) > 0:
                worm = worm[:-1]
    elif command == "left":
        if -1 < col - 1 < n:
            field[row][col] = "-"
            col -= 1
            if field[row][col].isalpha():
                worm += field[row][col]
                field[row][col] = "P"
        else:
            if len(worm) > 0:
                worm = worm[:-1]
    elif command == "right":
        if -1 < col + 1 < n:
            field[row][col] = "-"
            col += 1
            if field[row][col].isalpha():
                worm += field[row][col]
                field[row][col] = "P"
        else:
            if len(worm) > 0:
                worm = worm[:-1]

print(worm)
for i in range(n):
    for j in range(n):
        print(field[i][j], end="")
    print()
