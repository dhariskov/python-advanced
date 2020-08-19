def age_assignment(*args, **kwargs):
    result = dict()
    for each in args:
        for k,v in kwargs.items():
            if each[0] == k:
                result[each] = v
    return result


print(age_assignment("Peter", "George", G=26, P=19))