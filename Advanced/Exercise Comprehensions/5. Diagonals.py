n = int(input())
matrix = [input().split(", ") for i in range(n)]
print(f"First diagonal: {', '.join([matrix[i][i] for i in range(n)])}. Sum: {sum([(int(matrix[i][i])) for i in range(n)])}")
print(f"Second diagonal: {', '.join([matrix[i][n -1 -i] for i in range(n)])}. Sum: {sum([(int(matrix[i][n -1 -i])) for i in range(n)])}")