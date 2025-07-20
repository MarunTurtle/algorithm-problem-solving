word = input()

for i in range(len(word)):
    if word[i] == 'e':
        word = word[0:i] + word[i+1:]
        break

print(word)
