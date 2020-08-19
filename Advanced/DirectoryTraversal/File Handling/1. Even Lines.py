with open("text.txt", "r") as file:
    for n, line in enumerate(file):
        if n % 2 == 0:
            for el in "-.,!?":
                line = line.replace(el, "@")
                printer = line.split()
            print(" ".join([x for x in printer[::-1]]))
