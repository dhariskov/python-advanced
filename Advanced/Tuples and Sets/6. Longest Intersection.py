longest_interaction = set()
for i in range(int(input())):
    set1 = set()
    set2 = set()
    ranges = input().split("-")
    first_range = ranges[0].split(",")
    second_range = ranges[1].split(",")
    for i in range(int(first_range[0]), int(first_range[1]) + 1):
        set1.add(i)

    for j in range(int(second_range[0]), int(second_range[1]) + 1):
        set2.add(j)

    if len(longest_interaction) < len(set1.intersection(set2)):
        longest_interaction = set1.intersection(set2)

print(f"Longest intersection is {list(longest_interaction)} with length {len(longest_interaction)}")
