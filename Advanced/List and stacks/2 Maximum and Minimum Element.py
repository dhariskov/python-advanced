n = int(input())

stack = []
for _ in range(n):
    token = input().split()
    if token[0] == "1":
        stack.append(int(token[1]))
    elif token[0] == "2":
        if len(stack) > 0:
            stack.pop()
    elif token[0] == "3":
        if len(stack) > 0:
            print(max(stack))
    elif token[0] == "4":
        if len(stack) > 0:
            print(min(stack))

stack = list(reversed(stack))
print(", ".join([str(x) for x in stack]))