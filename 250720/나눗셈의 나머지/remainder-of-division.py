a, b = map(int, input().split())

count = [0] * b

while a > 1:
    count[a % b] += 1
    a = a // b

total = sum(x ** 2 for x in count)

print(total)