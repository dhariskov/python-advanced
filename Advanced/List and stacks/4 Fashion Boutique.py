box = [int(x) for x in input().split()]
rack_capacity = int(input())

rack_capacity_temp = rack_capacity
rack_count = 1
while box:
    current = box[-1]
    if rack_capacity_temp - current >= 0:
        rack_capacity_temp -= current
        box.pop()
    else:
        rack_count += 1
        rack_capacity_temp = rack_capacity

print(rack_count)
