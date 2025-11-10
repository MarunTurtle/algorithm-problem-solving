n, m = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(n)])
w, v = [0] + list(w), [0] + list(v)

dp = [float('-inf')] * (m+1)
dp[0] = 0

for i in range(1, m+1):
    for j in range(1, n+1):
        if i >= w[j]:
            if dp[i - w[j]] != float('inf'):
                dp[i] = max(dp[i], dp[i - w[j]] + v[j])

print(max(dp))