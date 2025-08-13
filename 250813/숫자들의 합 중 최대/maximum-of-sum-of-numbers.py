x, y = map(int, input().split())

max_sum = 0

for num in range(x, y+1):
    num_listed = list(map(int, list(str(num))))
    max_sum = max(max_sum, sum(num_listed))

print(max_sum)