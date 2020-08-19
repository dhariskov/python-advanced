import math

string = input().split()

result = 0
# string = [int(x) if x not in "+-*/" else x for x in string]
eval_result = ""
result = 0

temp = []
for i in range(len(string)):
    if string[i] not in "+-*/":
        temp.append(string[i])
    else:
        result = eval(string[i].join(temp))
        temp = [str(math.floor(result))]

print(int(temp[0]))
