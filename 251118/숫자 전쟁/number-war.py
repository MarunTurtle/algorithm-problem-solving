n = int(input())
a = [0] + list(map(int, input().split())) + [0]
b = [0] + list(map(int, input().split())) + [0]

dp = [[-1] * (n+1) for _ in range(n+1)]
dp[0][0] = 0

for i in range(n):
    for j in range(n):
        if dp[i][j] == -1:
            continue
        
        if a[i + 1] > b[j + 1]:
            dp[i][j+1] = max(dp[i][j+1], dp[i][j] + b[j+1])
        
        if a[i + 1] < b[j + 1]:
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
        
        dp[i+1][j+1] = max(dp[i][j], dp[i+1][j+1])

ans = 0

for i in range(n):
    ans = max(ans, dp[i][n])
    ans = max(ans, dp[n][i])

print(ans)