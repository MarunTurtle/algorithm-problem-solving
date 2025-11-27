from itertools import combinations
import sys

INT_MIN = -sys.maxsize

n = int(input())
students = [list(map(int, input().split())) for _ in range(n)]

combos = list(combinations(students, 20))
new_combos = []
for combo in combos:
    new_combo = sorted(list(combo))
    if new_combo not in new_combos:
        new_combos.append(new_combo)

max_sum = 0

for combo in combos:
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
        # if r > 18:
        #     for row in dp[r+1]:
        #         print(*row)
        #     print("======")
    max_sum = max(max_sum, dp[20][11][9])

print(max_sum)
