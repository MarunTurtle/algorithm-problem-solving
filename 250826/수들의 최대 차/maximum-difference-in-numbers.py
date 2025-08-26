n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
ans = 0

for i, num in enumerate(arr):
    first_num = arr[i]
    count = 1
    for j in range(i+1, n):
        if abs(first_num - arr[j]) <= k:
            count += 1
    ans = max(ans, count)

print(ans)