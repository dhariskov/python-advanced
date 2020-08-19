r, c = [int(x) for x in input().split()]

matrix = []
for row in range(r):
    matrix.append([int(x) for x in input().split()])

biggest_sum = 0
for row in range(3):
    for col in range(3):
        biggest_sum += matrix[row][col]

current_sum = 0
biggest_matrix = [[0, 0, 0]] * 3
last_index = (2, 2)
for row in range(r-2):
    for col in range(c-2):
        current_sum = 0
        for i in range(3):
            for j in range(3):
                current_sum += matrix[row+i][col+j]
        if biggest_sum < current_sum:
            biggest_sum = current_sum
            last_index = (row+i, col+j)

print(f'Sum = {biggest_sum}')
for m in range(last_index[0]-2, last_index[0]+1):
    for k in range(last_index[1]-2, last_index[1]+1):
        print(matrix[m][k], end=" ")
    print()

