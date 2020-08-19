import copy

n, m = (int(x) for x in input().split())

lair = []
copy_lair = []
for i in range(n):
    lair.append([ch for ch in input()])
commands = [ch for ch in input()]
copy_lair = copy.deepcopy(lair)
bunnies = []
player = []
end_game = False
is_player_alive = True
while not end_game:
    copy_lair = copy.deepcopy(lair)
    current_command = commands.pop(0)
    is_player_alive = False
    for i in range(n):
        for j in range(m):
            if lair[i][j] == "P":
                player = [i, j]
                is_player_alive = True
                break
        if is_player_alive:
            break
    if not is_player_alive:
        print(f"dead: {player[0]}{player[1]}")
        break

    if current_command == "L":
        if player[1] != 0:
            lair[player[0]][player[1]] = "."
            player[1] -= 1
            if lair[player[0]][player[1]] == "B":
                print(f"dead: {player[0]}{player[1]}")
            else:
                lair[player[0]][player[1]] = "P"
        else:
            print(f"won: {player[0]} {player[1]}")
            end_game = True
    elif current_command == "R":
        if player[1] != n - 1:
            lair[player[0]][player[1]] = "."
            player[1] += 1
            if lair[player[0]][player[1]] == "B":
                print(f"dead: {player[0]}{player[1]}")
            else:
                lair[player[0]][player[1]] = "P"
        else:
            print(f"won: {player[0]} {player[1]}")
            end_game = True
    elif current_command == "U":
        if player[0] != 0:
            lair[player[0]][player[1]] = "."
            player[0] -= 1
            if lair[player[0]][player[1]] == "B":
                print(f"dead: {player[0]}{player[1]}")
            else:
                lair[player[0]][player[1]] = "P"
        else:
            print(f"won: {player[0]} {player[1]}")
            end_game = True
    elif current_command == "D":
        if player[0] != n - 1:
            lair[player[0]][player[1]] = "."
            player[0] += 1
            if lair[player[0]][player[1]] == "B":
                print(f"dead: {player[0]}{player[1]}")
            else:
                lair[player[0]][player[1]] = "P"
        else:
            print(f"won: {player[0]} {player[1]}")
            end_game = True
    for row in range(n):
        for col in range(m):
            if lair[row][col] == "B":
                if 0 <= row - 1:
                    copy_lair[row - 1][col] = "B"
                if row + 1 <= n - 1:
                    copy_lair[row][col] = "B"
                if 0 <= col - 1:
                    copy_lair[row][col - 1] = "B"
                if col + 1 <= m - 1:
                    copy_lair[row][col + 1] = "B"
