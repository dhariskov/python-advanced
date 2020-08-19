def func_executor(*args):
    ll = []
    for each in args:
        func = each[0]
        arguments = each[1]
        ll.append(func(*arguments))
    return ll

def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
