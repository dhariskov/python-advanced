command = input()
numbers = [int(x) for x in input().split()]
if command == "Odd":
    sum_odd = (sum(list(filter(lambda x: x % 2 == 1, numbers)))) * len(numbers)
    print(sum_odd)
elif command == "Even":
    sum_even = sum(list(filter(lambda x: x % 2 == 0, numbers))) * len(numbers)
    print(sum_even)
