word = input()
n = len(word)

for i in range(n-1, -1, -1):
    if (i + 1) % 2 == 0:
        print(word[i], end="")