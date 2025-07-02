a, b, c = map(int, input().split())

total = a + b + c
avg = int(total / 3)
num = int(total - avg)

print(total, avg, num, sep="\n")