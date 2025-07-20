word1 = input()
word2 = input()

def erase_letter(word):
    ans = ""
    for letter in word:
        if letter.isdigit():
            ans += str(letter)
    return int(ans)

num1 = erase_letter(word1)
num2 = erase_letter(word2)

print(num1+num2)