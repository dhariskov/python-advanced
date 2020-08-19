# a= 97
r, c = [int(x) for x in input().split()]

# for i in range(r):
#     for j in range(c):
#         print(chr(97 + i) + chr(97 + i +j) + chr(97 + i), end=" ")
#     print()

#matrix = [[f"{chr(97 + i)}{chr(97+i+j)}{chr(97+i)}" for j in range(c)] for i in range(r)]
print("\n".join([" ".join(row) for row in [[f"{chr(97 + i)}{chr(97+i+j)}{chr(97+i)}" for j in range(c)] for i in range(r)]]))