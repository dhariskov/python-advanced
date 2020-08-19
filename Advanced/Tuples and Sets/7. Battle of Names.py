set_even = set()
set_odd = set()
for i in range(1, int(input()) + 1):
    sum_name = sum([ord(x) for x in input()]) // i
    if sum_name % 2 == 0:
        set_even.add(sum_name)
    else:
        set_odd.add(sum_name)
even_sum = sum(set_even)
odd_sum = sum(set_odd)
if even_sum == odd_sum:
    print(", ".join([str(x) for x in set_odd.union(set_even)]))
elif odd_sum > even_sum:
    print(", ".join([str(x) for x in set_odd.difference(set_even)]))
elif even_sum > odd_sum:
    print(", ".join([str(x) for x in set_odd.symmetric_difference(set_even)]))
