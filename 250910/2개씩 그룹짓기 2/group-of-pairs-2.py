n = int(input())
arr = list(map(int, input().split()))

arr.sort()
ans = float('inf')

for i in range(n):
    diff = arr[i + n] - arr[i]
    ans = min(ans, diff)

print(ans)