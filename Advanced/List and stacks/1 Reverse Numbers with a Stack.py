numbers = input().split()

reversed_stack = []
for _ in range(len(numbers)):
    reversed_stack.append(numbers.pop())

print(" ".join([x for x in reversed_stack]))