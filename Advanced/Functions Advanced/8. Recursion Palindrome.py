def palindrome(word, index):
    if index == len(word) // 2:
        return f"{word} is a palindrome"
    else:
        if word[index] == word[-1 - index]:
            return palindrome(word, index + 1)
        else:
            return f"{word} is not a palindrome"


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
