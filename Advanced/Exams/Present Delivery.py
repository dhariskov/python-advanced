def give_presents_all_around(neighbourhood, row, col, presents, nice_kids):
    if -1 < row + 1 < len(neighbourhood[0]):
        if neighbourhood[row + 1][col] in "X" and presents > 0:
            neighbourhood[row + 1][col] = "-"
            presents -= 1
    if -1 < row - 1 < len(neighbourhood[0]):
        if neighbourhood[row - 1][col] in "X" and presents > 0:
            neighbourhood[row - 1][col] = "-"
            presents -= 1
    if -1 < col - 1 < len(neighbourhood[0]):
        if neighbourhood[row][col - 1] in "X" and presents > 0:
            neighbourhood[row][col - 1] = "-"
            presents -= 1
    if -1 < col + 1 < len(neighbourhood[0]):
        if neighbourhood[row][col + 1] in "X" and presents > 0:
            neighbourhood[row][col + 1] = "-"
            presents -= 1
    if -1 < row + 1 < len(neighbourhood[0]):
        if neighbourhood[row + 1][col] in "V" and presents > 0:
            neighbourhood[row + 1][col] = "-"
            presents -= 1
            nice_kids -= 1
    if -1 < row - 1 < len(neighbourhood[0]):
        if neighbourhood[row - 1][col] in "V" and presents > 0:
            neighbourhood[row - 1][col] = "-"
            presents -= 1
            nice_kids -= 1
    if -1 < col - 1 < len(neighbourhood[0]):
        if neighbourhood[row][col - 1] in "V" and presents > 0:
            neighbourhood[row][col - 1] = "-"
            presents -= 1
            nice_kids -= 1
    if -1 < col + 1 < len(neighbourhood[0]):
        if neighbourhood[row][col + 1] in "V" and presents > 0:
            neighbourhood[row][col + 1] = "-"
            presents -= 1
            nice_kids -= 1
    return neighbourhood, presents, nice_kids


def giving_presents(neighbourhood, row, col, presents, nice_kids):
    if neighbourhood[row][col] == "C":
        neighbourhood, presents, nice_kids = give_presents_all_around(neighbourhood, row, col, presents, nice_kids)
        neighbourhood[row][col] = "S"
    elif neighbourhood[row][col] == "V":
        presents -= 1
        nice_kids -= 1
        neighbourhood[row][col] = "S"
    elif neighbourhood[row][col] == "X":
        neighbourhood[row][col] = "S"
    return neighbourhood, presents , nice_kids


presents = int(input())
n = int(input())
neighbourhood = [input().split() for _ in range(n)]

nice_kids = 0
for i in range(n):
    for j in range(n):
        if neighbourhood[i][j] == "S":
            row = i
            col = j
        elif neighbourhood[i][j] == "V":
            nice_kids += 1

nice_kids_initial = nice_kids
give_presents_all_around_return = None
while True:
    command = input()
    if command == "Christmas morning":
        break

    if command == "up":
        if -1 < row - 1 < n:
            neighbourhood[row][col] = "-"
            row -= 1
            neighbourhood, presents, nice_kids = giving_presents(neighbourhood, row, col, presents, nice_kids)
    elif command == "down":
        if -1 < row + 1 < n:
            neighbourhood[row][col] = "-"
            row += 1
            neighbourhood, presents, nice_kids = giving_presents(neighbourhood, row, col, presents, nice_kids)
    elif command == "left":
        if -1 < col - 1 < n:
            neighbourhood[row][col] = "-"
            col -= 1
            neighbourhood, presents, nice_kids = giving_presents(neighbourhood, row, col, presents, nice_kids)
    elif command == "right":
        if -1 < col + 1 < n:
            neighbourhood[row][col] = "-"
            col += 1
            neighbourhood, presents, nice_kids = giving_presents(neighbourhood, row, col, presents, nice_kids)

    if presents == 0:
        break
if presents == 0 and nice_kids > 0:
    print("Santa ran out of presents!")

for each in neighbourhood:
    print(" ".join([x for x in each]))
if nice_kids == 0:
    print(f"Good job, Santa! {nice_kids_initial} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids} nice kid/s.")

