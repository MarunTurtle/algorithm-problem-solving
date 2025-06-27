m = int(input())

start = max(0, m - (9 * len(str(m))))

for num in range(start, m):
  digits = list(map(int, str(num)))
  total = num
  for i in range(len(digits)):
    total += digits[i]

  if total == m:
    print(num)
    break
else:
  print(0)