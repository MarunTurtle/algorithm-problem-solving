n = int(input())
arr = [0] + list(map(int, input().split()))
m = sum(arr)
dp = [float('-inf')] * (m + 1)
dp[0] = 0
diff = [float('inf')] * (m+1)
max_value = 0

for j in range(1, n+1):
    for i in range(m, -1, -1):
        if i >= arr[j]:
            if dp[i - arr[j]] != float('-inf'):
                dp[i] = max(dp[i], dp[i - arr[j]] + 1)
                diff[i] = min(diff[i], abs(i * 2 - m))

print(min(diff))