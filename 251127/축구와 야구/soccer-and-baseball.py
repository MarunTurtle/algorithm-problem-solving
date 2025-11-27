from itertools import combinations
import sys

INT_MIN = -sys.maxsize

n = int(input())
students = [list(map(int, input().split())) for _ in range(n)]

students.sort(key=lambda x: (x[0], x[1]))

combo = students[:20]

max_sum = 0

dp = [[[0] * 10 for _ in range(12)]for _ in range(21)]
dp[0][0][0] = 0
dp[1][1][0] = combo[0][0]
dp[1][0][1] = combo[0][1]

for r in range(1, 20):
    for i in range(12):
        for j in range(10):
            if dp[r][i][j] != 0:
                if i+1 < 12:
                    dp[r+1][i+1][j] = max(dp[r+1][i+1][j], dp[r][i][j] + combo[r][0])
                if j+1 < 10:
                    dp[r+1][i][j+1] = max(dp[r+1][i][j+1], dp[r][i][j] + combo[r][1])

max_sum = max(max_sum, dp[20][11][9])

print(max_sum)
