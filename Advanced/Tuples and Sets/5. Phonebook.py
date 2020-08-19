phonebook = {}

while True:
    contact = input().split("-")
    if contact[0].isdigit():
        break
    phonebook[contact[0]] = contact[1]

for i in range(int(contact[0])):
    search = input()
    if search in phonebook:
        print(f"{search} -> {phonebook[search]}")
    else:
        print(f"Contact {search} does not exist.")
