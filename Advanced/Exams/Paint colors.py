string = input().split()

colors = ["red", "yellow", "blue", "orange", "purple", "green"]
temp_color = ""
temp_color2 = ""
result = []
# for i in range(len(string)//2):

while string:
    if len(string) > 1:
        temp_color = string[0] + string[-1]
        temp_color2 = string[-1] + string[0]
        if temp_color in colors:
            if temp_color not in result:
                result.append(temp_color)
        elif temp_color2 in colors:
            if temp_color2 not in result:
                result.append(temp_color2)
        else:
            string0 = string[0][:- 1:]
            string1 = string[-1][:- 1:]
            temp_color = string0 + string1
            if string1:
                string.insert(len(string) // 2, string1)
            if string0:
                string.insert(len(string) // 2, string0)

        string.pop(0)
        string.pop()
    elif len(string) == 1:
        temp_color = string[0]
        if temp_color in colors:
            if temp_color not in result:
                result.append(temp_color)
        string.pop()
if "orange" in result:
    if "red" not in result or "yellow" not in result:
        result.remove("orange")
if "purple" in result:
    if "red" not in result or "blue" not in result:
        result.remove("purple")
if "green" in result:
    if "blue" not in result or "yellow" not in result:
        result.remove("green")

print(result)