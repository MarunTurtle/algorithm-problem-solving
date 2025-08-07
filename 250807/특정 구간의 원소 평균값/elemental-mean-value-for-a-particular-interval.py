n = int(input())
arr = list(map(int, input().split()))
count = 0
# Please write your code here.
for i in range(n):
    for j in range(i, n):
        total_sum = 0
        for k in range(i, j+1):
            total_sum += arr[k]
        avg = total_sum / (j + 1 - i)
        if avg in arr:
            count += 1
        # print(avg)

print(count)