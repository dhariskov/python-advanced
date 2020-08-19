import os

while True:
    command = input().split("-")
    if command[0] == "End":
        break

    if command[0] == "Create":
        with open(f"{command[1]}", "w") as file:
            file.write("")
    elif command[0] == "Add":
        with open(f"{command[1]}", "a") as file:
            file.write(f"{command[2]}\n")
    elif command[0] == "Replace":
        if os.path.exists(command[1]):
            with open(command[1], "r") as file:
                temp_text = ""
                for line in file:
                    temp_text += line.replace(command[2], command[3])
                with open(command[1], "w") as file:
                    file.write(temp_text)
        else:
            print("An error occurred")

    elif command[0] == "Delete":
        if os.path.exists(command[1]):
            os.remove(command[1])
        else:
            print("An error occurred")
