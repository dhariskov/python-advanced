from collections import deque
males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])

matches = 0
while males and females:

    f_female = females[0]
    l_male = males[-1]

    if f_female <= 0:
        females.popleft()
        continue
    if l_male <= 0:
        males.pop()
        continue

    if f_female % 25 == 0:
        females.popleft()
        if len(females) >= 1:
            females.popleft()
        continue
    if l_male % 25 == 0:
        males.pop()
        if len(males) >= 1:
            males.pop()
        continue

    if f_female == l_male:
        males.pop()
        females.popleft()
        matches += 1
    else:
        females.popleft()
        males[-1] -= 2

print(f"Matches: {matches}")

if males:
    print(f"Males left: {', '.join([str(x) for x in males][::-1])}")
else:
    print("Males left: none")

if females:
    print(f"Females left: {', '.join([str(x) for x in females])}")
else:
    print("Females left: none")

