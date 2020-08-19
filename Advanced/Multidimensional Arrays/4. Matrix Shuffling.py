def check_valid_input(matrix, command, r, c):
    if command[0] == "swap" and len(command) == 5:
        if (-1 < int(command[1]) < r) and (-1 < int(command[2]) < c) or (
                -1 < int(command[3]) < r) and (-1 < int(command[4]) < c):
            return True
        else:
            return False
    else:
        return False


r, c = [int(x) for x in input().split()]
matrix = []
for row in range(r):
    matrix.append([col for col in input().split()])

temp = None
while True:
    command = input().split()
    if command[0] == "END":
        break
    if check_valid_input(matrix, command, r, c):
        matrix[int(command[1])][int(command[2])], matrix[int(command[3])][int(command[4])] =\
            matrix[int(command[3])][int(command[4])], matrix[int(command[1])][int(command[2])]
        for i in range(r):
            for j in range(c):
                print(matrix[i][j], end=" ")
            print()
    else:
        print("Invalid input!")
