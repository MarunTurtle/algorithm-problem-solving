n = int(input())
# s, e, pay
jobs = [tuple(map(int, input().split())) for _ in range(n)]

jobs.sort(key = lambda x : (x[1], x[0]))

dp = [0] * n
for i in range(n):
    dp[i] = jobs[i][2]

for i in range(1, n):
    for j in range(i):
        if jobs[j][1] < jobs[i][0]:
            dp[i] = max(dp[i], dp[j] + jobs[i][2])

print(max(dp))