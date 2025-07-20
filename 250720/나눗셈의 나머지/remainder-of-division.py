a, b = map(int, input().split())

count = [0] * b

while a > 1:
    rmder = a % b
    count[rmder] += 1
    a = a // b

total = sum(x ** 2 for x in count)

print(total)