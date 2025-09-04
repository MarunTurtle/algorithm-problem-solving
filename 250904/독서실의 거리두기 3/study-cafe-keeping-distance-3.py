n = int(input())
seats = list(map(int, list(input())))
count = []

cur_count = 1
for i in range(1, n):
    if seats[i] == 0:
        cur_count += 1
    else:
        count.append(cur_count)
        cur_count = 1
# print(count)
count.sort(reverse=True)
# print(count)
ans = 0
new_a = count[0] // 2
new_b = count[0] - new_a
del count[0]
# print(count)
count.append(new_a)
count.append(new_b)
# print(count)
print(min(count))
