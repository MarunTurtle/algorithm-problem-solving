n = int(input())

total = 0

for i in range(n):
    total += int(input())

total = str(total)[1:] + str(total)[0]

print(total)
