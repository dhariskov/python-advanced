n = int(input())
sum_pd = 0
sum_sd = 0
matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split()])

for row_col in range(n):
    sum_pd += matrix[row_col][row_col]
    sum_sd += matrix[row_col][n - 1 - row_col]

print(abs(sum_pd-sum_sd))

