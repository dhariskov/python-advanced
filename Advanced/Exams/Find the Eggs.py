def find_strongest_eggs(ll, n):
    new_list = [[] for i in range(n)]
    strongest_eggs = []

    while ll:
        for i in range(len(ll)):
            new_list[i % n].append(ll.pop(0))

    for each in new_list:
        is_stronger = False
        for k in range(1, len(each) // 2 +1):
            if each[len(each) // 2 - k] < each[len(each) // 2] > each[len(each) // 2 + k]:
                if each[len(each) // 2 + k] > each[len(each) // 2 - k]:
                    is_stronger = True
            if not is_stronger:
                break
        if is_stronger:
            strongest_eggs.append(each[len(each) // 2])

    return strongest_eggs


test = ([-1, 7, 3, 15, 2, 12], 2)
print(find_strongest_eggs(*test))

test = ([-1, 0, 2, 5, 2, 3], 2)
print(find_strongest_eggs(*test))

test = ([51, 21, 83, 52, 55], 1)
print(find_strongest_eggs(*test))
