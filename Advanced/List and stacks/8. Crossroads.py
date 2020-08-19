from collections import deque
flag = True
queue_car = deque()
car = ""
current_car = deque()
green_light = int(input())
green_light_left = 0
free_window = int(input())
total_cars_passed = 0
while True:
    command = input()
    if command == "END":
        break
    queue_car.append(command)

while queue_car:
    if queue_car[0] == "green":
        queue_car.popleft()
    #queue_car.popleft()
    if len(queue_car) == 0:
        break
    while queue_car[0] != "green":
        car = queue_car.popleft()
        total_cars_passed += 1
        current_car = deque([x for x in car])
        for i in range(green_light, 0, -1):
            if len(current_car) > 0:
                current_car.popleft()
                green_light_left -= 1
            else:
                if len(queue_car) == 0:
                    break
                car = queue_car.popleft()
                if car =="green":
                    break

                current_car = deque([x for x in car])
                total_cars_passed += 1
                current_car.popleft()
                green_light_left -= 1
        for j in range(free_window, 0, -1):
            if len(queue_car) == 0:
                break
            if len(current_car) > 0:
                current_car.popleft()
                green_light_left -= 1
            else:
                break
        if len(current_car)>0:
            print(f"A crash happened!\n{car} was hit at {current_car.popleft()}.")
            flag = False
            break
        if len(queue_car) == 0:
            break
        if green_light_left == 0:
            break
    if green_light_left == 0:
        break
if flag:
    print(f"Everyone is safe.\n{total_cars_passed} total cars passed the crossroads.")