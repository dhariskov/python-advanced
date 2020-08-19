def fix_calendar(numbers):
    for j in range(len(numbers)):
        for i in range(len(numbers) -1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
    return numbers


numbers = [3, 2, 1]
fixed = fix_calendar(numbers)
print(fixed)
