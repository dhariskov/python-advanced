import os

path = input()
dict_result = {}
separator_count = path.count(os.path.sep)

for root, directories, files in os.walk(path):
    if separator_count - root.count("\\") > 1:
        continue
    for file in files:
        extension = file.split(".")[-1]
        if extension not in dict_result:
            dict_result[extension] = []
        dict_result[extension].append(file)

result_str = ""
for k, v in sorted(dict_result.items()):
    result_str += f".{k}\n"
    for file in sorted(v):
        result_str += f"---{file}\n"

desktop = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop")
final_location = desktop + os.path.sep + "report.txt"
with open(final_location, "w") as file:
    file.write(result_str)
