n = int(input())

field = [input().split() for i in range(n)]
steps = {}
for i in range(n):
    for j in range(n):
        if field[i][j] == "B":
            bunny = [i, j]

steps = {
    "up": [],
    "down": [],
    "left": [],
    "right": []
}

directions = {}

for k in steps.keys():
    if k == "up":
        for i in range(bunny[0] - 1, -1, -1):
            if field[i][bunny[1]] == "X":
                break
            else:
                if k not in directions:
                    directions[k] = int(field[i][bunny[1]])
                else:
                    directions[k] += int(field[i][bunny[1]])
                steps[k].append([i, bunny[1]])
    elif k == "down":
        for i in range(bunny[0] + 1, n):
            if field[i][bunny[1]] == "X":
                break
            else:
                if k not in directions:
                    directions[k] = int(field[i][bunny[1]])
                else:
                    directions[k] += int(field[i][bunny[1]])
                steps[k].append([i, bunny[1]])
    elif k == "left":
        for i in range(bunny[1] - 1, -1, -1):
            if field[bunny[0]][i] == "X":
                break
            else:
                if k not in directions:
                    directions[k] = int(field[bunny[0]][i])
                else:
                    directions[k] += int(field[bunny[0]][i])
                steps[k].append([bunny[0], i])
    elif k == "right":
        for i in range(bunny[1] + 1, n):
            if field[bunny[0]][i] == "X":
                break
            else:
                if k not in directions:
                    directions[k] = int(field[bunny[0]][i])
                else:
                    directions[k] += int(field[bunny[0]][i])
                steps[k].append([bunny[0], i])

directions = dict(sorted(directions.items(), key=lambda x: -x[1]))

print(list(directions.keys())[0])
for each in steps[list(directions.keys())[0]]:
    print(each)

print(directions[list(directions)[0]])



