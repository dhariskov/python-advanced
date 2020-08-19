def get_repeating_DNA(dna):
    ll = []
    result = {}
    for i in range(len(dna) - 9):
        ll.append(dna[i: i + 10:])

    ll.sort()
    for each in ll:
        if len(each) == 10:
            if each in result:
                result[each] += 1
            else:
                result[each] = 1

    return [k for k, v in result.items() if v > 1]

test = "AAAAAACCCCAAAAAACCCCTTCAAAATCTTTCAAAATCT"
result = get_repeating_DNA(test)
print(result)
test = "TTCCTTAAGGCCGACTTCCAAGGTTCGATC"
result = get_repeating_DNA(test)
print(result)
test = "AAAAAAAAAAA"
result = get_repeating_DNA(test)
print(result)
