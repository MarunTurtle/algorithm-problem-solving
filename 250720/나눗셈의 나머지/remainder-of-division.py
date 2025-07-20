a, b = map(int, input().split())

count = [0]*b

while a > 0:
    count[a % b] += 1
    a = a // b
total = 0

for i in range(b):
    total += count[i]**2

print(total)