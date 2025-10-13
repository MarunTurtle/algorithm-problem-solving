n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def count_gold(r, c, k):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if abs(r - i) + abs(c - j) <= k:
                cnt += grid[i][j]
    return cnt

ans = 0

for k in range(n+1):
    cost = (k**2) + ((k+1)**2)
    for r in range(n):
        for c in range(n):
            gold = count_gold(r, c, k)
            if gold * m >= cost:
                ans = max(ans, gold)

print(ans)