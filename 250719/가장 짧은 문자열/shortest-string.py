max = float('-inf')
min = float('inf')

for _ in range(3):
    word = str(input())
    if len(word) > max:
        max = len(word)
    if len(word) < min:
        min = len(word)

print(max - min) 