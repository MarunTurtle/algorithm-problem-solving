n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
ans = 0

def get_coins(r, c):
    return sum(1 if grid[r+i][c+j] == 1 else 0 for i in range(3) for j in range(3))

for i in range(n-2):
    for j in range(n-2):
        ans = max(ans, get_coins(i, j))

print(ans)