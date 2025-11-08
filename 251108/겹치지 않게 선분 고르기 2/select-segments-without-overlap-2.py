n = int(input())
lines = list(tuple(map(int, input().split())) for _ in range(n))
lines.sort(key = lambda x : (x[1], x[0]))

dp = [1] * n

for i in range(n):
    for j in range(i):
        if lines[j][1] < lines[i][1] and lines[j][0] < lines[i][0]:
            dp[i] = max(dp[i], dp[j] + 1)

print(dp)