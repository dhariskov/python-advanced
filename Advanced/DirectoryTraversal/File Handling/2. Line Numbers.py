with open("text.txt", "r") as file:
    full_text = ""
    for idx, line in enumerate(file):
        counter_letters = 0
        counter_punctuation = 0
        for each in line:
            if each in "',:;.!?-\"":
                counter_punctuation += 1
            elif each.isalpha() or each.isdigit():
                counter_letters += 1

        full_text += f"Line {idx + 1}: {line[:-2]} ({counter_letters}) ({counter_punctuation})\n"
    with open("otput.txt" , "w") as f:
        f.write(full_text)

