from collections import deque

materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])

presents = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}
crafted_items = []

while materials and magic:
    current_material = materials.pop()
    current_magic = magic.popleft()

    if current_material == 0 and current_magic == 0:
        continue
    elif current_material == 0:
        magic.appendleft(current_magic)
        continue
    elif current_magic == 0:
        materials.append(current_material)
        continue

    total = current_magic * current_material

    if total in presents:
        crafted_items.append(presents[total])
    elif total < 0:
        sum_value = current_material + current_magic
        materials.append(sum_value)
    elif total > 0 and total not in presents:
        materials.append(current_material + 15)

successful_cases = ['Doll' in crafted_items and 'Wooden train' in crafted_items,
                    'Teddy bear' in crafted_items and 'Bicycle' in crafted_items]

if any(successful_cases):
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if materials:
    print(f'Materials left: {", ".join([str(x) for x in reversed(materials)])}')
if magic:
    print(f'Magic left: {", ".join([str(x) for x in magic])}')

presents_amount = {}
for item in crafted_items:
    if item not in presents_amount.keys():
        presents_amount[item] = crafted_items.count(item)

presents_amount = sorted(presents_amount.items(), key=lambda kvp: kvp[0])
[print(f'{k}: {v}') for k, v in presents_amount]