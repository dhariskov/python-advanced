from collections import deque

food_quantity = int(input())
orders = input().split()

orders = deque([int(x) for x in orders])
print(max(orders))

current = ""
is_completed = True
while orders:
    current = orders[0]
    if food_quantity - current >= 0:
        food_quantity -= current
        orders.popleft()
    else:
        print(f"Orders left: {' '.join([str(x) for x in orders])}")
        is_completed = False
        break

if is_completed:
    print("Orders complete")
