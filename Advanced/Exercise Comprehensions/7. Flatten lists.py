string = input().split("|")
# for i in range(len(string) - 1, -1, -1):
#     string[i] = string[i].split()
#     #print(string[i])
#     print(" ".join(string[i]), end=" ")
# print()

#print(" ".join([" ".join(each.split()) for each in [string[i] for i in range(len(string) - 1, -1, -1)]]))

print(" ".join([el for x in string[::-1] for el in x.split()]))