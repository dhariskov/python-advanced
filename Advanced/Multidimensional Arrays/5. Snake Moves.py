from collections import deque

r, c = [int(x) for x in input().split()]
text = deque([ch for ch in input()])
matrix = []
for i in range(r):
    matrix.append(["x"]*c)
for row in range(r):
    if row % 2 == 0:
        for col in range(c):
            current_char = text.popleft()
            matrix[row][col] = current_char
            text.append(current_char)
    else:
        for col in range(c - 1, -1, -1):
            current_char = text.popleft()
            matrix[row][col] = current_char
            text.append(current_char)
for i in range(r):
    for j in range(c):
        print(matrix[i][j], end ="")
    print()

