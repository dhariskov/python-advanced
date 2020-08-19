n = int(input())
matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split()])

coordinates = input().split()
coordinates = [each.split(",") for each in coordinates]
for r in range(len(coordinates)):
    for c in range(len(coordinates[r])):
        coordinates[r][c] = int(coordinates[r][c])
current_bomb = 0
for _ in range(len(coordinates)):
    current_bomb = coordinates[0]
    if matrix[current_bomb[0]][current_bomb[1]] > 0:
        for row in range(current_bomb[0] - 1, current_bomb[0] + 2):
            for col in range(current_bomb[1] - 1, current_bomb[1] + 2):
                if -1 < row < n and -1 < col < n:
                    if [row, col] != current_bomb:
                        if matrix[row][col] > 0:
                            matrix[row][col] -= matrix[current_bomb[0]][current_bomb[1]]
        matrix[current_bomb[0]][current_bomb[1]] = 0
        # print(matrix)
        coordinates.append(coordinates.pop(0))
active_cells = 0
sum_active_cells = 0

for i in range(n):
    for j in range(n):
        if matrix[i][j] > 0:
            active_cells += 1
            sum_active_cells += matrix[i][j]

print(f"Alive cells: {active_cells}")
print(f"Sum: {sum_active_cells}")
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()
