n = int(input())
k = int(input(), 2)
count = 0

while k != 0:
  k = k - (k & -k)
  count += 1

print(count)

