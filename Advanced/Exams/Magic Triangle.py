def get_magic_triangle(n):
    triangle = []
    for i in range(n):
        triangle.append([])

    for i in range(n):
        for j in range(i+1):
            triangle[i].append(0)

    triangle[0][0] = 1
    triangle[1][0] = 1
    triangle[1][1] = 1
    for row in range(2, n):
        for col in range(row+1):
            if row == 0 and col == 0:
                triangle[row][col] = 1
            else:
                if row == 0 or col == 0:
                    triangle[row][col] = 1
                elif row == col:
                    triangle[row][col] = 1
                else:
                    triangle[row][col] = triangle[row-1][col-1] + triangle[row-1][col]

    return triangle

print(get_magic_triangle(6))
