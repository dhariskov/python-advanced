from collections import deque

n = int(input())
petrol_distance = deque()
current_petrol = 0
index = 0
counter_index = 0
for _ in range(n):
    petrol_distance.append([int(x) for x in input().split()])

for _ in range(n):
    if petrol_distance[0][0] + current_petrol < petrol_distance[0][1]:
        petrol_distance.append(petrol_distance.popleft())
        current_petrol = 0
        index += 1 + counter_index
        counter_index = 0
    else:
        current_petrol += petrol_distance[0][0] - petrol_distance[0][1]
        petrol_distance.popleft()
        counter_index += 1

if index < n:
    print(index)
