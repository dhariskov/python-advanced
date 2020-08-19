def even_odd(*args):
    command = args[-1]
    ll = args[:len(args)-1:]
    if command == "odd":
        sum_odd = list(filter(lambda x: x % 2 == 1, ll))
        return sum_odd
    elif command == "even":
        sum_even = list(filter(lambda x: x % 2 == 0, ll))
        return sum_even


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
