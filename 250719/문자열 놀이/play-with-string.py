word, n = input().split()
n = int(n)
word = list(word)

for _ in range(n):
    command, x, y = input().split()
    if command == '1':
        x, y = int(x), int(y)
        temp = word[x-1]
        word[x-1] = word[y-1]
        word[y-1] = temp
        print(''.join(word))
    else:
        for i in range(len(word)):
            if word[i] == x:
                word[i] = y
        print(''.join(word))
