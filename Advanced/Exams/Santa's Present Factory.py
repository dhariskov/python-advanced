boxes_materials = [int(x) for x in input().split()]
magic_val = [int(x) for x in input().split()]

presents_values = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

crafted_presents = {
    "Bicycle": 0,
    "Doll": 0,
    "Teddy bear": 0,
    "Wooden train": 0
}
is_done = False
while boxes_materials and magic_val:
    material = boxes_materials[-1]
    magic = magic_val[0]
    total_magic_level = material * magic
    if total_magic_level in presents_values:
        crafted_presents[presents_values[total_magic_level]] += 1
        boxes_materials.pop()
        magic_val.pop(0)
    else:
        if total_magic_level < 0:
            temp = material + magic
            boxes_materials.pop()
            magic_val.pop(0)
            boxes_materials.append(temp)
        elif total_magic_level > 0:
            magic_val.pop(0)
            boxes_materials[-1] += 15
        elif total_magic_level == 0:
            if material == 0:
                boxes_materials.pop()
            if magic == 0:
                magic_val.pop(0)

if crafted_presents["Doll"] > 0 and crafted_presents["Wooden train"] > 0 or crafted_presents["Teddy bear"] > 0 and crafted_presents["Bicycle"] > 0:
    is_done = True

if is_done:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if sum(boxes_materials) > 0:
    print(f"Materials left: {', '.join([str(m) for m in boxes_materials[::-1]])}")
if len(magic_val) > 0:
    print(f"Magic left: {', '.join([str(m) for m in magic_val])}")

crafted_presents = dict(sorted(crafted_presents.items(), key=lambda x: x[0], reverse=False))
for k, v in crafted_presents.items():
    if v > 0:
        print(f"{k}: {v}")
