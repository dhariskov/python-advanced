ll = [int(x) for x in input().split()]
positive = sum(list(filter(lambda x: x > 0, ll)))
negative = sum(list(filter(lambda x: x < 0, ll)))
#abs_negative = sum(list(map(abs, negative)))
abs_negative = abs(negative)
print(negative)
print(positive)
if abs_negative > positive:
    print("The negatives are stronger than the positives")
elif abs_negative < positive:
    print("The positives are stronger than the negatives")

