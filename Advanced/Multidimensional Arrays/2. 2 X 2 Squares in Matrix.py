def check_equal_el_2x2(matrix, row, col):
    if matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1]:
        return 1
    else:
        return 0


r, c = [int(x) for x in input().split()]

matrix = []
counter = 0
for row in range(r):
    matrix.append(input().split())

for row in range(r - 1):
    for col in range(c - 1):
        counter += check_equal_el_2x2(matrix, row, col)

print(counter)
