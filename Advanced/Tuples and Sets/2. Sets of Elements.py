numb = input().split()
print("\n".join((set([input() for x in range(int(numb[0]))])).intersection(set([input() for y in range(int(numb[1]))]))))