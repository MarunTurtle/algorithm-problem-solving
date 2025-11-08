n = int(input())

a = [0] + list(map(int, input().split()))

dp = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
