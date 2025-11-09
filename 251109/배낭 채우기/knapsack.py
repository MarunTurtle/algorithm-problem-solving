N, M = map(int, input().split())
jewerly = [tuple(map(int, input().split())) for _ in range(N)]
w, v = zip(*jewerly)
w, v = list(w), list(v)

dp = [float('-inf')] * (M + 1)
dp[0] = 0

for i in range(N):
    for j in range(M, -1, -1):
        if j >= w[i]:
            if dp[j - w[i]] == float('-inf'):
                continue
            dp[j] = max(dp[j], dp[j - w[i]] + v[i])

print(-1 if dp[-1] == float('-inf') else dp[-1])
