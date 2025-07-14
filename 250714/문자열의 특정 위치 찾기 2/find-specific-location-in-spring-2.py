words = ['apple', 'banana', 'grape', 'blueberry', 'orange']

l = input()
cnt = 0

for word in words:
    if word[2] == l or word[3] == l:
        print(word)
        cnt += 1

print(cnt)