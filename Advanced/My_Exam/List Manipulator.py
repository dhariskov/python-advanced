def list_manipulator(ll, *args):
    temp = []
    if len(args) > 2:
        temp = [int(x) for x in args[2:]]

    if args[0] == "add" and args[1] == "beginning":
        temp.extend(ll)
        return temp
    elif args[0] == "add" and args[1] == "end":
        ll.extend(temp)
        return ll
    elif args[0] == "remove" and args[1] == "beginning":
        if len(temp) > 0:
            for i in range(temp[0]):
                ll.pop(0)
        else:
            ll.pop(0)
        return ll
    elif args[0] == "remove" and args[1] == "end":
        if len(temp) > 0:
            for i in range(temp[0]):
                ll.pop()
        else:
            ll.pop()
        return ll


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
