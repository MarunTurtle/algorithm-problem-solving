a, b = map(int, input().split())

count = [0] * b

while a > 0:
    count[a % b] += 1
    a = a // b

total = sum(c ** 2 for c in count)

print(total)