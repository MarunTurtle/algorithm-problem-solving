word = input()
word = list(word)
first = word[0]
second = word[1]

for i in range(len(word)):
    if word[i] == second:
        word[i] = first

print(''.join(word))
