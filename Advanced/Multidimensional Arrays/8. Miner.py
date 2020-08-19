def movement(matrix, current_position, coals_count):
    if matrix[current_position[0]][current_position[1]] == "c":
        matrix[current_position[0]][current_position[1]] = "*"
        coals_count -= 1
        if coals_count == 0:
            print(f"You collected all coals! ({current_position[0]}, {current_position[1]})")
            return None
    elif matrix[current_position[0]][current_position[1]] == "e":
        print(f"Game over! ({current_position[0]}, {current_position[1]})")
        return None
    return coals_count


n = int(input())
commands = input().split()
matrix = []
for _ in range(n):
    matrix.append(input().split())

coals_count = 0
starting_position = []
end_position = []
regular_positions = []

for i in range(n):
    for j in range(n):
        if matrix[i][j] == "c":
            coals_count += 1
        elif matrix[i][j] == "s":
            starting_position = [i, j]

current_position = starting_position
is_over = False
while commands:
    current_command = commands[0]
    if current_command == "left":
        if current_position[1] != 0:
            current_position[1] -= 1
            coals_count = movement(matrix, current_position, coals_count)
            if coals_count is None:
                is_over = True
                break
    elif current_command == "right":
        if current_position[1] != n - 1:
            current_position[1] += 1
            coals_count = movement(matrix, current_position, coals_count)
            if coals_count is None:
                is_over = True
                break
    elif current_command == "up":
        if current_position[0] != 0:
            current_position[0] -= 1
            coals_count = movement(matrix, current_position, coals_count)
            if coals_count is None:
                is_over = True
                break
    elif current_command == "down":
        if current_position[0] != n - 1:
            current_position[0] += 1
            coals_count = movement(matrix, current_position, coals_count)
            if coals_count is None:
                is_over = True
                break
    commands.pop(0)


if len(commands) == 0 and (not is_over):
    print(f"{coals_count} coals left. ({current_position[0]}, {current_position[1]})")