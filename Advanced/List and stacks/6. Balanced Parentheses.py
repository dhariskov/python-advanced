from collections import deque

sequence = deque([x for x in input()])
flag = False
if len(sequence)%2 == 0:
    while sequence:
        if sequence[0] + sequence[-1] in "{}[]()":
            sequence.popleft()
            sequence.pop()
            flag = True
        else:
            if sequence[0]+sequence[1] in ")(}{][":
                sequence.pop()
                sequence.pop()
                flag = True
            else:
                flag = False
                break
if flag:
    print("YES")
else:
    print("NO")