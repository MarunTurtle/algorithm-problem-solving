word = input()
sub = input()

n = len(word)
m = len(sub)

count = 0

for i in range(n - m + 1):
    if word[i:i+m] == sub:
        count += 1

print(count)