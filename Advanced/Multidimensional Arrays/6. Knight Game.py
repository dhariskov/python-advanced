n = int(input())
matrix = []
for _ in range(n):
    matrix.append([each for each in input()])
possible_hit_coordinates = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]

biggest_counter_coordinates = dict()
to_remove = None
counter = 0
while True:
    biggest_counter_coordinates = {}
    for row in range(n):
        for col in range(n):
            if matrix[row][col] == "K":
                for each in possible_hit_coordinates:
                    if -1 < each[0] + row < n and -1 < each[1] + col < n:
                        if matrix[each[0] + row][each[1] + col] == "K":
                            if (row, col) in biggest_counter_coordinates:
                                biggest_counter_coordinates[(row, col)] += 1
                            else:
                                biggest_counter_coordinates[(row, col)] = 1
    if biggest_counter_coordinates == {}:
        break
    else:
        biggest_counter_coordinates = dict(sorted(biggest_counter_coordinates.items(), key=lambda x: -x[1]))
        for k, v in biggest_counter_coordinates:
            to_remove = (k, v)
            del biggest_counter_coordinates[to_remove]

            if matrix[k][v] == "K":
                matrix[k][v] = "0"
                counter += 1
            break

print(counter)
