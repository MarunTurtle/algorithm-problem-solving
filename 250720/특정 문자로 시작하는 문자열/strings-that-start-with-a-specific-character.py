n = int(input())

words = []

for _ in range(n):
    words.append(input())

letter = input()
count = 0
total = 0

for word in words:
    if word[0] == letter:
        count += 1
        total += len(word)

avg = f"{(total / count):.2f}"

print(count, avg)