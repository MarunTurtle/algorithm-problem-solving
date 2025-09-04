n = int(input())
seats = list(map(int, list(input())))
count = []

cur_count = 0
for i in range(n):
    if seats[i] == 0:
        cur_count += 1
    else:
        count.append(cur_count)
        cur_count = 0

count.sort(reverse=True)
print((count[0]+1)//2)
