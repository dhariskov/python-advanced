text = input()
dict_ch = {}
for each in text:
    if each not in dict_ch:
        dict_ch[each] = 0
    dict_ch[each] += 1

dict_ch = dict(sorted(dict_ch.items(), key=lambda x: x[0]))

for key, value in dict_ch.items():
    print(f"{key}: {value} time/s")