from collections import deque

free_robots = deque([x.split("-") for x in input().split(";")])
starting_time =[int(x) for x in input().split(":")]
starting_time_seconds = starting_time[0]*60*60 + starting_time[1]*60 + starting_time[2]

products = deque()
busy_robots = deque()
name_product_ptime = deque()
while True:
    command = input()
    if command == "End":
        break
    products.append(command)

while products:
    if free_robots!=deque([]):
        


    if free_robots == deque([]):
        busy_robots = deque(sorted(deque(busy_robots), key=lambda x: x[2]))
        temp2 = busy_robots.popleft()
        temp2.pop()
        free_robots.append(temp2)
        starting_time_seconds += int(free_robots[0][1]) -1
        for _ in range(int(free_robots[0][1]) -1):
            products.append(products.popleft())

    if free_robots != deque([]):
        starting_time_seconds += 1
        temp = free_robots.popleft()
        temp.append(starting_time_seconds + int(temp[1]))
        busy_robots.append(temp)
        name_product_ptime.append([busy_robots[-1][0], products.popleft(), starting_time_seconds])


for name, prod, time in name_product_ptime:
    seconds = (time%3600)%60
    minutes = (time%3600)//60
    hours = time//3600
    print(f"{name} - {prod} [{hours:02d}:{minutes:02d}:{seconds:02d}]")
