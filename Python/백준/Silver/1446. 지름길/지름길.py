import sys
input = sys.stdin.readline

N, D = map(int, input().split())

shortcuts = [[] for _ in range(D + 1)]
for _ in range(N):
    a, b, w = map(int, input().split())
    if a > D or b > D:
        continue  
    shortcuts[a].append((b, w))

INF = 10**9
dp = [INF] * (D + 1)
dp[0] = 0

for i in range(D):
    if dp[i] + 1 < dp[i + 1]:
        dp[i + 1] = dp[i] + 1
    for e, w in shortcuts[i]:
        if dp[i] + w < dp[e]:
            dp[e] = dp[i] + w

print(dp[D])
