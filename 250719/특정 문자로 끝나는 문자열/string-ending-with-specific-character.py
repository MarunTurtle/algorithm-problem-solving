words = []

for _ in range(10):
    words.append(str(input()))

letter = str(input())

for word in words:
    if word[-1] == letter:
        print(word)
