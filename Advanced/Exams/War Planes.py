n = int(input())
field = [input().split() for x in range(n)]
targets = []
free_space = []
for i in range(n):
    for j in range(n):
        if field[i][j] == "p":
            cp = (i, j)
        elif field[i][j] == "t":
            targets.append((i, j))
        elif field[i][j] == ".":
            free_space.append((i, j))
targets_count = len(targets)
m = int(input())
for s in range(m):
    command = input().split()
    if command[1] == "down":
        if -1 < cp[0] + int(command[2]) < n:
            if field[cp[0] + int(command[2])][cp[1]] == ".":
                if command[0] == "shoot":
                    field[cp[0] + int(command[2])][cp[1]] = "x"
                elif command[0] == "move":
                    field[cp[0]][cp[1]] = "."
                    cp = (cp[0] + int(command[2]), cp[1])
                    field[cp[0]][cp[1]] = "p"
            elif field[cp[0] + int(command[2])][cp[1]] == "t":
                if command[0] == "shoot":
                    field[cp[0] + int(command[2])][cp[1]] = "x"
                    targets_count -= 1
    elif command[1] == "up":
        if -1 < cp[0] - int(command[2]) < n:
            if field[cp[0] - int(command[2])][cp[1]] == ".":
                if command[0] == "shoot":
                    field[cp[0] - int(command[2])][cp[1]] = "x"
                elif command[0] == "move":
                    field[cp[0]][cp[1]] = "."
                    cp = (cp[0] - int(command[2]), cp[1])
                    field[cp[0]][cp[1]] = "p"
            elif field[cp[0] - int(command[2])][cp[1]] == "t":
                if command[0] == "shoot":
                    field[cp[0] - int(command[2])][cp[1]] = "x"
                    targets_count -= 1
    elif command[1] == "right":
        if -1 < cp[1] + int(command[2]) < n:
            if field[cp[0]][cp[1] + int(command[2])] == ".":
                if command[0] == "shoot":
                    field[cp[0]][cp[1] + int(command[2])] = "x"
                elif command[0] == "move":
                    field[cp[0]][cp[1]] = "."
                    cp = (cp[0], cp[1] + int(command[2]))
                    field[cp[0]][cp[1]] = "p"
            elif field[cp[0]][cp[1] + int(command[2])] == "t":
                if command[0] == "shoot":
                    field[cp[0]][cp[1] + int(command[2])] = "x"
                    targets_count -= 1
    elif command[1] == "left":
        if -1 < cp[1] - int(command[2]) < n:
            if field[cp[0]][cp[1] - int(command[2])] == ".":
                if command[0] == "shoot":
                    field[cp[0]][cp[1] - int(command[2])] = "x"
                elif command[0] == "move":
                    field[cp[0]][cp[1]] = "."
                    cp = (cp[0], cp[1] - int(command[2]))
                    field[cp[0]][cp[1]] = "p"
            elif field[cp[0]][cp[1] - int(command[2])] == "t":
                if command[0] == "shoot":
                    field[cp[0]][cp[1] - int(command[2])] = "x"
                    targets_count -= 1

if targets_count <= 0:
    print(f"Mission accomplished! All {len(targets)} targets destroyed.")
else:
    print(f"Mission failed! {targets_count} targets left.")

for each in field:
    print(" ".join([x for x in each]))
