set1 = set()
for _ in range(int(input())):
    set1 = set1.union(set(input().split()))
print("\n".join(set1))