n = int(input())
matrix = [[int(each) for each in input().split()] for x in range(n)]
while True:
    coordinates = input().split()
    if coordinates[0] == "END":
        break
    command = coordinates[0]
    row = int(coordinates[1])
    col = int(coordinates[2])
    value = int(coordinates[3])
    if 0 <= row < n and 0 <= col < n:
        if command == "Add":
            matrix[row][col] += value
        elif command == "Subtract":
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")

matrix = [[str(matrix[x][each]) for each in range(n)] for x in range(n)]
for each in matrix:
    print(" ".join([x for x in each]))
