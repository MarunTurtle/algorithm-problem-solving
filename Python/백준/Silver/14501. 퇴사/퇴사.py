import sys
input = sys.stdin.readline

N = int(input().strip())
T = [0] * (N + 2)
P = [0] * (N + 2)
for i in range(1, N + 1):
    t, p = map(int, input().split())
    T[i], P[i] = t, p

dp = [0] * (N + 2)  # dp[N+1] = 0 기본

for i in range(N, 0, -1):
    end_day = i + T[i]  # 상담이 끝난 다음 날
    if end_day <= N + 1:
        dp[i] = max(dp[i + 1], P[i] + dp[end_day])
    else:
        dp[i] = dp[i + 1]

print(dp[1])
