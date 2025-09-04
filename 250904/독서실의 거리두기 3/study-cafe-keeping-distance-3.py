n = int(input())
seats = list(map(int, list(input())))
count = []

cur_count = 0
for i in range(1, n):
    if seats[i] == 0:
        cur_count += 1
    else:
        count.append(cur_count)
        cur_count = 0

count.sort()
ans = 0
for i in range(len(count)):
    count[i] -= 1
    ans = max(ans, min(count))
    count[i] += 1

print(ans)