import sys

input = sys.stdin.readline
INT_MIN = -10**18  # 충분히 작은 음수

n = int(input().strip())
students = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[INT_MIN] * 10 for _ in range(12)]
dp[0][0] = 0

for s, b in students:
    for i in range(11, -1, -1):
        for j in range(9, -1, -1):
            if dp[i][j] == INT_MIN:
                continue
            if i + 1 <= 11:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + s)
            if j + 1 <= 9:
                dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + b)

ans = dp[11][9]
print(ans)
