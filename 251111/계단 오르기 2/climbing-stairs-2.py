n = int(input())
coin = [0] + list(map(int, input().split()))
dp = [float('-inf')] * (n+1)
ones = [0] * (n+1)

cnt = 0
dp[0] = 0
dp[1] = coin[1]
ones[1] = 1
ans = 0

def dfs(i, dp, ones):
    global ans

    if i == n + 1:
        ans = max(ans, dp[n])
        return

    if i == n - 1 and ones[i-2] == 3 and ones[i-1] == 3:
        return

    for j in range(1, 3):
        if ones[i - j] == 3:
            if j == 1:
                continue
        else:
            dp[i] = dp[i - j] + coin[i]
            ones[i] = ones[i-j]
            if j == 1:
                ones[i] += 1
            dfs(i + 1, dp, ones)
            dp[i] = 0
            ones[i] = 0
            dfs(i + 1, dp, ones)

dfs(2, dp, ones)
print(ans)